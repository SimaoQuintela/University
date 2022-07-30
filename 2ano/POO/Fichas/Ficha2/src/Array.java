import static java.lang.System.out;
import java.util.Scanner;
import java.util.Arrays;

public class Array {
    Scanner scan = new Scanner(System.in);
    // 1. a)
    public int lerDevolverMinimo(int size) {
        int[] array = new int[size];
        int i;

        for (i = 0; i < size; i += 1) {
            System.out.print("Insere um numero: ");
            int numero = scan.nextInt();
            array[i] = numero;
        }

        int min = array[0];
        for (i = 0; i < size; i += 1)
            if (array[i] < min)
                min = array[i];

        return min;
    }

    // 1. b)
    public void lerDevolverEntreIndices(int size) {
        int[] array = new int[size];
        int i;

        for (i = 0; i < size; i += 1) {
            out.print("Insere um numero: ");
            int numero = scan.nextInt();
            array[i] = numero;
        }
        out.print("Indice 1: ");
        int indice1 = scan.nextInt();
        out.print("Indice 2: ");
        int indice2 = scan.nextInt();

        if (indice1 < 0 || indice2 >= size) {
            out.print("Index out of bound");
        }

        int[] noMeio = new int[indice2-indice1];

        for (i = 0; i < indice2-indice1; i += 1) {
            noMeio[i] = array[i + indice1];
            out.print(noMeio[i]);
        }
    }

    // 1. c)
    public void comumAosDois(int size, int[] comuns){
        int[] array1 = new int[size];
        int[] array2 = new int[size];
        int i,j;
        // colocar valores no array1
        for(i = 0; i<size; i+=1){
            out.print("Array1 posicao " + i + ": ");
            array1[i] = scan.nextInt();
        }
        // colocar valores no array2
        for(i = 0; i<size; i+=1){
            out.print("Array2 posicao " + i + ": ");
            array2[i] = scan.nextInt();
        }

        // PROBLEMA AQUI AO IMPRIMIR
        // ver quais os elementos em comum
        for(i=0, j=0; i<size; i+=1){
            if(Arrays.binarySearch(array2, array1[i]) >= 0) {
                comuns[j] = array1[i];
                out.print(comuns[j]);
            }
            j += 1;

        }

    }

    // 4. a)
    public void ordena(int[] array){
        Arrays.sort(array);
    }

    // 4. b)
    public int procuraBinaria(int[] array, int x){
        ordena(array);
        return(Arrays.binarySearch(array, x));
    }


}
