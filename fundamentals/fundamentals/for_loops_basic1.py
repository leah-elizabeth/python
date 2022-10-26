for i in range(0,151):
    print(i)

for i in range(5,1001,5):
    print(i)


for i in range(1,101):
    if i % 10 == 0:
        print ("Coding")
    elif i % 5 == 0:
        print("Coding Dojo")
    else:
        print(i)


# add odd intergers from 0 to 500000 and print the final sum

sum = 0
for i in range(1,500000,2):
    sum = sum + i
print(sum)

#print positive numbers starting at 2018, counting down by 4

for i in range(2018,0, -4):
    print(i)

#set three varialbes: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the intergers that are a multiple of mult

lowNum = 2
highNum = 78
mult = 4
for i in range(lowNum, highNum+1):
    if(i % 4 ==0):
        print(i)