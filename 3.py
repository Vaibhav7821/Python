# PYTHON PROGRAM 3

r=int(input("Enter no of rows: "))
c=int(input("Enter no of cols: "))

A_mat=[[0 for j in range (c)] for i in range (r)]
print("Enter elements of A: ")

for i in range (r):
    for j in range (c):
        row=int(input())
        A_mat[i][j]=row

print("Display matrix A: ")
for n in A_mat:
    print(n)



B_mat=[[0 for j in range (c)] for i in range (r)]
print("Enter elements of B: ")

for i in range (r):
    for j in range (c):
        row=int(input())
        B_mat[i][j]=row

print("Dislay Matrix B:")
for n in B_mat:
    print(n)


def add():
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            C_mat[i][j]=A_mat[i][j]+B_mat[i][j]
    print("Addition of A and B:")
    for n in C_mat:
        print(n)

def sub1():
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            C_mat[i][j]=B_mat[i][j]-A_mat[i][j]
    print("Subtraction of matrix A from B: ")
    for n in C_mat:
        print(n)


def sub2():
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            C_mat[i][j]=A_mat[i][j]-B_mat[i][j]
    print("Subtraction of matrix B from A: ")
    for n in C_mat:
        print(n)


def mult():
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            for k in range (len(B_mat)):
                C_mat[i][j]+=A_mat[i][k]*B_mat[k][j]
    print("Multiplication of matrix A and B:")
    for n in C_mat:
        print(n)

def trans1():
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            C_mat[i][j]=A_mat[j][i]
    print("Transpose of matrix A:")
    for n in C_mat:
        print(n)


def trans2():
    C_mat=[[0 for j in range (c)] for i in range (r)]
    for i in range (r):
        for j in range (c):
            C_mat[i][j]=B_mat[j][i]
    print("Transpose of matrix B:")
    for n in C_mat:
        print(n)

a=True

while(a==True):
    print("*******MENU********")
    print("1.Addition of matrix")
    print("2.Subtraction of matrix A from B")
    print("3.Subtraction of matrix B from A")
    print("4.Multiplication of matrix B from A")
    print("5.Transpose of matrix A")
    print("6.Transpose of matrix B")
    print("7.Exit")
    
    ch=int(input("Enter your choice: "))
    if(ch==1):
        print(add())
    elif(ch==2):
        print(sub1())
    elif(ch==3):
        print(sub2())
    elif(ch==4):
        print(mult())
    elif(ch==5):
        print(trans1())
    elif(ch==6):
        print(trans2())
    elif(ch==7):
        print("Exiting....")
        a=False

    
