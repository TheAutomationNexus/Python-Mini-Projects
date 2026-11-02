print("="*15)
print("Contact Book")
print("="*15)
contacts={}
while True:
    print("\n1.Enter new contact \n2.View Contact \n3.Exit")
    inp=int(input("Enter Your Choice:\n"))
    if inp==3:
        print("Goodbye")
        break
    elif inp==1:
        name=input("Enter Name:\n")
        num=input("Enter Phone Number:\t")
        contacts[name]=num
        print(f"Saved {name}")
    elif inp==2:
        print("\n--- View Contacts ---")
        for name,phone in contacts.items():
            print(f"{name}⏩{phone}")
    else:
        print("Try Again")
