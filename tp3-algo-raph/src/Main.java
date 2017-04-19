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
    static Random random = new Random();
    static double bestTotalCostPath = Double.POSITIVE_INFINITY;


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
        ArrayList<Integer> typesList = new ArrayList<Integer>();

        int indexPositionType = 0;
        // Remplir les array de positions selon la list data
        for (int index = 0; index < nbreTotalNode; index++) {
            if (scan.hasNext()) {
                indexPositionType = Integer.parseInt(scan.next());
                typesList.add(indexPositionType);
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

        while (true) {
            findMinPath(nbreTotalNode, wowSpotsIndexPosition, entreesIndexPosition, etapesIndexPosition, nbreMaximumEdgesAllow, typesList, costMatrix);
        }
    }
    public static void findMinPath(int nbreTotalNode, ArrayList<Integer> wowSpotsIndexPosition, ArrayList<Integer> entreesIndexPosition, ArrayList<Integer> etapesIndexPosition, int[] nbreMaximumEdgesAllow, ArrayList<Integer> typesList, double[][] costMatrix) {

        // Creation du graph
        Graph graph = new Graph(nbreTotalNode);
        // Cout trouve pour ce present path
        double currentCostPath = 0.0;
        // Couples trouve pour ce present path
        ArrayList<Integer[]> currentCouplesFound = new ArrayList<Integer[]>();
        // Nombres de edges permit restant pour chaque node
        int[] nbreEdgesPermisRestants = nbreMaximumEdgesAllow.clone();
        // Random number qui sera utiliser dans toutes les fonctions
        int randomNumber = 0;
        // Nombre de tour de boucle que devra faire le loop avant d'avoir lie chq node
        int nbreTourDeLoop = typesList.size();
        // Nodes restant a lier aux autres
        ArrayList<Integer> nodeRestantALier = (ArrayList<Integer>) typesList.clone();
        // couple A & B de test pour les case plus bas
        Integer[] coupleTestA = new Integer[2];
        Integer[] coupleTestB = new Integer[2];
        // List test pour les cases plus bas pour eliminer les node fini de liaison
        ArrayList<Integer> testList = new ArrayList<>();


        // Loop lie tous les nodes ensemble... il ne sortira pas du loop tant qu'il reste des nombres
        loop: while(nbreTourDeLoop > 0) {
            int randomNodeIndex = random.nextInt(nbreTourDeLoop);

            switch(nodeRestantALier.get(randomNodeIndex)) {
                // Case ou c'est les wowSpots
                case 1:
                    // Si le node ne peut deja plus faire de liens
                    if(nbreEdgesPermisRestants[randomNodeIndex] == 0) {
                        nodeRestantALier.remove(randomNodeIndex);
                        nbreTourDeLoop--;
                        continue loop;
                    }

                    // gerer le cas ou les liens permit sont neg
                    randomNumber = random.nextInt(nbreTotalNode);
                    testList.clear();
                    while(nbreEdgesPermisRestants[randomNumber] <= 0) {
                        if(testList.size() == nbreTotalNode) {
                            nodeRestantALier.remove(randomNodeIndex);
                            nbreTourDeLoop--;
                            continue loop;
                        }
                        else {
                            randomNumber = random.nextInt(nbreTotalNode);
                            if(!testList.contains(randomNumber)) {
                                testList.add(randomNumber);
                            }
                        }
                    }

                    // verifier que le currentcost nest pas plus que le meilleure total trouve
                    if(currentCostPath + costMatrix[randomNodeIndex][randomNumber] > bestTotalCostPath) {
                        // si oui on abandonne la creation de liens
                        return;
                    }
                    else {
                        currentCostPath += costMatrix[randomNodeIndex][randomNumber];
                        // Reduire nbre edges permit pour le couple trouve
                        nbreEdgesPermisRestants[randomNodeIndex] -= 1;
                        nbreEdgesPermisRestants[randomNumber] -= 1;
                        // ajouter ce couple aux couples trouves
                        Integer[] coupleTrouve = {randomNodeIndex, randomNumber};
                        currentCouplesFound.add(coupleTrouve);

                        // Ajouter ce couple au graph
                        graph.addEdge(randomNodeIndex, randomNumber);
                        graph.addEdge(randomNumber, randomNodeIndex);
                    }

                    // Eliminer les node qui ne peuvent plus faire de liens
                    if(nbreEdgesPermisRestants[randomNodeIndex] == 0) {
                        nodeRestantALier.remove(randomNodeIndex);
                        nbreTourDeLoop--;
                    }
                    // Fin de ce case
                    break;

                // Case ou c'est les entrees
                case 2:
                    // Si le node ne peut deja plus faire de liens
                    if(nbreEdgesPermisRestants[randomNodeIndex] == 0) {
                        nodeRestantALier.remove(randomNodeIndex);
                        nbreTourDeLoop--;
                        continue loop;
                    }

                    randomNumber = random.nextInt(nbreTotalNode);
                    coupleTestA[0] = randomNodeIndex;
                    coupleTestA[1] = randomNumber;

                    coupleTestB[0] = randomNumber;
                    coupleTestB[1] = randomNodeIndex;

                    testList.clear();
                    while(nbreEdgesPermisRestants[randomNumber] <= 0 || Utils.isCoupleAlreadyThere(currentCouplesFound, coupleTestA) || Utils.isCoupleAlreadyThere(currentCouplesFound, coupleTestB)) {
                        if(testList.size() == nbreTotalNode) {
                            nodeRestantALier.remove(randomNodeIndex);
                            nbreTourDeLoop--;
                            continue loop;
                        }
                        else {
                            randomNumber = random.nextInt(nbreTotalNode);
                            if(!testList.contains(randomNumber)) {
                                testList.add(randomNumber);
                            }
                            // Reajuster en fonction du new random
                            coupleTestA[0] = randomNodeIndex;
                            coupleTestA[1] = randomNumber;

                            coupleTestB[0] = randomNumber;
                            coupleTestB[1] = randomNodeIndex;
                        }
                    }
                    // verifier que le currentcost nest pas plus que le meilleure total trouve
                    if(currentCostPath + costMatrix[randomNodeIndex][randomNumber] > bestTotalCostPath) {
                        // si oui on abandonne la creation de liens
                        return;
                    }
                    else {
                        currentCostPath += costMatrix[randomNodeIndex][randomNumber];
                        // Reduire nbre edges permit pour le couple trouve
                        nbreEdgesPermisRestants[randomNodeIndex] -= 1;
                        nbreEdgesPermisRestants[randomNumber] -= 1;
                        // ajouter ce couple aux couples trouves
                        Integer[] coupleTrouve = {randomNodeIndex, randomNumber};
                        currentCouplesFound.add(coupleTrouve);

                        // Ajouter ce couple au graph
                        graph.addEdge(randomNodeIndex, randomNumber);
                        graph.addEdge(randomNumber, randomNodeIndex);
                    }

                    // Eliminer les node qui ne peuvent plus faire de liens
                    if(nbreEdgesPermisRestants[randomNodeIndex] == 0) {
                        nodeRestantALier.remove(randomNodeIndex);
                        nbreTourDeLoop--;
                    }
                    // Fin de ce case
                    break;
                case 3:
                    // Si le node ne peut deja plus faire de liens
                    if(nbreEdgesPermisRestants[randomNodeIndex] == 0) {
                        nodeRestantALier.remove(randomNodeIndex);
                        nbreTourDeLoop--;
                        continue loop;
                    }

                    randomNumber = random.nextInt(nbreTotalNode);
                    coupleTestA[0] = randomNodeIndex;
                    coupleTestA[1] = randomNumber;

                    coupleTestB[0] = randomNumber;
                    coupleTestB[1] = randomNodeIndex;

                    testList.clear();
                    while(nbreEdgesPermisRestants[randomNumber] <= 0 || Utils.isCoupleAlreadyThere(currentCouplesFound, coupleTestA) || Utils.isCoupleAlreadyThere(currentCouplesFound, coupleTestB)) {
                        if(testList.size() == nbreTotalNode) {
                            nodeRestantALier.remove(randomNodeIndex);
                            nbreTourDeLoop--;
                            continue loop;
                        }
                        else {
                            randomNumber = random.nextInt(nbreTotalNode);
                            if(!testList.contains(randomNumber)) {
                                testList.add(randomNumber);
                            }
                            // Reajuster en fonction du new random
                            coupleTestA[0] = randomNodeIndex;
                            coupleTestA[1] = randomNumber;

                            coupleTestB[0] = randomNumber;
                            coupleTestB[1] = randomNodeIndex;
                        }
                    }
                    // verifier que le currentcost nest pas plus que le meilleure total trouve
                    if(currentCostPath + costMatrix[randomNodeIndex][randomNumber] > bestTotalCostPath) {
                        // si oui on abandonne la creation de liens
                        return;
                    }
                    else {
                        currentCostPath += costMatrix[randomNodeIndex][randomNumber];
                        // Reduire nbre edges permit pour le couple trouve
                        nbreEdgesPermisRestants[randomNodeIndex] -= 1;
                        nbreEdgesPermisRestants[randomNumber] -= 1;
                        // ajouter ce couple aux couples trouves
                        Integer[] coupleTrouve = {randomNodeIndex, randomNumber};
                        currentCouplesFound.add(coupleTrouve);

                        // Ajouter ce couple au graph
                        graph.addEdge(randomNodeIndex, randomNumber);
                        graph.addEdge(randomNumber, randomNodeIndex);
                    }

                    // Eliminer les node qui ne peuvent plus faire de liens
                    if(nbreEdgesPermisRestants[randomNodeIndex] == 0) {
                        nodeRestantALier.remove(randomNodeIndex);
                        nbreTourDeLoop--;
                    }
                    // Fin de ce case
                    break;
                default:
                    break;
            }




        }




        // TODO: Dont forget to close the scan ...








    }
}
