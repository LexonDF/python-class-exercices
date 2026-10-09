package Herencia;

public class Motocicleta extends Vehiculo {
    private int cilindraje;

    public Motocicleta(String placa, String marca, int cilindraje) {
        super(placa, marca);
        this.cilindraje = cilindraje;
    }

    @Override
    public String describir() {
        return super.describir() + " - Motocicleta de " + cilindraje + " cc";
    }
}
