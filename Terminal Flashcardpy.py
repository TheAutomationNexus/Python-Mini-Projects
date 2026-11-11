print(":"*20)
print("Flashcard Study Tools")
print(":"*20)
flashcard={"variable": "A variable to store information",
     "python": "A fantastic Programming language",
     "dictonary": "A collection of words with their meanings"}
while True:
    try:
        print("\n1.Add flashcard\n2.View all flash cards\n3.Remove flashcard \n4.Study Quiz\n5.Exit")
        cmd=int(input("Enter your choice:\n"))
        if cmd==5:
            print("Goodbye")
            break
        elif cmd==1:
            term=input("Enter the word/term to add:\n").lower()
            definitions=input("Enter the definition/meaning to add:\n")
            if term in flashcard:
                print(f"{term} term already exist in flash card.")
            elif term=="" or definitions=="":
                print(f"{term} field can't be empty.")
            else:
                flashcard[term]=definitions
                print(f"{term} has been successfully added.")
        elif cmd==2:
            
            if len(flashcard)==0:
                print("There are no flashcards.]\n")
            else:
                print("\n=== Flashcards View ===")
                for terms,definitions in flashcard.items():
                    print(f"{terms}:\t{definitions}")
        elif cmd==3:
            if len(flashcard)==0:
                print(" There is no flashcard to remove.")
            else:
                re_term=input("Enter term to remove:\n").lower()
                if re_term in flashcard:
                    flashcard.pop(re_term)
                    print(f"{re_term} has been removed from flashcard.")
                else:
                    print(f"{re_term} is not found in flashcard.")
        elif cmd==4:
            if not flashcard:
                print("No term is found in flashcard.")
            else:
                print("\n === Flashcard ===")
                score=0
                total=len(flashcard)
                for terms, definitions in flashcard.items():
                    print(f"Definition:{definitions}")
                    user=input("Enter term or type 'quit' to exit:\n")
                    if user=="quit":
                        print("Excited to quit.")
                        break
                    elif user==terms:
                        print("Correct")
                        score+=1
                    else:
                        print(f"{user} term is not found.")
            print(f"\nQuiz finished. Total score is {score}/{total}")
        else:
            print("Enter only between 1 and 5.")
    except ValueError:
        print("Invalid Input.Try Again.")
