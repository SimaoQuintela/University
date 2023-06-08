class Producer extends Thread {
    BoundedBuffer bb;

    Producer(BoundedBuffer bb) {
        this.bb = bb;
    }

    public void run() {
        try {
            for (int i = 0; i < 100000; i++) {
                try {
                    sleep(1000);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
                System.out.println("Vou fazer put de " + i);
                bb.put(i);
                System.out.println("Put de " + i + " retornou");
            }
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}

class Consumer extends Thread{
    BoundedBuffer bb;
    Consumer(BoundedBuffer bb) { this.bb = bb;}

    public void run() {
        try {
            for (int i = 1; i < 100000; i++) {
                System.out.println("Vou fazer get");
                int v = bb.get();
                System.out.println("Get retornou " + v);
                sleep(2000);

            }
        } catch(InterruptedException e){
            throw new RuntimeException(e);
        }
    }
}


public class Main {
    public static void main(String[] args) throws InterruptedException {
        BoundedBuffer bb = new BoundedBuffer(10);
        new Producer(bb).start();
        new Consumer(bb).start();
    }

}