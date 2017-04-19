import jdk.internal.cmm.SystemResourcePressureImpl;

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

    public static void main(String[] args) throws FileNotFoundException {
        int nbreTotalNode = 0;
        Scanner scan = new Scanner((new File("data/Parc1-10Zones.txt")));

        // Get le nombre de points sur la map
        if (scan.hasNext()) {
            nbreTotalNode = Integer.parseInt(scan.next());
        }

        // Determiner les index pour chaque type de points selon le data
        ArrayList<Integer> wowSpotsIndexPosition = new ArrayList<Integer>();
        ArrayList<Integer> entreesIndexPosition = new ArrayList<Integer>();
        ArrayList<Integer> etapesIndexPosition = new ArrayList<Integer>();
        int[] typesList = new int[nbreTotalNode];
        ArrayList<Integer> allNodes = new ArrayList<Integer>();

        int indexPositionType = 0;
        // Remplir les array de positions selon la list data
        for (int index = 0; index < nbreTotalNode; index++) {
            if (scan.hasNext()) {
                indexPositionType = Integer.parseInt(scan.next());
                typesList[index] = (indexPositionType);
                allNodes.add(index);
                switch (indexPositionType) {
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
        int[] nbreMaximumEdgesAllow = new int[nbreTotalNode];
        for (int i = 0; i < nbreTotalNode; i++) {
            if (scan.hasNext()) {
                nbreMaximumEdgesAllow[i] = Integer.parseInt(scan.next());
            }
        }

        // Get les cout des edges entre chq points
        double[][] costMatrix = new double[nbreTotalNode][nbreTotalNode];
        for (int i = 0; i < nbreTotalNode; i++) {
            for (int j = 0; j < nbreTotalNode; j++) {
                if (scan.hasNext()) {
                    costMatrix[i][j] = Double.parseDouble(scan.next());
                    // Remplacer les 0 par des 999 de distance
                    if (costMatrix[i][j] == 0) {
                        costMatrix[i][j] = 999.00;
                    }
                }
            }
        }

        scan.close();

        // Rouler l'algo qui trouve en continue le meilleur chemin
        while (true) {
            AlgoFindPaths.findMinPath(nbreTotalNode, wowSpotsIndexPosition, entreesIndexPosition, etapesIndexPosition, nbreMaximumEdgesAllow, typesList, costMatrix, allNodes);
        }
    }
}
