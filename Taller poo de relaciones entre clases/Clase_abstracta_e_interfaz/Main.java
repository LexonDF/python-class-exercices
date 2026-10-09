package Clase_abstracta_e_interfaz;

public class Main {
    public static void main(String[] args) {
        Figura f1 = new Circulo("Rojo", 5);
        Figura f2 = new Rectangulo("Azul", 4, 3);
        System.out.println(f1.describir());
        System.out.println(f2.describir());

        Imprimible i = new Circulo("Verde", 2);
        i.imprimir();
    }
}
