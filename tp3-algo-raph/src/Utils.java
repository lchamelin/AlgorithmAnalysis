import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by RCR on 2017-04-19.
 */
public class Utils {

    public static boolean isCoupleAlreadyThere(ArrayList<Integer[]> currentCouplesFound, Integer[] coupleATester) {
        for(Integer[] couple : currentCouplesFound) {
            if(Arrays.equals(couple, coupleATester)) {
                return true;
            }
        }
        return false;
    }
}
