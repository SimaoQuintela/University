import java.util.concurrent.Semaphore;

public class Main {
    static Barreira b = new Barreira(3);
    static int count = 0;

    public static void main(String[] args) {
        for (int i = 0; i < 3; i++) {
            int j = i;
            new Thread(() -> {
                try {
                    while(true) {
                        Thread.sleep(1000);
                        System.out.println("Antes " + count);
                        //System.out.println(b.c);
                        //System.out.println(b.awake);
                        b.await();
                        //System.out.println(b.c);
                        //System.out.println(b.awake);
                        System.out.println("Depois " + count);
                        count+=1;
                    }
                } catch (Exception e) {
                }
            }).start();
        }
    }

}