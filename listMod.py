def checknumber(list):
    T = 0;
    L = len(list)
    N = []
    for T in range (0,L):
        if (list[T] > 1) and (list[T]<20):
            N.extend([list[T]])
    return N
    
    
test = [2,4,6,8,16,31,64]
    
print checknumber(test)



