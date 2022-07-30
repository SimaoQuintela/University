import java.util.ArrayList;
import java.util.Scanner;
import java.util.Iterator;
import java.util.stream.Stream;
import static java.lang.System.out;

public class Ficha4 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        out.print("Ex: ");
        int ex = scan.nextInt();

        switch(ex){
            case 1:
                ArrayList<String> stack = new ArrayList<String>();
                Stack s = new Stack(stack);
                s.pop();
                s.push("Chandler");
                s.push("Monica");
                s.pop();
                s.push("Joey");
                s.top();
                out.println("Está vazia: " + s.empty());
                out.println(("Size: " + s.length()));

                out.println(s.toString());

        }

    }
}
