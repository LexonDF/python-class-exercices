package Asociacion_muchos_a_muchos;

import java.util.ArrayList;
import java.util.List;

public class Estudiante {
    private String nombre;
    private List<Curso> cursos = new ArrayList<>();

    public Estudiante(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public List<Curso> getCursos() {
        return cursos;
    }

    public void inscribir(Curso curso) {
        if (!cursos.contains(curso)) {
            cursos.add(curso);
            curso.agregarEstudiante(this);
        }
    }
}
