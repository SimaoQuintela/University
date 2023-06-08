import java.util.concurrent.Semaphore;

public class Barreira {
    private int c = 0;
    private final int N;
    public Barreira (int N) {
        this.N = N;
    }

    public synchronized void await() throws InterruptedException {
        this.c += 1;
        if(c == N){
            notifyAll();
        }

        while(c == N){
            wait();
        }

    }
}

public class Main(){
    static Barreira b = new Barreira(3);

    public static void main(String[] args) {
        for (int i = 0; i < 3; i++) {
            int j = i;
            new Thread(() -> {
                try {
                    Thread.sleep(1000);
                    System.out.println("Antes");
                    b.await();
                    System.out.println("Depois");
                } catch (Exception e) {
                }
            }).start();
        }
    }

}