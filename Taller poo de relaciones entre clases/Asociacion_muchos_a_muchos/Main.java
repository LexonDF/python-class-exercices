package Asociacion_muchos_a_muchos;

public class Main {
    public static void main(String[] args) {
        Estudiante e1 = new Estudiante("Diego");
        Estudiante e2 = new Estudiante("Laura");
        Curso c1 = new Curso("Cálculo");
        Curso c2 = new Curso("Teoría de la Computación");

        e1.inscribir(c1);
        e1.inscribir(c2);
        e2.inscribir(c1);

        for (Curso c : new Curso[]{c1, c2}) {
            System.out.println(c.getNombre() + ": "
                    + c.getEstudiantes().stream().map(Estudiante::getNombre).toList());
        }
        System.out.println("Diego cursa: "
                + e1.getCursos().stream().map(Curso::getNombre).toList());
    }
}
