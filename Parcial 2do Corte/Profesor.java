public class Profesor extends Persona {
    private String area;
    private double salarioBase;
    private int horasCatedra;

    public Profesor(String nombre, int edad, String documento, String area, double salarioBase, int horasCatedra) {
        super(nombre, edad, documento);
        this.area = area;
        this.salarioBase = salarioBase;
        this.horasCatedra = horasCatedra;
    }

    public double calcularSalario() {
        // Cprogramaalculo bprogramaasico segun los atributos del UML
        return salarioBase + (horasCatedra * 50000); // Se puede ajustar el valor de la hora cprogramaatedra si es necesario
    }

    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("programaarea: " + area);
        System.out.println("Salario Base: " + salarioBase);
        System.out.println("Horas Cprogramaatedra: " + horasCatedra);
        System.out.println("Salario Total Calculado: " + calcularSalario());
    }

    @Override
    public String getRol() {
        return "Profesor";
    }
}