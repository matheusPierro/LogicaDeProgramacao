package capDois;
//Representa todo momento em que o algoritmo precisa interagir com o usuario
public class saidaDeDados {//equacao
	public static void main(String[] args) {
		int i = 2;
        	double r = Math.sqrt(i);
        	System.out.print("A raiz de ");
        	System.out.print(i);
        	System.out.print(" é ");
        	System.out.print(r);
	   	System.out.println(".");
	   	i = 5;
	   	r = Math.sqrt(i);
	   	System.out.println("A raiz de " + i + " é " + r + ".");
    }
}