import random
import string

print(":"*30)
print("  Secure Password Generator")
print(":"*30)

while True:
    try:
        print("\n1.Generate Password\n2.Exit")
        cmd=int(input("Enter Choice:\n"))
        
        if cmd==2:
            print("Goodbye!")
            break
        
        elif cmd==1:
            length=int(input("Enter Length of password:\n"))
            #Combining letters, digits, punctuation to make single characters
            characters=string.ascii_letters+string.digits+string.punctuation
            password="".join(random.choice(characters) for _ in range(length))
            print("The password is\n",password)

        else:
            print("Try Again!")
            
    except ValueError:
        print("Invalid Input")
