import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by RCR on 2017-04-19.
 */
public class Utils {

    // fonction qui verifie si le couple present est dans les list de couple deja trouve
    public static boolean isCoupleAlreadyThere(ArrayList<Integer[]> currentCouplesFound, Integer[] coupleATester) {
        Integer[] coupleATesterA = {coupleATester[0], coupleATester[1]};
        Integer[] coupleATesterB = {coupleATester[1], coupleATester[0]};
        for(Integer[] couple : currentCouplesFound) {
            if((Arrays.equals(couple, coupleATesterA)) || (Arrays.equals(couple, coupleATesterB))) {
                return true;
            }
        }
        return false;
    }
}
