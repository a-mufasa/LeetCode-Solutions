var isPalindrome = function(head) {
    arr = [];
    
    while (head !== null){
        arr.push(head.val);
        head = head.next;
    }
    
    arrReverse = [...arr].reverse();
    
    bool = true;
        
    for (i = 0; i<arr.length; i++){
        if (arr[i] !== arrReverse[i]){
            bool = false;
        }
    }
    
    return bool;
};