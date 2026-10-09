package Herencia;

public class Main {
    public static void main(String[] args) {
        Vehiculo[] flota = {
            new Automovil("ABC123", "Mazda", 4),
            new Motocicleta("XYZ98D", "Yamaha", 250),
            new Camion("SUV456", "Chevrolet", 8.5)
        };
        for (Vehiculo v : flota) {
            v.acelerar(40);
            System.out.println(v.describir());
        }
    }
}
