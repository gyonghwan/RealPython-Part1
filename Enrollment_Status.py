def enrollment_stats(U):
    T = 0;
    Count = len(U)
    tList = []
    eList = []
    tSum = 0;
    eSum = 0;
    for T in range (0,Count):
        tList.append(U[T][1])
        eList.append(U[T][2])
        #tSum += int(U[T][1])
        #eSum += int(U[T][2])
    return tList,eList
    
def mean(L):
    T = 0;
    C = len(L)
    lSum = 0;
    M = 0;
    for T in range (0,C):
        lSum += int(L[T])
    M = lSum / C
    return M 

def median(L):
    T = 0;
    C = len(L)
    M = 0;
    if (C % 2) == 1:
        M = (L[(C/2)] + L[(C/2-1)])/2 
    else:
        M = L[C/2]
    return M
    
    
University = [['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['princeton',7802,37000],
              ['Rice',5879, 35551],
              ['Standford',19535,40569],
              ['Yale',11701,40500]]
             
print enrollment_stats(University)

Tuition = enrollment_stats(University)[0]
Student = enrollment_stats(University)[1]

print mean(Tuition)
print median(Tuition)
print mean(Student)
print median(Student)

