print("="*20)
print(" Contact Book List ")
print("="*20)
contacts={}
while True:
    try:
        print("1.Add Contact \n2.View all contacts \n3.Search Contact \n4.Delete Contact \n5.Exit")
        cmd=int(input("Enter Your Choice:\n"))
        if cmd==5:
            print("Goodbye")
            break
        elif cmd==1:
            name=input("Enter Contact Name:\n").strip().title()
            number=input("Enter Phone Number:\n").strip()
            contacts[name]=number
            print(f"Contact:{name} has been added.\n")
    
        elif cmd==2:
            if not contacts:
                print("Empty Contacts\n")
            else:
                print("\n === Yours contacts are === ")
                for name,number in contacts.items():
                    print(f"Name:{name} | Number:{number}")
        elif cmd==3:
            nem=input("Enter name of contact:\n").strip().title()
            if nem in contacts:
                print(f"Found.{nem}'s number is {contacts[nem]}.\n")
            else:
                print(nem,"is not found in contact list.\n")
        elif cmd==4:
            nam=input("Enter name to delete contact:\n").strip().title()
            if nam in contacts:
                del contacts[nam]
                print(f"Contact '{nam}' has been deleted.\n")
            else:
                print(f"{nam} is not found.\n")
    except ValueError:
            print("Invalid Input")
