package Dependencia;

public class Cajero {
    private String nombre;

    public Cajero(String nombre) {
        this.nombre = nombre;
    }

    public void cobrar(double monto) {
        Recibo recibo = new Recibo(monto);   // dependencia: variable local
        System.out.println(nombre + " entrega: " + recibo.generarTexto());
    }

    public void anular(Recibo recibo) {      // dependencia: parámetro
        System.out.println(nombre + " anula: " + recibo.generarTexto());
    }
}