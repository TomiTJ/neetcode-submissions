class Solution {
    public int[] twoSum(int[] numbers, int target) {

        HashMap<Integer,Integer> searched = new HashMap<>();

        for (int i = 0 ; i < numbers.length ; i++){
            int complement = target - numbers[i];
            if (searched.containsKey(complement)){
                return new int[]{searched.get(complement)+1,i+1};
            }
            searched.put(numbers[i],i);
        }

        return new int[]{};
        
    }
}
