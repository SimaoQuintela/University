import javax.sound.sampled.Port;
import java.util.*;
import java.util.concurrent.locks.*;

public class WareHouse {
    private Lock l = new ReentrantLock();
    public class Product{
        int quant;
        Condition c = l.newCondition();
    }
    Map<String, Product> map = new HashMap<>();

    private Product getProduct(String item){
        Product p = map.get(item);
        if(p == null){
            p = new Product();
            map.put(item, p);
        }
        return p;
    }

    public void supply(String item, int quantity){
        l.lock();
        try{
            Product p = getProduct(item);
            p.quant += quantity;
            p.c.signalAll();
        } finally {
            l.unlock();
        }
    }

    // versão egoísta
    public void consume(String[] item) throws InterruptedException{
        l.lock();
        try{
            for(String product: item){
                Product p = getProduct(product);
                while(p.quant == 0){
                    p.c.await();
                }
                p.quant -= 1;
            }
        } finally {
            l.unlock();
        }
    }


    private Product missing(Product[] ps){
        for(Product p: ps){
            if (p.quant == 0){
                return p;
            }
        }
        return null;
    }

    // versão não egoísta
    // verificamos se há todos os ‘items’ disponíveis, se houver decrementamos, senão esperamos e verificamos de novo
    public void consume2(String[] items) throws InterruptedException{
        l.lock();
        try{
            Product[] ps = new Product[items.length];
            for(int i = 0; i<items.length; i++)
                ps[i] = getProduct(items[i]);

            Product p;
            do {
                p = missing(ps);
                if(p != null){
                    p.c.await();
                }
            } while(p != null);


            for(Product p2: ps){
                p2.quant -= 1;
            }

        } finally {
            l.unlock();
        }
    }

}
