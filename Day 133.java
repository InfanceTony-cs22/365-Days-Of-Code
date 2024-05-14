public class Solution {
    public int permuteStrings(String A, String B) {
        // Check if the lengths of the strings are different
        if (A.length() != B.length()) {
            return 0;
        }
        
        // Initialize frequency arrays for both strings
        int[] freqA = new int[26]; // Assuming lowercase English alphabets
        int[] freqB = new int[26]; // Assuming lowercase English alphabets
        
        // Count the occurrences of each character in string A
        for (char ch : A.toCharArray()) {
            freqA[ch - 'a']++;
        }
        
        // Count the occurrences of each character in string B
        for (char ch : B.toCharArray()) {
            freqB[ch - 'a']++;
        }
        
        // Compare the frequency arrays
        for (int i = 0; i < 26; i++) {
            if (freqA[i] != freqB[i]) {
                return 0; // Frequency arrays are not equal, so permutation doesn't exist
            }
        }
        
        return 1; // Frequency arrays are equal, so permutation exists
    }
}
