import java.time.LocalDateTime;
import static java.lang.System.out;

public class Ficha1 {
    // 1
    public double celsiusParaFarenheit(double graus) {
        return ((graus * 9 / 5) + 32);
    }

    // 2
    public int maximoNumeros(int a, int b) {
        return (Math.max(a, b));
    }

    // 3
    public String criaDescricaoConta(String nome, double saldo) {
        return ("Nome: " + nome + "Saldo: " + saldo);
    }

    // 4
    public double eurosParaLibras(double valor, double taxaConversao) {
        return (valor * taxaConversao);
    }

    // 5 feito no main

    // 6
    public long factorial(int num) {
        if (num == 1) {
            return 1;
        } else {
            return (num * factorial(num - 1));
        }
    }

    // 7
    public long tempoGasto() {
        long before = System.nanoTime();
        out.println(factorial(500));
        long after = System.nanoTime();

        return (after - before) / 1000000;
    }

}
