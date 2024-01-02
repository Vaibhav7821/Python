r=int(input("Enter no of rows:"))
c=int(input("Enter no of columns:"))
A_mat=[[0 for j in range (c)] for i in range (r)]
print("Enter elements of 1st matrix: ")
for i in range (r):
    for j in range (c):
        rows=int(input())
        A_mat[i][j]=rows

print("Display matrix 1st: ")
for n in A_mat:
    print(n)


B_mat=[[0 for j in range (c)] for i in range (r)]
print("enter elements of 2nd matrix:")
for i in range (r):
    for j in range (c):
        rows=int(input())
        B_mat[i][j]=rows

print("Display matrix 2nd:")
for n in B_mat:
    print(n)


def add():
    C_mat=[[0 for j in range (c)] for i in range (r)]

    for i in range (r):
        for j in range (c):
            C_mat[i][j]=A_mat[i][j]+B_mat[i][j]
    print("Addition of matrix: ")
    for n in C_mat:
        print(n)
    

def sub1():
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            C_mat[i][j]=A_mat[i][j]-B_mat[i][j]
    print("Subtraction of matrix 1st from 2nd: ")
    for n in C_mat:
        print(n)
    
def sub2():
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            C_mat[i][j]=B_mat[i][j]-A_mat[i][j]
    print("Subtraction of matrix 2nd from 1st: ")
    for n in C_mat:
        print(n)


def trans1():
 
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            C_mat[i][j]=A_mat[j][i]
    print("Transpose of 1st matrix:")
    for n in C_mat:
         print(n)


def trans2():
 
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            C_mat[i][j]=B_mat[j][i]
    print("Transpose of 2nd matrix:")
    for n in C_mat:
        print(n)

def mult():
    C_mat=[[0 for j in range (c)] for i in range (r)]

    for i in range (r):
        for j in range (c):
            for k in range (len(B_mat)):
                C_mat[i][j]+=A_mat[i][k]*B_mat[k][j]

    print("Multiplication of matrix: ")
    for n in C_mat:
        print(n)


a=True

while a:
    print("1.Addition of matrix")
    print("2.Subtraction of matrix 1st from 2nd")
    print("3.Subtraction of matrix 2nd from 1st")
    print("4.Transpose of 1st matrix")
    print("5.Transpose of 2nd matrix")
    print("6.Multiplication of matrix")
    
    ch=int(input("Enter your choice:"))
    if(ch==1):
        add()
    elif(ch==2):
        sub1()
    elif(ch==3):
        sub2()
    elif(ch==4):
        trans1()
    elif(ch==5):
        trans2()
    elif(ch==6):
        mult()
    elif(ch==7):
         a=False
         break
    else:
        print("Wrong choice")
    print("1.Continue?")
    print("2.exit")
    ch2=int(input("Enter choice2: "))
    if(ch2==1):
        a=True
    elif(ch2==2):
        a=False
        break;
    else:
        print("Wrong choice")
