package Clase_abstracta_e_interfaz;

public class Circulo extends Figura implements Imprimible {
    private double radio;

    public Circulo(String color, double radio) {
        super(color);
        this.radio = radio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * radio * radio;
    }

    @Override
    public void imprimir() {
        System.out.println(describir());
    }
}
