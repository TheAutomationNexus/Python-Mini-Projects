print(":"*20)
print(" Number Guess Game ")
print(":"*20)
import random
while True:
    try:
        print("\n1.Play\n2.Exit")
        cmd=int(input("Enter Choice:\n"))
        if cmd==2:
            print("Goodbye")
            break
        elif cmd==1:
             num=random.randint(1,100)
             attempts=0        
             while True:
                    0
                    try:

                        usnum=int(input("\nEnter a number between 1 and 100:\n"))
                        attempts+=1
                        if usnum>num:
                            print("Too high. Try Again!")
                        elif usnum<num:
                            print("Too low. Try Again!")
                        elif usnum==num:
                            print(f"You win.It took you {attempts} attempts.\n")
                            break
                        else:
                            print("Invalid Input")
                    except ValueError:
                        print("Invalid Input.Please Enter only number.\n")
        else:
            print("Invalid Input.Try Again.")
    except ValueError:
        print("Invalid Number. Only Enter 1 or 2\n")
        
