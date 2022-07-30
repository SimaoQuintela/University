import java.time.LocalDate;
import java.util.Scanner;
import static java.lang.System.out;

public class Ficha2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        out.print("Exercicio: ");
        int ex = scan.nextInt();
        int i,j;

        switch (ex) {
            case 1:
                // inicializar o array
                Array array = new Array();
                out.print("Alinea: ");
                String alinea1 = scan.next();
                out.print("Numero de inteiros que quer introduzir: ");
                int numeroDeInteiros = scan.nextInt();
                switch (alinea1) {
                    case "a":
                        int min = array.lerDevolverMinimo(numeroDeInteiros);
                        out.print("min: " + min);
                        break;
                    case "b":
                        array.lerDevolverEntreIndices(numeroDeInteiros);
                        break;
                    case "c":
                        int[] comuns = new int[numeroDeInteiros];
                        array.comumAosDois(numeroDeInteiros, comuns);
                        break;
                }
                break;
            case 2:
                Turma turma = new Turma(5,5);
                out.print("Alinea: ");
                String alinea2 = scan.next();

                // 2. a)
                // preencho a matriz fora do switch para poder utiliza-la nas
                // alíneas seguintes.
                out.println("Vamos preencher a matriz das notas");
                for(i=0; i<5; i+=1) {
                    for (j=0; j < 5; j += 1) {
                        out.println("Aluno " + i);
                        out.println("Uc " + j);
                        out.print("Nota: ");
                        int nota = scan.nextInt();
                        turma.atualizarPauta(i, j, nota);
                    }
                }

                switch (alinea2){
                    case "b":
                        out.print("Indice da Uc: ");
                        int indiceUc = scan.nextInt();
                        int somaNotas = turma.somaNotas(indiceUc);
                        out.println("A soma das notas desta Uc e " + somaNotas);
                        break;

                    case "c":
                        out.print("Indice do aluno: ");
                        int indiceAluno = scan.nextInt();
                        float mediaNotasAluno = turma.mediaDoAluno(indiceAluno);
                        out.println("A media deste aluno e " + mediaNotasAluno);
                        break;

                    case "d":
                        out.print("Insira o indice da Uc: ");
                        int ucIndex = scan.nextInt();
                        float mediaNotasUc = turma.mediaDaUc(ucIndex);
                        out.println("A media desta uc e " + mediaNotasUc);
                        break;

                    case "e":
                        int notaMaisAlta = turma.notaMaisAlta();
                        out.println("A nota mais alta da turma e " + notaMaisAlta);
                        break;
                    case "f":
                        int notaMaisBaixa = turma.notaMaisBaixa();
                        out.println("A nota mais baixa da turma e " + notaMaisBaixa);
                        break;
                    case "g":
                        out.println("Insira um numero inteiro: ");
                        int valor = scan.nextInt();
                        turma.notasAcimaDe(valor);
                        break;
                    case "h":
                        out.println("Notas de todos os alunos do curso");
                        turma.notasDosAlunos();
                        break;
                    case "i":
                        out.println("Indice da Uc com maior media: " + turma.mediaUcMaisAlta());
                        break;
                    default:
                        out.println("Alinea inexistente");
                        break;
                }
                break;

            case 3:
                out.print("Tamanho do array das datas: ");
                int size = scan.nextInt();
                Datas datas = new Datas(size);
                out.print("Alinea: ");
                String alinea3 = scan.next();
                int d, m, a;

                switch (alinea3){
                    case "a":
                        System.out.print("Digite o dia: ");
                        d = scan.nextInt();
                        System.out.print("Digite o mes: ");
                        m = scan.nextInt();
                        System.out.print("Digite o ano: ");
                        a = scan.nextInt();
                        datas.insereData(LocalDate.of(a,m,d));
                        break;
                    case "b":
                        System.out.print("Digite o dia: ");
                        d = scan.nextInt();
                        System.out.print("Digite o mes: ");
                        m = scan.nextInt();
                        System.out.print("Digite o ano: ");
                        a = scan.nextInt();
                        LocalDate data = LocalDate.of(a,m,d);
                        out.print("A data mais proxima e" + datas.dataMaisProxima(data));
                        break;
                    case "c":
                        out.print(datas.toString());
                        break;
                    default:
                        out.println("Alinea inexistente");
                        break;
                }
            case 6:
                //iniciei localmente as matrizes porque o exercício apenas fala em métodos
                Matrizes matrizes = new Matrizes();
                int numLinhas = 3;
                int numColunas = 3;
                int[][] matriz1 = {{1,2,3},
                                   {4,5,6},
                                   {7,8,9}};

                int[][] matriz2 = {{10,20,30},
                                  {40,50,60},
                                  {70,80,90}};
                int[][] result = new int[numLinhas][numColunas];


                out.println("Alinea: ");
                String alinea6 = scan.next();
                switch (alinea6){
                    case "a":
                        matrizes.lerMatriz(matriz1, numLinhas, numColunas);
                        matrizes.lerMatriz(matriz2, numLinhas, numColunas);
                        break;
                    case "b":
                        matrizes.somaMatrizes(matriz1, matriz2, result, numLinhas, numColunas);
                        break;
                    case "c":
                        matrizes.saoIguais(matriz1, matriz2, numLinhas, numColunas);
                        break;
                    case "d":
                        matrizes.matrizOposta(matriz1, result, numLinhas, numColunas);
                        matrizes.matrizOposta(matriz2, result, numLinhas, numColunas);
                        break;
                    default:
                        out.print("Alinea inexistente");
                        break;
                }
            case 7:
                out.println("Let's gamble!!!!!");
                Euromilhoes euromilhoes = new Euromilhoes(5,2);
                euromilhoes.gerarChave();
                int[] numerosUser = new int[5];
                int[] estrelasUser = new int[2];


                // pedir os números ao utilizador
                out.println("Insira numeros entre 1 e 50");
                for(i=0; i<5; i+=1){
                    out.print("Numero " + (i+1) + ": ");
                    int num = scan.nextInt();
                    numerosUser[i] = num;
                }

                // pedir as chaves ao utilizador
                out.println("Insira estrelas entre 1 e 9");
                for(i=0; i<2; i+=1){
                    out.print("Estrela " + (i+1) + ": ");
                    int estrela = scan.nextInt();
                    estrelasUser[i] = estrela;
                }

                euromilhoes.imprimeChave();
                euromilhoes.comparaAposta(numerosUser, estrelasUser);
        }

    }

}
