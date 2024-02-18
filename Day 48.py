class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):  # Corrected function name
        total_gas = 0
        total_cost = 0
        start_index = 0
        current_gas = 0
        
        for i in range(len(A)):
            total_gas += A[i]
            total_cost += B[i]
            current_gas += A[i] - B[i]
            
            # If current gas becomes negative, reset start_index and current_gas
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0
        
        # If total_gas is less than total_cost, it's impossible to complete the circuit
        if total_gas < total_cost:
            return -1
        else:
            return start_index % len(A)
