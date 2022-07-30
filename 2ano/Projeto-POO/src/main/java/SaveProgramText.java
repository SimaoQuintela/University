import CasaInteligente.CasaInteligente;
import ComercializadoresEnergia.Comercializador;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Set;

/**
 * Esta class guarda o programa num ficheiro de texto.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class SaveProgramText {

    /**
     * Metodo que guarda o programa num ficheiro de texto.
     * @param c Comunidade.
     * @param file Ficheiro.
     * @throws IOException
     */
    public static void saveTextMode(Comunidade c, String file) throws IOException {
        FileWriter writer = new FileWriter(file);

        int tax = 0;
        int baseValue = 0;


        for(Comercializador com: c.getMercado().values()){
            tax = com.getImposto();
            baseValue = com.getValorBase();
            break;
        }

        writer.write("Imposto:" + tax + "\n");
        writer.flush();
        writer.write("ValorBase:" + baseValue + "\n");
        writer.flush();

        for (Comercializador c2: c.getMercado().values()) {
            c2.writeInFile(writer);
        }

        for(CasaInteligente casa: c.getCasas().values()){
            casa.writeInFile(writer);
        }

        writer.close();
    }
}
