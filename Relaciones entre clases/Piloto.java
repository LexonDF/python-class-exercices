/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.clases.js;

/**
 *
 * @author giova
 */
public class Piloto {
       private String nombre;
    private String licencia;
    private int experiencia;

    public Piloto(String nombre, String licencia, int experiencia) {
        this.nombre = nombre;
        this.licencia = licencia;
        this.experiencia = experiencia;
    }

    public String presentarse() {
        return nombre + " (Licencia: " + licencia + ") - " + experiencia + " anos de experiencia";
    }

    public String getNombre() {
        return nombre;
    }
}
