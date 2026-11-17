print("_-"*20)
print("Caesar Cipher Encoder & Decoder")
print("_-"*20)
while True:
    print("\n1.Encode a message \n2.Decode a message \n3.Exit")
    cmd=input("Enter a number:\n").strip()
    if cmd=="3":
        print("GOODBYE.Stay Secret.")
        break
    elif cmd=="1" or cmd=="2":
        message=input("Enter your message:\n").strip()
        try:
            shift=int(input("Enter a number:(1-26)"))
            if shift<1 or shift>25:
                print("Enter number only between 1 and 26\n")
                continue
        except ValueError:
            print("Enter only a whole Number.")
            continue
        alphabet="abcdefghijklmnopqrstuvwxyz"    
        if cmd=="2":
            shift=-shift
        result = ""
        for char in message:
            if char.lower() in alphabet:
                pos=alphabet.index(char.lower())
                new_pos=(pos+shift)%26
                new_char=alphabet[new_pos]
                if char.isupper():
                    result+=new_char.upper()
                else:
                    result+=new_char
            else:
                result+=char
        print(f"'{message}' is converted into '{result}'")
    else:
        print("Only Enter 1,2 or 3")
