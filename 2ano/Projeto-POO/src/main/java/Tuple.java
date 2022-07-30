import java.io.Serializable;
import java.security.SecureRandomParameters;

/**
 * Tuple implementa uma estrutura para representaçao de tuplos.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Tuple implements Serializable {
    private String p1;
    private float p2;

    /**
     * Construtor por omissao.
     */
    public Tuple(){
        this.p1 = "";
        this.p2 = 0;
    }

    /**
     * Construtor parametrizado.
     * @param p1 Primeiro parametro.
     * @param p2 Segundo parametro.
     */
    public Tuple(String p1, Float p2){
        this.p1 = p1;
        this.p2 = p2;
    }

    /**
     * Construtor de copia.
     * @param t Tuplo que e copiado.
     */
    public Tuple(Tuple t){
        this(t.getP1(), t.getP2());
    }

    /**
     * Metodo que averigua a igualdade entre um tuplo e um outro objeto.
     * @param o Objeto comparado com o tuplo.
     * @return Booleano que indica o resultado da comparaçao.
     */
    public boolean equals(Object o){
        if(o == this) return true;
        if(o == null || o.getClass() != this.getClass()) return false;

        Tuple t = (Tuple) o;

        return (
                this.p1.equals(t.getP1()) &&
                this.p2 == t.getP2()
                );
    }

    /**
     * Metodo que devolve uma copia do Tuplo.
     * @return Copia do Tuplo.
     */
    public Tuple clone() {
        return new Tuple(this);
    }

    /**
     * Metodo que devolve o Tuplo em formato de texto.
     * @return Tuplo em formato de texto.
     */
    public String toString(){
        StringBuilder sb = new StringBuilder();

        sb.append("(").append(this.getP1()).append(",").append(this.getP2()).append(")\n");
        return sb.toString();
    }

    /**
     * Metodo que devolve o segundo elemento do Tuplo.
     * @return Segundo elemento do Tuplo.
     */
    public float getP2() {
        return this.p2;
    }

    /**
     * Metodo que devolve o primeiro elemento do Tuplo.
     * @return Primeiro elemento do Tuplo.
     */
    public String getP1() {
        return this.p1;
    }

    /**
     * Metodo que altera o primeiro elemento do Tuplo.
     * @param p1 Primeiro elemento do Tuplo.
     */
    public void setP1(String p1) {
        this.p1 = p1;
    }

    /**
     * Metodo que altera o segundo elemento do Tuplo.
     * @param p2 Segundo elemento do Tuplo.
     */
    public void setP2(float p2) {
        this.p2 = p2;
    }
}
