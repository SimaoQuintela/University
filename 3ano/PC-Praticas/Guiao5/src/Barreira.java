public class Barreira {
    public int c = 0;
    public int awake = 0;
    public final int N;
    public int e;

    public Barreira(int N) {
        this.N = N;
    }

    // este método sincroniza as N threads
    public synchronized void await() throws InterruptedException {
        // manda uma thread esperar caso esta esteja a tentar executar antes das outras estarem todas acordadas
        while (this.c == this.N) {
            wait();
        }

        this.c+=1;
        if (this.c < this.N) {
            while (this.c < this.N) {
                wait();
            }
        } else {
            notifyAll();
        }

        this.awake+=1;
        if (this.awake == this.N){
            this.awake = 0;
            this.c = 0;
            notifyAll();
        }
    }
}



// outra implementação, com épocas
// não podemos passar da época 0 para a época 1 sem que todas as threads da época 0 tenham acabado de executar
public class Barreira {
    public int c = 0;
    public int e = 0;
    public final int N;


    public Barreira(int N) {
        this.N = N;
    }

    // este método sincroniza as N threads
    public synchronized void await() throws InterruptedException {
        this.c+=1;

        if (this.c < this.N) {
            int e_local = this.e;
            while (this.e == e_local) {
                wait();
            }
        } else {
            notifyAll();
            this.c = 0;
            this.e += 1;
        }

    }
}
