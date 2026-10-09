package Herencia;

public class Automovil extends Vehiculo {
    private int numeroPuertas;

    public Automovil(String placa, String marca, int numeroPuertas) {
        super(placa, marca);
        this.numeroPuertas = numeroPuertas;
    }

    @Override
    public String describir() {
        return super.describir() + " - Automóvil de " + numeroPuertas + " puertas";
    }
}