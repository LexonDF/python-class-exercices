package Dependencia;

public class Main {
    public static void main(String[] args) {
        Cajero cajero = new Cajero("Laura");
        cajero.cobrar(25000);
        cajero.anular(new Recibo(25000));
    }
}
