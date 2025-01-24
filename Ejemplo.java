package Hilo;

public class Ejemplo implements Runnable {
    private String threadName;

    public Ejemplo(String threadName) {
        this.threadName = threadName;
    }

    @Override
    public void run() {
        if ("MultiplesDe2".equals(threadName)) {
            for (int i = 1; i <= 20; i++) {
                System.out.println("Hilo: " + threadName + " - Múltiplo de 2: " + (i * 2));
            }
        }
        System.out.println("Termina hilo: " + threadName);
    }

    public static void main(String[] args) {
        Thread hilo1 = new Thread(new Ejemplo("Multiples de 2"));
        Thread hilo2 = new Thread(new Ejemplo("ComprobadorDeHilos"));

        hilo1.start();
        hilo2.start();

        System.out.println("Termina thread main");
    }
}

