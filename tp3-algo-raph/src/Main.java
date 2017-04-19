import java.io.File;
import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Random;
import java.util.HashMap;
import java.io.*;
import java.util.*;
import java.util.LinkedList;

public class Main {
    static int nbrePoints = 0;


    public static void main(String[] args) throws FileNotFoundException {
	    Scanner scan = new Scanner((new File("data/Parc1-10Zones.txt")));

        // Get le nombre de points sur la map
        if(scan.hasNext()) {
            nbrePoints = Integer.parseInt(scan.next());
        }

        // Determiner les index pour chaque type de points selon le data
        ArrayList<Integer> wowSpotsIndexPosition = new ArrayList<Integer>();
        ArrayList<Integer> entreesIndexPosition = new ArrayList<Integer>();
        ArrayList<Integer> etapesIndexPosition = new ArrayList<Integer>();
        int indexPositionType = 0;
        // Remplir les array de positions selon la list data
        for(int index = 0; index < nbrePoints; index++) {
            if(scan.hasNext()) {
                indexPositionType = Integer.parseInt(scan.next());

                switch(indexPositionType) {
                    case 1:
                        wowSpotsIndexPosition.add(index);
                        break;
                    case 2:
                        entreesIndexPosition.add(index);
                        break;
                    case 3:
                        etapesIndexPosition.add(index);
                        break;
                    default:
                        break;
                }
            }
        }

        // Get le maximum d'edges accepte selon chaque point
        int[] nbreMaximumEdgesAllow = new int[nbrePoints];
        for(int i = 0; i < nbrePoints; i++) {
            if(scan.hasNext()) {
                nbreMaximumEdgesAllow[i] = Integer.parseInt(scan.next());
            }
        }

        // Get les cout des edges entre chq points
        double [][] costMatrix = new double[nbrePoints][nbrePoints];
        for(int i = 0; i < nbrePoints; i++) {
            for(int j = 0; j < nbrePoints; j++) {
                if(scan.hasNext()) {
                    costMatrix[i][j] = Double.parseDouble(scan.next());
                }
            }
        }

        System.out.println(nbrePoints);
        System.out.println(Arrays.deepToString(costMatrix));

        // TODO: Dont forget to close the scan ...








    }
}
