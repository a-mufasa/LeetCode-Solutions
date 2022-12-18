import java.util.*;

class LRUCache {
    Map<Integer, Integer> cache;
    public LRUCache(int capacity) {
        cache = new LinkedHashMap<>(capacity, 1, true){
            @Override
            public boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest){
                if (capacity+1 == size()){
                    return true;
                }
                else{
                    return false;
                }
            }
        };
    }
    
    public int get(int key) {
        Integer val = cache.get(key);
        if(val == null){
            return -1;
        }
        else{
            return val;
        }
    }
    
    public void put(int key, int value) { //size vs capacity
        cache.put(key, value);
    }
}