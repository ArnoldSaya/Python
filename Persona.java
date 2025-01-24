package Clase_Miercoles;

public class Persona implements Comparable<Persona> {
    private String nombre;
    private String apellido;
    private int edad;

    public Persona(String nombre ,String apellido, int edad) {
        this.nombre = nombre;
        this.edad = edad;
        this.apellido = apellido;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    @Override
    public int compareTo(Persona p) {
        int nombreComparacion = this.nombre.compareTo(p.nombre);
        if (nombreComparacion != 0) {
            return nombreComparacion; 
        }

        int apellidoComparacion = this.apellido.compareTo(p.apellido);
        if (apellidoComparacion != 0) {
            return apellidoComparacion; 
        }
        return Integer.compare(this.edad, p.edad); 
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Arnold","Sayas", 14);
        Persona persona2 = new Persona("Arnold","Sayas", 14);

        int comparacion = persona1.compareTo(persona2);
        if (comparacion == 0) {
            System.out.println("Ambas personas tienen el mismo nombre, apellido y edad.");
        } else if (comparacion > 0) {
            System.out.println(persona1.getNombre() + " " + persona1.getApellido() + " es mayor en el orden." + persona1.getEdad());
        } else {
            System.out.println(persona2.getNombre() + " " + persona2.getApellido() + " es mayor en el orden." + persona2.getEdad());
        }
    }
}
