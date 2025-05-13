import java.util.*;
class Solution {
    public int solution(int[] players, int m, int k) {
        int [] servers = new int[players.length];
        int serverCnt = 0;
        for (int ser: servers){
            System.out.println(ser);
        }
        for (int i = 0; i < players.length; i++) {
            int need = players[i] / m; 
            int curServer = 0;
            
            for (int j = i; j >= Math.max(i-k+1, 0); j--) {
                curServer += servers[j];
                // System.out.println(j+"번째 서버: "+servers[j]);
            }
            // System.out.println("필요한 서버수: "+need+" curServer: "+curServer);
            if (curServer < need) {
                int toAdd = need - curServer;
                // System.out.println("toAdd"+toAdd);
                servers[i] = toAdd;
                serverCnt += toAdd;
            }
        }
        return serverCnt;
    }
}