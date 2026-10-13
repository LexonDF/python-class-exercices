import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("--- Registro de Estudiante ---");
        System.out.print("Nombre: ");
        String nomEst = scanner.nextLine();
        System.out.print("Edad: ");
        int edadEst = scanner.nextInt();
        scanner.nextLine(); // Limpiar buffer
        System.out.print("Documento: ");
        String docEst = scanner.nextLine();
        System.out.print("Programa: ");
        String progEst = scanner.nextLine();
        System.out.print("Promedio: ");
        double promEst = scanner.nextDouble();
        scanner.nextLine(); // Limpiar buffer

        Estudiante estudiante = new Estudiante(nomEst, edadEst, docEst, progEst, promEst);

        System.out.println("\n--- Registro de Profesor ---");
        System.out.print("Nombre: ");
        String nomProf = scanner.nextLine();
        System.out.print("Edad: ");
        int edadProf = scanner.nextInt();
        scanner.nextLine(); // Limpiar buffer
        System.out.print("Documento: ");
        String docProf = scanner.nextLine();
        System.out.print("Área: ");
        String areaProf = scanner.nextLine();
        System.out.print("Salario Base: ");
        double salBase = scanner.nextDouble();
        System.out.print("Horas Cátedra: ");
        int horasCat = scanner.nextInt();

        Profesor profesor = new Profesor(nomProf, edadProf, docProf, areaProf, salBase, horasCat);

        System.out.println("\n========================================");
        System.out.println("INFORMACIÓN DEL ESTUDIANTE (Rol: " + estudiante.getRol() + ")");
        System.out.println("========================================");
        estudiante.mostrarInfo();

        System.out.println("\n========================================");
        System.out.println("INFORMACIÓN DEL PROFESOR (Rol: " + profesor.getRol() + ")");
        System.out.println("========================================");
        profesor.mostrarInfo();

        scanner.close();
    }
}