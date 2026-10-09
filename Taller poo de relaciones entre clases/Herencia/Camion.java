package Herencia;

public class Camion extends Vehiculo {
    private double capacidadCarga;

    public Camion(String placa, String marca, double capacidadCarga) {
        super(placa, marca);
        this.capacidadCarga = capacidadCarga;
    }

    @Override
    public String describir() {
        return super.describir() + " - Camión con carga máxima de " + capacidadCarga + " t";
    }
}
