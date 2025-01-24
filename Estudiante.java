package Clase_Miercoles;

import java.util.ArrayList;
import java.util.Collections;

public class Estudiante implements Comparable<Estudiante> {
    private String nombre;
    private int nota;
    private int edad;

    public Estudiante(String nombre, int nota, int edad) {
        this.nombre = nombre;
        this.nota = nota;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
    	this.nombre = nombre;
    }

    public int getNota() {
        return nota;
    }
    public void setNota(int nota) {
    	this.nota = nota;
    }

    public int getEdad() {
        return edad;
    }
    
    public void setEdad(int edad) {
    	this.edad = edad;
    }

    @Override
    public int compareTo(Estudiante e) {
        return this.nombre.compareTo(e.nombre);
    }

    @Override
    public String toString() {
        return "Estudiante" +
                "nombre='" + nombre +
                ", nota=" + nota +
                ", edad=" + edad;
    }

    public static void main(String[] args) {
        ArrayList<Estudiante> estudiantes = new ArrayList<>();
        estudiantes.add(new Estudiante("Alejando", 95, 44));
        estudiantes.add(new Estudiante("Ana", 95, 45));

        Collections.sort(estudiantes);
        System.out.println("Ordenados por nombre:");
        for (Estudiante estudiante : estudiantes) {
            System.out.println(estudiante);
        }
        Collections.sort(estudiantes, (e1, e2) -> Double.compare(e2.getNota(), e1.getNota()));
        System.out.println("\nOrdenados por nota:");
        for (Estudiante estudiante : estudiantes) {
            System.out.println(estudiante);
        }
        Collections.sort(estudiantes, (e1, e2) -> Integer.compare(e1.getEdad(), e2.getEdad()));
        System.out.println("\nOrdenados por edad:");
        for (Estudiante estudiante : estudiantes) {
            System.out.println(estudiante);
        }
    }
}
