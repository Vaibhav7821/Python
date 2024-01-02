# PYTHON PROGRAM 1

a=[];
n=int(input("Enter no of students:  "))

print("Enter -1 for absents students\n")

for i in range (0,n):
    marks=int(input("ENter marks of students:  \n"))
    a.append(marks)

def Average(list):
    sum=0;
    absent=0;

    for x in list :
        if(x != -1):
            sum=sum+x;
        else:
            absent=absent+1;
    Avg = sum/n-absent
    print("Average of marks is: ")
    print(Avg)

def Highest_m(list):
    max=list[0]
    for x in list:
        if(x>max):
            max=x
    print("Highest Marks: ")
    print(max)

def absent_stud(list):
    absent=0
    for x in list:
        if(x==-1):
            absent=absent+1
    print("Absent no of students: ")
    print(absent)

def freq_high(list):
    max=list[0]
    for x in list:
        if(x>max):
            max=x
    count=0
    largest=max

    for x in list:
        if(x==largest):
            count=count+1
    print("Freq of highest marks: ")
    print(count)

def min_marks(list):
    min=list[0]
    if(min==-1):
        for i in range (0,n):
            min=list[i]
            if(min!=-1):
                break;

    for x in list:
        if(x!=-1 and x<min):
            min=x;
    print("Lowest Marks is:")
    print(min)

b=True

while b:
    print("1.Average of marks")
    print("2.Highest Marks")
    print("3.Absent Students")
    print("4.Freq of highest mark")
    print("5.Lowest marks")

    choice=int(input("Enter your choice: "))
    if(choice==1):
        print(Average(a))
    elif(choice==2):
        print(Highest_m(a))
    elif(choice==3):
        print(absent_stud(a))
    elif(choice==4):
        print(freq_high(a))
    elif(choice==5):
        print(min_marks(a))
    elif(choice==6):
        b=False
        break;
    else:
        print("Wrong choice")
    
    print("Press 1 for continue ")
    print("Press 2 for exit")
    choice2=int(input("Enter choie2: "))
    if(choice2==1):
        b=True
    elif(choice2==2):
        b=False
    else:
        print("Wrong choice")
