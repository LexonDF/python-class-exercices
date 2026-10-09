package Interface;

public class TarjetaCredito implements MedioDePago {
    private double cupoDisponible;

    public TarjetaCredito(double cupoDisponible) {
        this.cupoDisponible = cupoDisponible;
    }

    @Override
    public boolean pagar(double monto) {
        if (monto <= cupoDisponible) {
            cupoDisponible -= monto;
            return true;
        }
        return false;
    }
}
