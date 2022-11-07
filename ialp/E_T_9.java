/* Crea una clase Persona con las siguientes variables:

- La edad

- El nombre

- El teléfono

Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.

Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.

Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador. */

public class E_T_9 {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.setEdad(17);
        cliente.setNombre("Kevin");
        cliente.setTelefono(314592);
        cliente.setCredito("¿Crédito?");

        Trabajador trabajador = new Trabajador();
        trabajador.setEdad(18);
        trabajador.setNombre("Mateo");
        trabajador.setTelefono(314592);
        trabajador.setSalario(300);

        System.out.println(
                "Cliente:\n" +
                        "\tEdad:" + cliente.getEdad() + "\n" +
                        "\tNombre:" + cliente.getNombre() + "\n" +
                        "\tTeléfono:" + cliente.getTelefono() + "\n" +
                        "\tCrédito:" + cliente.getCredito() + "\n\n" +
                "Trabajador:\n" +
                        "\tEdad:" + trabajador.getEdad() + "\n" +
                        "\tNombre:" + trabajador.getNombre() + "\n" +
                        "\tTeléfono:" + trabajador.getTelefono() + "\n" +
                        "\tSalario:" + trabajador.getSalario() + "\n");
    }
}

class Persona {
    private int edad;
    private String nombre;
    private int telefono;

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public int getTelefono() {
        return this.telefono;
    }
}

class Cliente extends Persona {
    private String credito;

    public void setCredito(String credito) {
        this.credito = credito;
    }

    public String getCredito() {
        return this.credito;
    }
}

class Trabajador extends Persona {
    private int salario;

    public void setSalario(int salario) {
        this.salario = salario;
    }

    public int getSalario() {
        return this.salario;
    }
}
