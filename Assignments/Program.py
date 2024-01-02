

rows = int(input("Enter rows"))

num = 1

for i in range(rows):
    ch = 0
    for j in range(1,rows+1,ch):

        temp = num
        add = 0
        while(temp != 0):
            add = add + temp%10
            temp = temp/10

        if num%add == 0:
            print(num, end = " ")
            ch = ch + 1

        num = num +1

    print();

