import java.util.Comparator;

/**
 * Comparador de consumos.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class ConsumeComparator implements Comparator<Tuple> {

    /**
     * Metodo que compara dois tuplos.
     * @param t1 the first object to be compared.
     * @param t2 the second object to be compared.
     * @return Valor que indica o resultado da comparaçao.
     */
    public int compare(Tuple t1, Tuple t2) {
        float a1 = t1.getP2();
        float a2 = t2.getP2();

        return Float.compare(a2, a1);
    }
}
