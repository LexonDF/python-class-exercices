package Interface;

public class Main {
    public static void main(String[] args) {
        MedioDePago[] medios = {
            new TarjetaCredito(500000),
            new Nequi(20000),
            new Efectivo()
        };

        double total = 50000;
        for (MedioDePago m : medios) {
            String resultado = m.pagar(total) ? "aprobado" : "rechazado";
            System.out.println(m.nombre() + ": pago " + resultado);
        }
    }
}
