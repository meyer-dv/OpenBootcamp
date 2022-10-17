public class E_T_4 {
    public static void main(String[] args) {
        // if
        int numeroIf = 0;
        if (numeroIf < 0) {
            System.out.println("El número es negativo");
        } else if (numeroIf > 0) {
            System.out.println("El número es positivo");
        } else {
            System.out.println("El número es 0");
        }

        // while
        int numeroWhile = 3;
        while (numeroWhile < 3) {
            System.out.println(numeroWhile++);
        }

        // do while
        do {
            System.out.println(numeroWhile++);
        } while (numeroWhile < 3);

        // for
        for (int numeroFor = 0; numeroFor <= 3; numeroFor++) {
            System.out.println(numeroFor);
        }

        // switch
        String estacion = "Primavera";
        switch (estacion) {
            case "Verano":
                System.out.println("Es verano");
                break;
            case "Invierno":
                System.out.println("Es Invierno");
                break;
            case "Primavera":
                System.out.println("Es Primavera");
                break;
            case "Otoño":
                System.out.println("Es Otoño");
                break;
            default:
                System.out.println("No es una estación");
        }
    }
}
