public class Solution {
    public String longestCommonPrefix(String[] strs) {

        
        if(strs[0].equals("")){
            return "";
        }

        if(strs.length == 1){
            return strs[0];
        }


        char first = strs[0].charAt(0);
        String shared  = "" ;


        String min = strs[0];

        for (String st : strs){
            if (st.length() < min.length()){
                min = st;
            }
        }

        while (shared.length() <= min.length() -1){
            int end =  shared.length();
            
            shared = shared + strs[0].charAt(end);

            System.out.println(shared);
            for(String st : strs){
                
                String arg = st.substring(0,end +1);
                System.out.println(arg);

                if (arg.equals(shared)){
                    System.out.println(arg);
                }

                else{
                    return shared.substring(0,end);
                }

            }
           
        }

    return shared;
    }
    
} {
    
}
