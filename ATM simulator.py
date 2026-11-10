print("|"*15)
print("ATM Simulator")
print("|"*15)
Balance=10000
while True:
    try:
        print("\n1.Check Balance\n2.Deposit Money\n3.Withdraw Money \n4.Exit")
        cmd=int(input("Enter Your Choice:\n"))
        if cmd==4:
            print("Goodbye")
            break
        elif cmd==1:
            print(f"Your Balance is ${Balance}")
        elif cmd==2:
            balance=float(input("Enter Money to deposit:\n"))
            if balance>0:
                Balance=Balance+balance
                print(f"New Balance is ${Balance}")
        elif cmd==3:
            withdraw=float(input("Enter amount to withdraw:\n"))
            if withdraw>Balance:
                print("Insufficent Withdrawn.")
            else:
                Balance=Balance-withdraw
                print(f"Withdrawn successfully. Remaining Amount is {Balance}")
    except ValueError:
        print("Invalid Input. Try Again.")
            
