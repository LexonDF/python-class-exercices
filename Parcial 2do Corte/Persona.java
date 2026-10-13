public class Persona {
    protected String nombre;
    protected int edad;
    protected String documento;

    public Persona(String nombre, int edad, String documento) {
        this.nombre = nombre;
        this.edad = edad;
        this.documento = documento;
    }

    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Documento: " + documento);
    }

    public String getRol() {
        return "Persona";
    }
}