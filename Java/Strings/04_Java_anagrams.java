    static boolean isAnagram(String a, String b) {
        // Complete the function
        int l = a.length();
        int aocc[] = new int[l]; 
        if (l != b.length())
            return(false);
        char tempArray1[] = a.toUpperCase().toCharArray();
        char tempArray2[] = b.toUpperCase().toCharArray();
        Arrays.sort(tempArray1);
        Arrays.sort(tempArray2);
        for (int i = 0; i < l; i++)
        {
            if (tempArray1[i] != tempArray2[i])
                return(false);
        }
        return(true);
    }
