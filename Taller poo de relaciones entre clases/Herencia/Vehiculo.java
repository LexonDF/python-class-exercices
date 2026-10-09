package Herencia;

public class Vehiculo {
    protected String placa;
    protected String marca;
    protected int velocidadActual;

    public Vehiculo(String placa, String marca) {
        this.placa = placa;
        this.marca = marca;
    }

    public void acelerar(int incremento) { velocidadActual += incremento; }
    public void frenar() { velocidadActual = 0; }

    public String describir() {
        return "Vehículo " + marca + " [" + placa + "] a " + velocidadActual + " km/h";
    }
}
