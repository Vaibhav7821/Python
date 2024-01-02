marks=[]
n=int(input("Enter no of students: "))

print("Enter marks of students: ")
for i in range (0,n):
    ele=float(input())
    marks.append(ele)
print("Entered marks are: ")
print(marks)


def Selection_sort():
    for i in range (len(marks)-1):
        for j in range (i+1,len(marks)):
            if(marks[i]>marks[j]):
                c=marks[i]
                marks[i]=marks[j]
                marks[j]=c
    print(marks)


def Bubble_sort():
    for i in range (len(marks)-1):
        for j in range (0,len(marks)-i-1):
            if marks[j]>marks[j+1]:
                c=marks[j]
                marks[j]=marks[j+1]
                marks[j+1]=c
    print("Marks of students after performing bubble sort: ")
    print(marks)


a=True

while(a==True):
    print("*******MENU********")
    print("1.Using selection sort")
    print("2.Using bubble sort")
    print("3.Exit")

    ch=int(input("Enter choice: "))

    if(ch==1):
        print(Selection_sort())
    if(ch==2):
        print(Bubble_sort())
    elif(ch==3):
        print("Exiting...")
        a=False

