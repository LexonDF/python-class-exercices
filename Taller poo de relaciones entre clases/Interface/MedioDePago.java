package Interface;

public interface MedioDePago {
    boolean pagar(double monto);

    default String nombre() {
        return getClass().getSimpleName();
    }
}
