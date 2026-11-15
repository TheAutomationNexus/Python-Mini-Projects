print("!"*15)
print("Recipe CookBook")
print("!"*15)
cookbook={
    "pancakes":"Ingredients: Flour,Sugar,Milk,Baking Powder,Eggs",
    "omelets":"Ingredients: Eggs,Butter,Pepper,Cheese"}
while True:
    print("\n1.Add Recipe\n2.View all recipes\n3.Remove Recipie\n4.Search Recipe\n5.Exit")
    cmd=input("Enter choice between 1 to 5:\n").strip()
    if cmd=="5":
        print("Goodbye")
        break
    elif cmd=="1":
        name=input("Enter Name of new recipe:\n").strip().lower()
        ingredients=input("Enter Ingredients of recipe:\n").strip().lower()
        cookbook[name]=ingredients
        print(f"{name} has been added in cookbook")
    elif cmd=="2":
        if not  cookbook:
            print("Recipe List is empty.")
        else:
            print("\n=== Recipe List ===")
            for name,details in cookbook.items():
                print(f"Name:{name.capitalize()}\t>>>\tDetails:{details}")
    elif cmd=="3":
        if not  cookbook:
            print("Recipe List is empty")
        else:
            user=input("Enter Name to remove:\n").strip().lower()
            if user not in cookbook:
                print("f{user} is not found in recipe list.")
            else:
                cookbook.pop(user)
                print(f"{user} has been deleted from cookbook.")
    elif cmd=="4":
        if not cookbook:
            print("Recipe List is empty.")
        else:
            search=input("Enter Recipe name to search:\n").strip().lower()
            if search not in cookbook:
                print(f"{search} is not found in cookbook.")
            else:
                name=cookbook[search]
                print(f" You searched recipe {name} is here:\n {search.capitalize()}:{name}")
    else:
        print("Invalid Input. Enter just number between 1 to 5\n")
        
