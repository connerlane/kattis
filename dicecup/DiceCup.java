/**
 * Created by connerlane on 2/1/17.
 */
import java.util.*;
public class DiceCup {

    public static void main(String args[]) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        Scanner scan = new Scanner(System.in);
        int dice1 = Integer.parseInt(scan.next());
        int dice2 = Integer.parseInt(scan.next());
        int[][] board = new int[dice1][dice2];
        for (int i = 0; i < dice1; i++) {
            for (int j = 0; j < dice2; j++) {
                int k = i + j + 2;
                board[i][j] = k;
                map.put(k, 0);
            }
        }

        for (int i = 0; i < dice1; i++) {
            for (int j = 0; j < dice2; j++) {
                int k = i + j + 2;
                int curval = map.get(k);
                map.put(k, (curval+1));
            }
        }
        int highest = 0;
        TreeSet<Integer> winList = new TreeSet<Integer>();
        for (int i = 0; i < dice1; i++) {
            for (int j = 0; j < dice2; j++) {
                int k = i + j + 2;
                int curval = map.get(k);
                if (curval > highest) {
                    winList.clear();
                    highest = curval;

                }
                if (curval == highest) {
                    winList.add(k);
                }
            }
        }

        for (int i: winList) {
            System.out.println(i);
        }
    }

}