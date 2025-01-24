package Clase_Miercoles;

public class ComparacionDemo {
	public static void main(String[] args) {
		int resultado1 = Integer.compare(10, 20);
		System.out.println("Integer: " + resultado1);
		int resultado2 = Long.compare(100L, 50L);
		System.out.println("Long: " + resultado2);
		int resultado3 = Double.compare(3.14, 2.71);
		System.out.println("Double: " + resultado3);
		int resultado4 = Character.compare('A', 'Z');
		System.out.println("Character: " + resultado4);
		int resultado5 = Boolean.compare(true, false);
		System.out.println("Boolean: " + resultado5);
		}
}