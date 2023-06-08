package ex1;

import static java.lang.System.out;
public class Main {
    public static void main(String[] args) {
        final int N =3;
        final int I = 3;
        Counter counter = new Counter();

        for (int i = 0; i < N; i++) {
            Incrementer t = new Incrementer(counter, I);

            t.start();
        }

        counter.printX();
        out.println("Done");
    }
}

class Counter{
    public int x;

    public Counter(){
        this.x = 0;
    }

    public void increment() {
        this.x++;
    }

    public void printX(){
        out.println(x);
    }
}

class Incrementer extends Thread{
    private Counter c;
    private final int I;

    public Incrementer(Counter counter, int i){
        this.c = counter;
        this.I = i;
    }

    public void run(){
        for(int i=1; i<=I; i++){
            this.c.increment();
            this.c.printX();
        }
    }


}