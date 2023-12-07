//Biblioteca de leitura de dados - interação - entrada
import java.util.Scanner;

public class SomarInteiros {
    public static void main(String[] args) throws Exception {
        
        try (Scanner entrada = new Scanner(System.in)) {

            int num1 = 0;
            int num2 = 0;
            int soma = 0;

            System.out.print("Insira um número: ");
            num1 = entrada.nextInt();

            System.out.print("Insira outro número: ");
            num2 = entrada.nextInt();

            soma = num1 + num2;

            System.out.printf("Soma é: %d%n", soma);

        }
    }
}
