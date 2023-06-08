import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

class InvalidAccount extends Exception {}
class NotEnoughFunds extends Exception {}


public class Bank {
    private static class Account {
        Lock l = new ReentrantLock();
        private int balance = 0;
        public int balance() {return this.balance; }
        public void deposit(int val) {this.balance += val;}
        public synchronized void withdraw(int val) throws NotEnoughFunds {
            if(balance < val) throw new NotEnoughFunds();
            balance -= val;
        }
    }

    private Map<Integer, Account> acs = new HashMap<>();
    //private Lock l = new ReentrantLock();
    private ReentrantReadWriteLock rwl = new ReentrantReadWriteLock();
    private int nextId = 0;

    public int createAccount(int bal){
        Account c = new Account();
        c.deposit(bal);

        rwl.writeLock().lock();
        try {
            int id = nextId;
            nextId += 1;
            acs.put(id, c);
            return id;
        } finally {
            rwl.writeLock().unlock();
        }
    }

    public int closeAccount(int id) throws InvalidAccount{
        Account c;
        rwl.writeLock().lock();
        try {
            c = acs.get(id);
            if (c == null) {
                throw new InvalidAccount();
            }
            acs.remove(id);
            c.l.lock();
        } finally {
            rwl.writeLock().unlock();
        }

        try{
            return c.balance();
        } finally {
            c.l.unlock();
        }

    }

    public int balance(int id) throws InvalidAccount{
        if(id <0 || id >= acs.size()){
            throw new InvalidAccount();
        }
        return acs[id].balance();
    }

    public void deposit(int id, int val) throws InvalidAccount{
        if(id <0 || id >= acs.size()){
            throw new InvalidAccount();
        }
        acs[id].deposit(val);
    }

    public void withdraw(int id, int val) throws InvalidAccount, NotEnoughFunds{
        if(id <0 || id >= acs.size()){
            throw new InvalidAccount();
        }
        Account c = acs[id];
        c.withdraw(val);

    }

    public int totalBalance(int[] accounts) throws InvalidAccount{
        accounts = accounts.clone();
        Arrays.sort(accounts);
        Account[] a = new Account[accounts.length];
        rwl.readLock().lock();
        try {
            for (int i = 0; i<accounts.length; i++){
                a[i] = acs.get(accounts[i]);
                if(a[i] == null) throw new InvalidAccount();
            }

            for (int i = 0; i<accounts.length; i++){
                a[i].l.lock();
            }
        } finally {
            rwl.readLock().unlock();
        }

        int total = 0;
        for (Account c: a){
            total += c.balance;
            c.l.unlock();
        }
        return total;
    }

    public void transfer(int from, int to, int val) throws InvalidAccount, NotEnoughFunds {
        Account acfrom;
        Account acto;
        rwl.readLock().lock();
        try {
            acfrom = acs.get(from);
            acto = acs.get(to);
            if(acfrom == null || acto == null) throw new InvalidAccount();

            if(from < to){
                acfrom.l.lock();
                acto.l.lock();
            } else {
                acto.l.lock();
                acfrom.l.lock();
            }
        } finally {
            rwl.readLock().unlock();
        }

        acfrom.withdraw(val);
        acfrom.l.unlock();
        acto.deposit(val);
        acto.l.unlock();

        /*
        funciona mas pouca concorrência
        try {
            acfrom.withdraw(val);
            acto.deposit(val);
        } finally {
            acfrom.l.unlock();
            acto.l.unlock();
        }
         */

        // funciona bem
        try {
            try {
                acfrom.withdraw(val);
            } finally {
                acfrom.l.unlock();
            }
            acto.deposit(val);
        } finally {
            acto.l.unlock();
        }



    }
}

class Main{
    public static void main(String[] args) throws Exception {
        final int n_contas = 10 ;//Integer.parseInt(args[0]);
        Bank b = new Bank();

        for (int i=0; i < n_contas; i++){
            b.deposit(i, 1000);
        }

        int[] ids = new int[n_contas];
        for (int i=0; i<n_contas; i++) ids[i] = i;

        new Thread(() -> {
            Random r = new Random();
            try{
                while(true){
                    int from = r.nextInt(n_contas);
                    int to = r.nextInt(n_contas);

                    b.transfer(from, to, 10);
                    int total = b.totalBalance(ids);
                    System.out.println("Thread 1: " + total + " from: " + from + " to: " + to);
                    //sleep(1000);

                }
            } catch(Exception ignored){}
        }).start();

        new Thread(() -> {
            Random r = new Random();
            try{
                while(true){
                    int total = b.totalBalance(ids);
                    System.out.println("Thread 2: " + total);
                    //sleep(1000);
                    //if(total != n_contas*1000) System.out.println("Balanço total errado: " + total);
                }
            } catch(Exception ignored){}
        }).start();





    }
}