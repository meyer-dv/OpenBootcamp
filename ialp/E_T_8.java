/* Para practicar la encapsulación:

- Crear clase Persona.

- Crear variables las privadas edad, nombre y telefono de la clase Persona.

- Crear gets y sets de cada propiedad.

- Crear un objeto persona en el main.

- Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola. */

public class E_T_8 {
    public static void main(String[] args) {
        Persona estudiante = new Persona();
        estudiante.setEdad(17);
        estudiante.setNombre("Meyer");
        estudiante.setTelefono(314592333);

        System.out.println("Edad del estudiante: " + estudiante.getEdad());
        System.out.println("Nombre del estudiante: " + estudiante.getNombre());
        System.out.println("Telefono del estudiante: " + estudiante.getTelefono());
    }
}

class Persona {
    private int edad;
    private String nombre;
    private int telefono;

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getTelefono() {
        return this.telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }
}
