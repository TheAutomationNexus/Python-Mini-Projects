import time
print("-_"*18)
print("Pomodoro Productivity Timer")
print("_-"*18)
task_log=[]
while True:
    print("\n1.Start 5 second test timer\n2.View Task Log \n3.Exit")
    cmd=input("Enter your choice:\n").strip()
    if cmd=="3":
        print("Keep your great work. GOODBYE!")
        break
    elif cmd=="1":
        try:
            minu=int(input("Enter Minutes you want to compete task:\n"))
            if minu<0:
                print("Invalid duration. Enter duration greater than 0")
                continue
        except ValueError:
            print("Invalid Input.Please enter only numbers")
            continue
        task_name=input("Enter Task Name:\n").strip().capitalize()
        
        sec=minu*60
        print(f"\nStarting Focusing Session of {minu} minutes for {task_name}")
        while sec>0:
            mins,secs=divmod(sec,60)
            tim_format=f"{mins:02d}:{secs:02d}"
            print(f"Time Remaining: {tim_format} seconds")
            time.sleep(1)
            sec-=1
        print("Time Over. Its Great.")
        if task_name:
            task_log.append(task_name)
    elif cmd=="2":
        if not  task_log:
            print("Task Log is empty.")
        else:
            print("\n=== Task LOG HERE ===")
            for i,task in enumerate(task_log,1):
                print(f"Number {i}:\t{task}")
    else:
        print("Invalid Choice. Enter only between 1 to 3\n")
