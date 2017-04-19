import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

/**
 * Created by RCR on 2017-04-19.
 */
public class AlgoFindPaths {
    static Random random = new Random();
    static double bestTotalCostPath = Double.POSITIVE_INFINITY;

    public static void findMinPath(int nbreTotalNode, ArrayList<Integer> wowSpotsIndexPosition, ArrayList<Integer> entreesIndexPosition, ArrayList<Integer> etapesIndexPosition, int[] nbreMaximumEdgesAllow, int[] typesList, double[][] costMatrix, ArrayList<Integer> allNodes) {
        // Creation du graph
        Graph graph = new Graph(nbreTotalNode);
        // Cout trouve pour ce present path
        double currentCostPath = 0.0;
        // Couples trouve pour ce present path
        ArrayList<Integer[]> currentCouplesFound = new ArrayList<>();
        // Nombres de edges permit restant pour chaque node
        int[] nbreEdgesPermisRestants = Arrays.copyOf(nbreMaximumEdgesAllow, nbreMaximumEdgesAllow.length);
        // Random number qui sera utiliser dans toutes les fonctions
        int randomNumber = 0;
        // Nombre de tour de boucle que devra faire le loop avant d'avoir lie chq node
        int nbreTourDeLoop = typesList.length;
        // Nodes restant a lier aux autres
        ArrayList<Integer> nodeRestantALier = new ArrayList(allNodes);

        // couple A & B de test pour les case plus bas
        Integer[] coupleTest = new Integer[2];
        // List test pour les cases plus bas pour eliminer les node fini de liaison
        ArrayList<Integer> testList = new ArrayList<>();


        // Loop lie tous les nodes ensemble... il ne sortira pas du loop tant qu'il reste des nombres
        loop: while(nbreTourDeLoop > 0) {

            int randomNodeIndex = random.nextInt(nbreTourDeLoop);

            switch(typesList[(nodeRestantALier.get(randomNodeIndex))]) {
                // Case ou c'est les wowSpots
                case 1:
                    // Si le node ne peut deja plus faire de liens
                    if(nbreEdgesPermisRestants[randomNodeIndex] == 0) {
                        nodeRestantALier.remove(Integer.valueOf(randomNodeIndex));
                        nbreTourDeLoop--;
                        continue loop;
                    }

                    // gerer le cas ou les liens permit sont neg
                    randomNumber = random.nextInt(nbreTotalNode);
                    testList.clear();
                    while(nbreEdgesPermisRestants[randomNumber] <= 0) {
                        if(testList.size() == nbreTotalNode) {
                            nodeRestantALier.remove(Integer.valueOf(randomNodeIndex));
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
                        nodeRestantALier.remove(Integer.valueOf(randomNodeIndex));
                        nbreTourDeLoop--;
                        continue loop;
                    }
                    // Fin de ce case
                    break;

                // Case ou c'est les entrees
                case 2:
                    // Si le node ne peut deja plus faire de liens
                    if(nbreEdgesPermisRestants[randomNodeIndex] == 0) {
                        nodeRestantALier.remove(Integer.valueOf(randomNodeIndex));
                        nbreTourDeLoop--;
                        continue loop;
                    }

                    // Creer le couple test afin de tester des solutions possible
                    randomNumber = random.nextInt(nbreTotalNode);
                    coupleTest[0] = randomNodeIndex;
                    coupleTest[1] = randomNumber;
                    // Clear la list test
                    testList.clear();
                    while(nbreEdgesPermisRestants[randomNumber] <= 0 || Utils.isCoupleAlreadyThere(currentCouplesFound, coupleTest)) {
                        if(testList.size() == nbreTotalNode) {
                            nodeRestantALier.remove(Integer.valueOf(randomNodeIndex));
                            nbreTourDeLoop--;
                            continue loop;
                        }
                        else {
                            randomNumber = random.nextInt(nbreTotalNode);
                            if(!testList.contains(randomNumber)) {
                                testList.add(randomNumber);
                            }
                            // Reajuster en fonction du new random
                            coupleTest[0] = randomNodeIndex;
                            coupleTest[1] = randomNumber;


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
                        nodeRestantALier.remove(Integer.valueOf(randomNodeIndex));
                        nbreTourDeLoop--;
                        continue loop;
                    }
                    // Fin de ce case
                    break;
                case 3:
                    // Si le node ne peut deja plus faire de liens
                    if(nbreEdgesPermisRestants[randomNodeIndex] == 0) {
                        nodeRestantALier.remove(Integer.valueOf(randomNodeIndex));
                        nbreTourDeLoop--;
                        continue loop;
                    }

                    // Creer le couple test afin de tester des solutions possible
                    randomNumber = random.nextInt(nbreTotalNode);
                    coupleTest[0] = randomNodeIndex;
                    coupleTest[1] = randomNumber;
                    // Clear la list test
                    testList.clear();
                    while(nbreEdgesPermisRestants[randomNumber] <= 0 || Utils.isCoupleAlreadyThere(currentCouplesFound, coupleTest)) {
                        if(testList.size() == nbreTotalNode) {
                            nodeRestantALier.remove(Integer.valueOf(randomNodeIndex));
                            nbreTourDeLoop--;
                            continue loop;
                        }
                        else {
                            randomNumber = random.nextInt(nbreTotalNode);
                            if(!testList.contains(randomNumber)) {
                                testList.add(randomNumber);
                            }
                            // Reajuster en fonction du new random
                            coupleTest[0] = randomNodeIndex;
                            coupleTest[1] = randomNumber;


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
                        nodeRestantALier.remove(Integer.valueOf(randomNodeIndex));
                        nbreTourDeLoop--;
                        continue loop;
                    }
                    // Fin de ce case
                    break;
                default:
                    break;
            }
        }

        // Make sure toutes les etapes ont au moins 2 edges reliees a eux
        boolean isEtapesEdgesMinAtteint = isEtapesEdgesMinAtteintFct(etapesIndexPosition, nbreMaximumEdgesAllow, nbreEdgesPermisRestants);

        // Verifier que chaque etape est ratachee a une entree
        boolean isEtapesReachEntree = isEtapesReachEntreeFct(etapesIndexPosition, entreesIndexPosition, graph);


        // Verifier que chaque etape est ratachee a une entree
        boolean isWowSpotReachEntree =  isWowSpotReachEntreeFct(wowSpotsIndexPosition, entreesIndexPosition, graph);

        // Verifier que chaque node est present dans le current path
        boolean isAllNodeInMinPath = isAllNodeInMinPathFct(allNodes, currentCouplesFound);

        //Si notre resultat est valide et meilleur on le garde
        if(currentCostPath < bestTotalCostPath && isEtapesReachEntree && isWowSpotReachEntree && isEtapesEdgesMinAtteint && isAllNodeInMinPath){
            bestTotalCostPath = currentCostPath;
            // Print le meilleur path trouve
            printPath(currentCouplesFound);

//            final long tempsCalcul = System.nanoTime() - startTime;

//            if(printTime  == true){
//                System.out.println("");
//                System.out.println("Temps de Calcul (Nanosecondes) : " + tempsCalcul);
//            }
        }
        return;
    }

    static boolean isAllNodeInMinPathFct(ArrayList<Integer> allNodes, ArrayList<Integer[]> currentCouplesFound) {
        boolean isAllNodeInMinPath = false;
        ArrayList<Integer> allNodesForVerif = new ArrayList<>();
        ArrayList<Integer> allNodeInParc = new ArrayList(allNodes);
        for(Integer[] couple : currentCouplesFound) {
            if(!allNodesForVerif.contains(couple[0])) {
                allNodesForVerif.add(couple[0]);
            }
            if(!allNodesForVerif.contains(couple[1])) {
                allNodesForVerif.add(couple[1]);
            }
        }
        for(Integer node : allNodeInParc) {
            if(!allNodesForVerif.contains(node)) {
                isAllNodeInMinPath = false;
                break;
            }
            isAllNodeInMinPath = true;
        }
        return isAllNodeInMinPath;
    }

    static boolean isEtapesEdgesMinAtteintFct(ArrayList<Integer> etapesIndexPosition, int[] nbreMaximumEdgesAllow, int[] nbreEdgesPermisRestants) {
        boolean isEtapesEdgesMinAtteint = false;
        for(Integer etape : etapesIndexPosition ) {
            if(nbreMaximumEdgesAllow[etape] - nbreEdgesPermisRestants[etape] < 2) {
                isEtapesEdgesMinAtteint = false;
                break;
            }
            isEtapesEdgesMinAtteint = true;
        }
        return isEtapesEdgesMinAtteint;
    }

    static boolean isEtapesReachEntreeFct(ArrayList<Integer> etapesIndexPosition, ArrayList<Integer> entreesIndexPosition, Graph graph) {
        boolean isEtapesReachEntree = false;
        for(Integer etape : etapesIndexPosition ) {
            for (Integer entree : entreesIndexPosition) {
                if (graph.isReachable(entree, etape)) {
                    isEtapesReachEntree = true;
                    break;
                }
            }
            if(!isEtapesReachEntree) {
                break;
            }
        }
        return isEtapesReachEntree;
    }

    static boolean isWowSpotReachEntreeFct(ArrayList<Integer> wowSpotsIndexPosition, ArrayList<Integer> entreesIndexPosition, Graph graph) {
        boolean isWowSpotReachEntree = false;
        for(Integer wowSpot : wowSpotsIndexPosition ) {
            for (Integer entree : entreesIndexPosition) {
                if (graph.isReachable(entree, wowSpot)) {
                    isWowSpotReachEntree = true;
                    break;
                }
            }
            if(!isWowSpotReachEntree) {
                break;
            }
        }
        return isWowSpotReachEntree;
    }


    static void printPath(ArrayList<Integer[]> currentCouplesFound) {
        System.out.println("-----------------------------------------------");
        for(int i = 0; i < currentCouplesFound.size(); i++){
            System.out.println(currentCouplesFound.get(i)[0] + " " + currentCouplesFound.get(i)[1]);
        }
        System.out.println("Fin");
        System.out.println("Meilleur Cout trouve: " + bestTotalCostPath);
    }
}
