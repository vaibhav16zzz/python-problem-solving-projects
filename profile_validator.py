# Profile Validator
# Created by Vaibhav Kale
# 7 Mar 2026

print("======================== PROFILE VALIDATOR =======================")
print("\nWelcome to the Profile Validator Program!")
print("\nProvide the following details to create a new profile:-")
print("\n- Username""\n- Password""\n- Mobile No.""\n- Age""\n- Gender")
print("\n==================================================================")

print("\nNOTE:-""\n\n# Username must be 4 characters long and under 10 characters""\n# Password must contain minimum 8 characters""\n# Mobile No. must be in numerical format""\n# Age must be 18 or above""\n# All fields are mandatory")
print("\n\n==================== ENTER YOUR DETAILS BELOW ====================")

username = input("\nEnter Username : ")
if(len(username)==0 or len(username)<4 or len(username)>10):
    print("\n>>> INVALID USERNAME LENGTH!")
    print("\n# PROFILE VERIFICATION FAILED")
    print("# Try again...")
else:
    print("\n>>> USERNAME VERIFIED")
    
    password = input("\nEnter Password : ")
    if(len(password)<8):
        print("\n>>> PASSWORD TOO SHORT!")
        print("\n# PROFILE VERIFICATION FAILED")
        print("# Try again...")
    else:
        print("\n>>> PASSWORD VERIFIED")
        
        mob = int(input("\nEnter Mobile No. : "))
        if(len(str(mob)) > 10 or len(str(mob)) < 10):
            print("\n>>> INVALID MOBILE NO.")
            print("\n# PROFILE VERIFICATION FAILED")
            print("# Try again...")
        else:
            print("\n>>> MOBILE NO. VERIFIED")
            
            age = int(input("\nAge (in numbers) : "))
            if(age<18):
                print("\n>>> YOU MUST BE 18 OR OLDER")
                print("\n# PROFILE VERIFICATION FAILED")
            elif(age>120):
                print("\n>>> INVALID AGE")
                print("\n# PROFILE VERIFICATION FAILED")
                print("# Try again...")
            else:
                print("\n>>> AGE VERIFIED")
                
                gen = input("\nGender (Male/Female/Other) : ")
                
                if(gen.lower() == "male" or gen.lower() == "female" or gen.lower() == "other"):
                    print("\n>>> GENDER DETAILS VERIFIED")
                    print("\n\n========================== YOUR DETAILS ==========================")
                    print("\nYOUR USERNAME -",username)
                    print("\nYOUR PASSWORD -", password)
                    print("\nYOUR MOBILE NO. -", mob)
                    print("\nYOUR AGE -", age, "y/o")
                    print("\nYOUR GENDER -", gen.upper())
                    print("\n\n>>> PROFILE CREATED SUCCESSFULLY <<<")
                else:
                    print("\n>>> INVALID GENDER")
                    print("\n# PROFILE VERIFICATION FAILED")
                    print("# Try again...")