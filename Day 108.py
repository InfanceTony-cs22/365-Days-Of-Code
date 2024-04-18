public static void solve(BitSet b1, BitSet b2) {
    // Store the cardinality of BitSet b1 in variable c1
    int c1 = b1.cardinality();
    
    // Store the cardinality of BitSet b2 in variable c2
    int c2 = b2.cardinality();
    
    // Xor BitSet b1 with BitSet b2
    b1.xor(b2);
    
    // Store the cardinality of BitSet b1 in variable c3
    int c3 = b1.cardinality();
    
    /*Don't alter the code below*/
    System.out.println(c1 + " " + c2 + " " + c3);
    /*******************************/
}
