import string
import random

def pswd():
    if __name__ == "__main__":
        s1 = string.ascii_lowercase
        #print(s1)
        s2 = string.ascii_uppercase
        #print(s2)
        s3 = string.digits
        #print(s3)
        s4 = string.punctuation
        #print(s4)
        plen = int(input("enter password length\n"))

        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)
        print()
        print()

        print("".join(s[0:plen]))
        print()
        print()
        print('DO YOU WANT ANOTHER PASSWORD??')
        print()
        print()
        print("Press 1 for YES")
        print("Press any other key to CONTINUE")
        print()
        print()
        
        i = input("Enter your choice ")
        if i == '1':
            pswd()
        else:
            pass


pswd()
