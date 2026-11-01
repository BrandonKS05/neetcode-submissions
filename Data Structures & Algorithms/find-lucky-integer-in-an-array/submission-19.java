class Solution {
    public int findLucky(int[] arr) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        ArrayList<Integer> res = new ArrayList<>();
        for(int num: arr){
            seen.put(num, seen.getOrDefault(num, 0) + 1);
        }
        for(Map.Entry<Integer, Integer> entry : seen.entrySet()){
            int key = entry.getKey();
            int val = entry.getValue();

            if (key == val){
                res.add(key);
            }
        }
      
        return (res.isEmpty()) ? -1 : Collections.max(res);

        
    }
}