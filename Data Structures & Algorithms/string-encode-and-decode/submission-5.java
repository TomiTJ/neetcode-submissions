class Solution {

    public String encode(List<String> strs) {
        ArrayList<String> output = new ArrayList<>();
        for (int i = 0 ; i < strs.size() ; i++){
            output.add(String.valueOf(strs.get(i).length()) + "#" + strs.get(i));
        }

        return String.join("",output); 

    }

    public List<String> decode(String str) {
        ArrayList<String> output = new ArrayList<>();
        int i = 0 ;  
        while (i < str.length()){
            
            int hash_pos = str.indexOf('#',i);
            int value_pos = Integer.parseInt(str.substring(i,hash_pos));



             output.add(str.substring(hash_pos + 1, hash_pos + 1 + value_pos)); 

            i = hash_pos + 1 + value_pos ;


        }

        return output; 





    }
}
