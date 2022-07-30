
import java.io.IOException;
import java.time.temporal.Temporal;
import java.util.*;

import static java.lang.System.out;

/**
 * A App e responsável pela execuçao do programa.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class App {
    static Scanner scan = new Scanner(System.in);
    static Controller controller = new Controller();

    /**
     * Metodo main que corre o programa.
     * @param args
     * @throws InterruptedException
     * @throws IOException
     * @throws ClassNotFoundException
     */
    public static void main(String[] args) throws InterruptedException, IOException, ClassNotFoundException {

        View view = new View(controller, scan);
        view.run();

    }


}