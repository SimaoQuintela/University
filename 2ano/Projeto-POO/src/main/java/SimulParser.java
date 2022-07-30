import static java.lang.System.out;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

/**
 * A classe SimulParser le o ficheiro de configuraçao de um simulaçao.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class SimulParser {

    /**
     * Metodo que responsavel pelo particionamento do conteudo do ficheiro de simulaçao
     * @param file Ficheiro de simulaçao.
     * @return TreeMap que contem o conteudo do ficheiro particionado.
     */
    public static TreeMap<String, List<List<String>>> simulParser(String file){
        List<String> linhas = lerFicheiro(file);
        List<String[]> linhasSplitted = new ArrayList<>();
        TreeMap<String, List<List<String>>> actions = new TreeMap<>();

        for(String l: linhas){
            linhasSplitted.add(l.split(","));
        //    out.println(Arrays.toString(l.split(",")));
        }

        String linhaMaisRecente = linhasSplitted.get(0)[0];
        //out.println(linhaMaisRecente);


        for(String[] l: linhasSplitted){
            linhaMaisRecente = l[0];
            List<String> modif = new ArrayList<>();
            for(String s: l) {
                if (!s.equals(linhaMaisRecente))     // são diferentes
                    modif.add(s);
            }

            if(actions.containsKey(l[0])){
                actions.get(l[0]).add(modif);
            } else {
                List<List<String>> novo = new ArrayList<>();
                actions.put(linhaMaisRecente,novo);
                actions.get(linhaMaisRecente).add(modif);
            }
        }


        return actions;
    }

    /**
     * Metodo que le o conteudo de um ficheiro.
     * @param nomeFich Ficheiro.
     * @return Lista de Strings lidas do ficheiro.
     */
    public static List<String> lerFicheiro(String nomeFich) {
        List<String> lines;
        try { lines = Files.readAllLines(Paths.get(nomeFich), StandardCharsets.UTF_8); }
        catch(IOException exc) { lines = new ArrayList<>(); }
        return lines;
    }




}
