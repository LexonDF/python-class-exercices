package Dependencia;

public class Recibo {
    private double valor;

    public Recibo(double valor) {
        this.valor = valor;
    }

    public String generarTexto() {
        return "Recibo por $" + valor;
    }
}
