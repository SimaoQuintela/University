package ex2.Public;
import static java.lang.System.out;
public class Main {
    public static void main(String[] args) {
        final int N = 3;
        final int I = 3;
        Counter counter = new Counter();

        for (int i = 0; i < N; i++) {
            myThread t = new myThread(counter, I);

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

    public void printX(){
        out.println(x);
    }
}

class myThread extends Thread{
    private final Counter c;
    private final int I;

    public myThread(Counter counter, int i){
        this.c = counter;
        this.I = i;
    }

    public void run(){
        for(int i = 1; i<=I; i++){
            this.c.x++;
            this.c.printX();
        }
    }
}