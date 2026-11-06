print("|=|"*10)
print(" Personal Expense Tracker")
print("|=|"*10)
expenses={}
while True:
    try:
        print("\n1.Add Expense \n2.View Expenses \n3.See Total Spent \n4.Exit")
        cmd=int(input("Enter Your choice:(1-4)\n"))
        if cmd==4:
            print("Goodbye")
            break
        elif cmd==1:
            name=input("Enter name of expense:\n").strip().title()
            exp=float(input("Enter Expense:\n"))
            expenses[name]=exp
            print(f"{name} has been added for cost ${exp:.2f}\n")
        elif cmd==2:
            if not expenses:
                print("Not found.\n")
            else:
                print("Your Expense List")
                for name,exp in expenses.items():
                    print(f"Name:{name} | cost:${exp:.2f}")
        elif cmd==3:
            total=sum(expenses.values())
            print(f"Total Spent Amount :{total:.2f}")
    except ValueError:
        print("Invalid Input.")
