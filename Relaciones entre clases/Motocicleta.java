/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.clases.js;

/**
 *
 * @author giova
 */
public class Motocicleta {
    private String marca;
    private String modelo;
    private int cilindraje;
    private Piloto piloto; // referencia, no crea al piloto internamente

    public Motocicleta(String marca, String modelo, int cilindraje) {
        this.marca = marca;
        this.modelo = modelo;
        this.cilindraje = cilindraje;
        this.piloto = null;
    }

    public void asignarPiloto(Piloto piloto) {
        this.piloto = piloto;
    }

    public void quitarPiloto() {
        this.piloto = null;
    }

    public void mostrarInfo() {
        System.out.println(marca + " " + modelo + " (" + cilindraje + "cc)");
        if (piloto != null) {
            System.out.println("Piloto actual: " + piloto.presentarse());
        } else {
            System.out.println("Sin piloto asignado");
        }
    }
}
