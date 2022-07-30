import java.util.Random;

import static java.lang.System.out;

public class Euromilhoes {
    private int[] numeros;
    private int[] estrelas;

    public Euromilhoes(int numNumeros, int numEstrelas){
        numeros = new int[numNumeros];
        estrelas = new int[numEstrelas];
    }

    public void gerarChave(){
        Random ran = new Random();
        int i;
        int randomNumero;
        int randomEstrela;

        for(i=0; i<5; i+=1){
            // gera um número entre 1 e 50
            randomNumero = ran.nextInt(50) +1;
            this.numeros[i] = randomNumero;
        }

        for(i=0; i<2; i+=1){
            // gera uma estrela entre 1 e 9
            randomEstrela = ran.nextInt(9) +1;
            this.estrelas[i] = randomEstrela;
        }

    }

    public void imprimeChave(){
        int i;
        out.print("Numeros: ");
        for(i=0; i<5; i+=1){
            out.print(numeros[i]);
            out.print(" ");
        }

        out.println(" ");

        out.print("Estrelas: ");
        for(i=0; i<2; i+=1){
            out.print(estrelas[i]);
            out.print(" ");
        }

        out.println(" ");

    }

    public void comparaAposta(int[] numerosUser, int[] estrelasUser){
        int numGuessed = 0;
        int estrelasGuessed = 0;

        for(int i =0; i<5; i+=1){
            if(this.numeros[i] == numerosUser[i]){
                numGuessed += 1;
            }
        }

        for(int i =0; i<2; i+=1){
            if(this.estrelas[i] == estrelasUser[i]){
                estrelasGuessed += 1;
            }
        }

        out.println("Acertou em " + numGuessed + " numeros");
        out.println("Acertou em " + estrelasGuessed + " estrelas");
    }


}
