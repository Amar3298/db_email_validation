email_input = input("Enter your email: ")
space = 0
upper_case = 0
other_char = 0
if(len(email_input)>=6):#1. email at least 6 character are there
    if(email_input[0].isalpha()): #2. first letter must be character
        if(("@" in email_input) and (email_input.count("@")==1)):#3. there must be only one @
            if((email_input[-4]==".")^(email_input[-3]==".")):#4. it must end with .com or .in we have use xor because either one must be true not both
                for i in email_input:
                    if(i==i.isspace()):#5. there must be no space 
                        space=1
                    elif(i.isalpha()):#6. there must be no upper letter character
                        if(i==i.upper()):
                            upper_case=1
                    elif(i.isdigit()):#7. if there is number in email it is valid
                        continue
                    elif(i in ["_",".","@"]):#8. email must contain this character only
                        continue
                    else:#9. if any other character it is an invalid email
                        other_char =1
                if(space==1 or upper_case==1 or other_char==1):
                    print("Wrong email 5")
                else:
                    print("Right email")
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")

input()