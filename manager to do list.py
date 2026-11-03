print("="*15)
print("Manager To Do List")
print("="*15)
tasks=[]
while True:
    try:
        print("Welcome to Manager To do List")
        print("\n1.Add Task \n2.View Task \n3.Delete task \n4.Exit")
        cmd=int(input("Enter your choice:(1-3)\n"))
        if(cmd==4):
            print("Goodbye")
            break
        elif cmd==1:
            task=input("Enter a new task:\n")
            tasks.append(task)
            print(task,"has been added.")
        elif cmd==2:
            if not tasks:
                print("List is empyt.")
            else:
                print("\n=== Task list is ===")
                for index, t in enumerate (tasks,start=1):
                    print(f"{index}.{t}")
        elif cmd==3:
            if not tasks:
                print("List is empty.")
                break
            else:
                for index, t in enumerate (tasks,start=1):
                    print(f"{index}.{t}")
                cmt=int(input("Enter task number you want to remove:"))
                tasks.pop(cmt-1)
                
    except ValueError:
        print("Invalid Input. Try Again.")
