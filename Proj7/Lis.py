def verify_subseq(seq, subseq):
    """
    Checks to see of a sequence is already in the bigger sequence
    :param seq: big sequence to check
    :param subseq: smaller sequence to check
    """
    for char in subseq:
        try:      
            seq = seq[seq.index(char)+1:]            
        except:
            return False
    return True


def verify_increasing(seq):
    """
    Checks if the sequence is in increasing order
    :param seq: sequence to check
    """
    for i in range( len(seq) - 1 ):
        if seq[i] >= seq[i+1]:
            return False
    return True



def find_lis(seq):
    """
    Returns the Longest Increasing Subsequence in the Given List/Array
    Returns the LIS
    :param seq: sequence used to find the LIS
    """
    N = len(seq)
    P = [0] * N
    M = [0] * (N+1)
    L = 0
    for i in range(N):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (seq[M[mid]] < seq[i]):
               lo = mid+1
           else:
               hi = mid-1
 
       newL = lo
       P[i] = M[newL-1]
       M[newL] = i
 
       if (newL > L):
           L = newL
 
    S = []
    k = M[L]
    for i in range(L-1, -1, -1):
        S.append(seq[k])
        k = P[k]
    return S[::-1]
