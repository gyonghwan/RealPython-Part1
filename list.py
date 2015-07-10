# list assignmentn

def enrollment_stat(list):
    student = []
    tuition = []

    for school in list:
        student.append(school[1])
        tuition.append(school[2])
    return student, tuition

def mean (value):
    total = 0
    average = 0
    for index in range(len(value)):
        total += value[index]
    average = total/len(value)
    return average

def median (value):
    length = len(value)
    sort_list = sorted(value)
    output = 0.00

    if not length % 2:
        output = (int(value[length/2]) + int(value[length/2 - 1])) / 2
    else:
        output = (int(value[length/2]))

    return output


universities = [['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]]

output = enrollment_stat(universities)
print output

print mean(output[0])
print mean(output[1])
print median(output[0])
print median(output[1])
