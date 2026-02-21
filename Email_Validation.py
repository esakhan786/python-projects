email = input("Enter email: ")

k = 0
d = 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if "." in email.split("@")[1]:

                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        continue
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@" or i == "-":
                        continue
                    else:
                        d = 1

                if k == 1 or d == 1:
                    print("Invalid Email ❌")
                else:
                    print("Valid Email ✅")

            else:
                print("wrong email 4 (Dot missing)")
        else:
            print("wrong email 3 (@ issue)")
    else:
        print("wrong email 2 (Start with letter)")
else:
    print("wrong email 1 (Too short)")