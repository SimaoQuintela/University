package ex2;

import java.util.Random;

class InvalidAccount extends Exception {}
class NotEnoughFunds extends Exception {}


public class Bank {
    private static class Account {
        int balance = 0;

        public synchronized int balance() {
            return this.balance;
        }
        public synchronized void deposit(int val) {
            this.balance += val;
        }
        public synchronized void withdraw(int val) throws NotEnoughFunds {
            if(balance < val){
                throw new NotEnoughFunds();
            }
            balance -= val;
        }
    }

    private Account[] acs;

    public Bank(int N){
        acs = new Account[N];
        for (int i = 0; i<N; i++){
            acs[i] = new Account();
        }
    }

    public int balance(int id) throws InvalidAccount{
        if(id <0 || id >= acs.length){
            throw new InvalidAccount();
        }
        return acs[id].balance();
    }

    public void deposit(int id, int val) throws InvalidAccount{
        if(id <0 || id >= acs.length){
            throw new InvalidAccount();
        }
        acs[id].deposit(val);
    }

    public void withdraw(int id, int val) throws InvalidAccount, NotEnoughFunds{
        if(id <0 || id >= acs.length){
            throw new InvalidAccount();
        }
        Account c = acs[id];
        c.withdraw(val);

    }

    public int totalBalance(int[] accounts) throws InvalidAccount{
        int total = 0;
        for(int id : accounts){
            total += balance(id);
        }

        return total;
    }

    public synchronized void transfer(int from, int to, int val) throws InvalidAccount, NotEnoughFunds {
        withdraw(from, val);
        deposit(to, val);
    }

}

class Main{
    public static void main(String[] args) throws Exception {
        final int n_contas = 10 ;//Integer.parseInt(args[0]);
        Bank b = new Bank(n_contas);

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

