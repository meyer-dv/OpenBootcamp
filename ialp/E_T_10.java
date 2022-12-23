public class E_T_10 {
    public static void main(String[] args) {
        System.out.println(factorial(4));
    }

    public static int factorial(int numero) {
        int resultado;
        if (numero == 1) {
            System.out.println(numero);
            return 1;
        }
        
        resultado = factorial(numero - 1) * numero;
        System.out.println(numero);

        return resultado;
    }
}
