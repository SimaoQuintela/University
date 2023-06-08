import java.util.concurrent.Semaphore;

public class BoundedBuffer {
    private int a[];
    private int iput = 0;
    private int iget = 0;

    Semaphore mut = new Semaphore(1);
    Semaphore items = new Semaphore(0);
    Semaphore slots;

    public BoundedBuffer(int N){
        a = new int[N];
        this.slots = new Semaphore(N);
    }

    public int get() throws InterruptedException {
        items.acquire();
        mut.acquire();

        int v = a[iget];
        iget = (iget +1) % a.length;

        mut.release();
        slots.release();
        return v;
    }

    public void put(int v) throws InterruptedException {
        slots.acquire();
        mut.acquire();

        a[iput] = v;
        iput = (iput +1) % a.length;

        mut.release();
        items.release();
    }
}



