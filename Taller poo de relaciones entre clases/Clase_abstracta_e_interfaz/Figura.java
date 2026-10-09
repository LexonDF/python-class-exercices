package Clase_abstracta_e_interfaz;

import java.util.Locale;

public abstract class Figura {
    protected String color;

    public Figura(String color) {
        this.color = color;
    }

    // Método abstracto: no tiene cuerpo, las subclases deben implementarlo
    public abstract double calcularArea();

    // Método concreto: las subclases lo heredan tal cual
    public String describir() {
        return "Figura de color " + color + " con área "
                + String.format(Locale.US, "%.2f", calcularArea());
    }
}