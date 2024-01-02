a=[];
n=int(input("Enter no of students: "))
print("Enter -1 for absent students: ")

print("Enter marks of students:  \n")
for i in range (0,n):
    marks=int(input())
    a.append(marks)

def average(list):
    sum=0
    absent=0
    for x in list : 
        if(x!=-1):
            sum=sum+x;
        else:
            absent=absent+1
    avg=sum/n-absent
    print("Average of marks: ")
    print(avg)


def highest(list):
    max=list[0]
    for x in list:
        if(x>max):
            max=x
    print("Highest marks is:")
    print(max)

def absent(list):
    absent=0
    for x in list:
        if(x==-1):
            absent=absent+1
    print("Absent students count is: ")
    print(absent)
    

def freq_high(list):
    max=list[0]
    count=0
    for x in list:
        if(x>max):
            max=x
    long=max
    for x in list:
        if(x==long):
            count=count+1

    print("Frequency of highest marks:")
    print(count)


def lowest(list):
    low=list[0]
    for x in list:
        if(x<low):
            low=x
    print("Lowest marks is: ")
    print(low)


b=True

while b:
    print("1.Average of marks")
    print("2.Highest marks")
    print("3.Absent students")
    print("4.frequency of highest marks")
    print("5.Lowest marks")

    ch=int(input("Enter your choice:  "))
    if(ch==1):
        average(a)
    elif(ch==2):
        highest(a)
    elif(ch==3):
        absent(a)
    elif(ch==4):
        freq_high(a)
    elif(ch==5):
        lowest(a)
    elif(ch==6):
        b=False
        break;
    else:
        print("Wrong choice\n")

    print("1.Continue?")
    print("2.Exit")
    ch2=int(input("Enter choice2: "))
    if(ch2==1):
        b=True
    elif(ch2==2):
        b=False
        break;
    else:
        print("Wrong choice\n")


