package Interface;

public class Efectivo implements MedioDePago {
    @Override
    public boolean pagar(double monto) {
        return monto > 0;
    }
}
