#for loop syntax
#for element in sequence:
#    body of for loop


#Range syntax: without loop statement you can't run range programs
#range(stop)
#range(start,stop)
#range(start,stop,stepsize)

#examples
#1
r1=range(10)
print(r1)
print(type(r1))

#2
for i in range(10): #takes n-1 i.e 10-1=9
    print(i)

#3
for i in range(10,20): #takes 10=start 20=stop: takes 20-1
    print(i)

#4
for i in range(1,11,1): #takes 1=start,11=stop:takes 11-1,1=stepsize: adds 1 everytime
    print(i)