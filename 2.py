# PYTHON PROGRAM 2

str=input("Enter your string: ")
list=str.split()

def length():
    max_len=0;
    for word in list:
        if(len(word)>max_len):
            max_len=len(word)
            temp=word
    print("Longest word is: ",temp)
    print("Length is: ",max_len)

def occurence():
    count=0;
    ch=input("Enter character: ")
    for i in range (len(str)):
        if(ch==str[i]):
            count=count+1
    print("Occurence is: ",count)

def palindrome():
    if(str==str[::-1]):
        print("String palindrome ")
    else:
        print("String is not palindrome")

def frequency():
    count=dict()
    for word in list:
        if word in count:
            count[word]=count[word]+1
        else:
            count[word]=1
    print("Frequency of words: ",count)

a=True

while(a==True):
    print("********MENU*********")
    print("1.Word with longest length")
    print("2.Occurence of particular character")
    print("3.Check Palindrome or not")
    print("4.Frequency of particular word in string")

    choice=int(input("Enter your choice: "))
    if(choice==1):
        print(length())
    elif(choice==2):
        print(occurence())
    elif(choice==3):
        print(palindrome())
    elif(choice==4):
        print(frequency())
    elif(choice==6):
        a=False
        break;

    else:
        print("Wrong choice")
    
    print("Enter 1 for continue")
    print("Enter 2 for exit")
    choice2=int(input("Enter choice 2:"))

    if(choice2==1):
        a=True
    elif(choice2==2):
        a=False
    else:
        print("Wrong choice")


