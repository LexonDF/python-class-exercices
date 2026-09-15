/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.clases.js;

public class ClasesJs {

    public static void main(String[] args) {
        Piloto marc = new Piloto("Marc Marquez", "A2-99887", 15);

        Motocicleta honda = new Motocicleta("Honda", "RC213V", 1000);
        honda.asignarPiloto(marc);
        honda.mostrarInfo();

        honda.quitarPiloto();
        System.out.println(marc.presentarse());

        Motocicleta yamaha = new Motocicleta("Yamaha", "YZF-R1", 998);
        yamaha.asignarPiloto(marc);
        yamaha.mostrarInfo();
    }
}