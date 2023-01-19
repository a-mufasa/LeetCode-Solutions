class Solution {
    public int findCircleNum(int[][] isConnected) {
        int provCount = 0;
        int n = isConnected.length;
        boolean[] checked = new boolean[n];
        for(int i =0; i<n; i++){
           if (checked[i] == false){
               checked[i] = true;
               provCount++;
               search(isConnected, checked, i);
           }
        }
        return provCount;
    }
    
    private void search(int[][] isConnected, boolean[] checked, int i){
        int n = isConnected.length;
        for(int j = 0; j< n; j++){
            if (checked[j]==false && isConnected[i][j]==1){
                checked[j] = true;
                search(isConnected, checked, j);
            }
        }
    }
}
