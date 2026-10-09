package Interface;

public class Nequi implements MedioDePago {
    private double saldo;

    public Nequi(double saldo) {
        this.saldo = saldo;
    }

    @Override
    public boolean pagar(double monto) {
        if (monto <= saldo) {
            saldo -= monto;
            return true;
        }
        return false;
    }
}
