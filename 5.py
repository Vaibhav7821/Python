a=[]
n=int(input("ENter no of elements:  "))
print("Elements are :")
for i in range (0,n):
    ele=int(input())
    a.append(ele)

def selection_sort(list):
    for i in range (0,n-1):
        for j in range (i+1,n):
            if(list[i]>list[j]):
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    return list 

def ternary_search(list,n,key):
    s=0
    e=n-1   
    while(s<=e):
        mid1=int(s+((e-s)/3))
        mid2=int(e-((e-s)/3))

        if(list[mid1]==key):
            return mid1
        elif(list[mid2]==key):
            return mid2
        elif(list[mid1]>key):
            e=mid2-1
        elif(list[mid2]<key):
            s=mid2+1
        else:
            s=mid1+1
            e=mid2-1

    return -1



while(True):
    print("1.For sorting the list")
    print("2.FOr searching element in the list")
    print("3.Exit")

    ch=int(input("Enter choice: "))

    if(ch==1):
        print("Sorted list is:  ",selection_sort(a))
    elif(ch==2):
        k=int(input("ENter element to be searched: "))
        ans=ternary_search(a,n,k)
        if(ans==-1):
            print("Element not found")
        else:
            print("Element found at  ",ans+1)
    elif(ch==3):
        print("Exiting.....")
        break
    else:
        print("Wrong choice")



