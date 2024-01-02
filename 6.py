data=[]
n=int(input("Enter number of students: "))
for i in range (0,n):
    num=float(input("Enter FE percentage: "))
    data.append(num)

print("Entered percentage are:(unsorted list) ")
print(data)

def partition(arr,low,high):


def quick_sort(arr,low,high):
        if(low<high):
            pi=partition(arr,low,high)
            quick_sort(arr,low,pi-1)
            quick_sort(arr,pi+1,high)

def topfive(data):
    for i in ran

