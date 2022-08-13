package capDois;
//o pacote de classes java.util disponibilizou a classe Scanner, que implementa operações de entrada de dados pelo teclado.
import java.util.Scanner;

public class entradaDeDados {
    public static void main(String[] args) {

        try (//Instanciar e criar um objeto Scanner usando o dispositivo padrão de entrada (System.in)
        Scanner entrada = new Scanner(System.in)) {
            //Pede a digitação ao usuário
            System.out.println("Digite o seu salário:");
            float salario = entrada.nextFloat();

            // Exibe o salário digitado
            System.out.println("Salário = R$" + salario);
        }
        catch (Exception e) {
            System.out.print("Ocorreu um erro:" + e);
        }
    }
}

//Tive que fazer uma gambiarra para esse código funcionar

//Existem outras formas de usar o metodo next para outros tipos de dados, basta pesquisar.
