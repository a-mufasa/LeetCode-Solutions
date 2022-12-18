class Solution {
    public boolean isRobotBounded(String instructions) {
        char arr[] = instructions.toCharArray();
        int x = 0, y = 0; //origin
        int xDir = 0, yDir = 1; //North
        boolean stuck = false;
        for (char input : arr){
            if (input == 'G'){
                x += xDir;
                y += yDir;
            }
            else if (input == 'L'){
                if (yDir != 0){
                    xDir = yDir*-1;
                    yDir = 0;
                }
                else if (xDir != 0){
                    yDir = xDir;
                    xDir = 0;
                }
            }
            else{
                if (yDir != 0){
                    xDir = yDir;
                    yDir = 0;
                }
                else if (xDir != 0){
                    yDir = xDir*-1;
                    xDir = 0;
                }
            }
        }
        if (x == 0 && y == 0){
            stuck = true;
        }
        else if (yDir != 1){
            stuck = true;
        }
        return stuck;
    }
}