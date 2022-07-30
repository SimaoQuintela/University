import java.util.Scanner;
import static java.lang.System.out;

public class App {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        Ficha1 ficha1 = new Ficha1();
        out.print("Número do exercício: ");
        int ex = scan.nextInt();

        switch (ex) {
            case 1:
                out.print("Graus Celsius: ");
                double graus = scan.nextInt();
                double farenheit = ficha1.celsiusParaFarenheit(graus);
                out.print(graus + "graus celsius correspondem a " + farenheit + " graus Farenheit");
                break;
            case 2:
                out.print("Numero 1: ");
                int num1 = scan.nextInt();
                out.print("Numero 2: ");
                int num2 = scan.nextInt();
                int maximo = ficha1.maximoNumeros(num1, num2);
                out.print(maximo + " é o maior entre " + num1 + " e " + num2);
                break;
            case 3:
                out.print("Insira o nome: ");
                String nome = scan.next();
                out.print("Insira o saldo: ");
                double saldo = scan.nextDouble();
                ficha1.criaDescricaoConta(nome, saldo);
                break;
            case 4:
                out.print("Insira o valor em Libras: ");
                double valor = scan.nextDouble();
                out.print("Insira o valor da taxa de conversão: ");
                double taxaConversao = scan.nextDouble();
                double eurosParaLibras = ficha1.eurosParaLibras(valor, taxaConversao);
                out.print(valor + " euros é equivalente a " + eurosParaLibras + " libras");
                break;
            case 5:
                out.print("Insira um inteiro: ");
                int a = scan.nextInt();
                out.print("Insira um inteiro: ");
                int b = scan.nextInt();
                float media = (a + b) / 2;
                out.print(Math.max(a, b) + " " + Math.min(a, b) + " " + media);
                break;
            case 6:
                out.print("Insira um inteiro: ");
                int x = scan.nextInt();
                out.print("O fatorial de " + x + " é " + ficha1.factorial(x));
                break;
            case 7:
                ficha1.tempoGasto();
                break;
            default:
                out.print("Exercício não existente!");
        }

        scan.close();
    }
}
