def circuit_output(A, B, C):
  
    A = bool(A)
    B = bool(B)
    C = bool(C)

    
    top_and = A and B
    middle_or = B or C
    bottom_and = B and C
    lower_and = middle_or and bottom_and

   
    Q = top_and or lower_and

    return Q



A = 1
B = 1
C = 0

print("Output Q =", int(circuit_output(A, B, C)))
