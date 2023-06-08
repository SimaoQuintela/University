package ex1;

import static java.lang.System.out;
class myThread extends Thread{
    public int I;

    public void run(){
        for(int i=1; i<I; i++){
            out.println(i);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            final int N = Integer.parseInt(args[0]);
            final int I = Integer.parseInt(args[1]);

            for(int i = 0; i<I; i++){
                myThread t = new myThread();
                t.I = I;

                t.start();
                t.join();
            }
            out.println("Done");
        } catch (InterruptedException e){
            e.printStackTrace();
        }
    }
}


