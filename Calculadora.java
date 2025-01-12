import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha uma das opções abaixo: ");

        System.out.println(" + = Soma");

        System.out.println(" - = Subtração");

        System.out.println(" * = Multiplicação");

        System.out.println(" / = Divisão");
        char escolha = scanner.next().charAt(0);

        System.out.print("Digite um numero inteiro: ");
        double n1 = scanner.nextDouble();

        System.out.print("Digite outro: ");
        double n2 = scanner.nextDouble();

        switch (escolha) {
            case '+':
                System.out.println("Resultado: " + (n1 + n2));
                break;

            case '-':
                System.out.println("Resultado: " + (n1 - n2));
                break;

            case '*':
                System.out.println("Resultado: " + (n1 * n2));
                break;

            case '/':
                if (n2 !=0) {
                    System.out.println("Resultado: " + (n1 / n2));
                } else {
                    System.out.println("Erro, não é possivel dividir por zero.");
                }
                break;

            default:
                System.out.println("Operação invalida!");
        }

        scanner.close();

    }
}
