import itertools

list0=[10,70,100]
list1 = [30,50,100]
list2 = [30,70,200] #1st
list3 = [20,40,60] # good
list4 = [30,50,100]
list5 = [-40,50,20,300] #2nd
list6 = [10,50,100] # bad
list7 = [20,30,60]
list8 = [-40,50,20,300] #2nd

results=[]
for i in range(3):
    for j in range (3):
        for k in range (3):
            results.append(list1[i]+list2[j]+list3[k])

results.sort()
length = len(results)
print(results[int(length/2)+1])

goodsum = list(map(lambda x:sum(x),itertools.product(list3,list4,list5)))
badsum = list(map(lambda x:sum(x),itertools.product(list6,list7,list8)))

goodsum.sort()
badsum.sort()

lengthg= len(goodsum)
lengthb = len(badsum)
print(goodsum[int(lengthg/2)+1])
print(badsum[int(lengthb/2)+1])
