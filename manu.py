age = int(input("Enter user age:-"))
if age>=18:
    fnm=input("Enter your first name:-")
    lnm=input("Enter your last name:-")
    mobile=input("Enter mobilenumber:-")
    city=input("Enter your city:-")
    if fnm.isalpha() and lnm.isalpha() and mobile.isdigit() and city.isalpha():
        print("Full name:-",fnm+" "+lnm)
        if mobile==10:
            print(mobile)
        else:
            print("Enter 10 Digit mobile number")
        print(city)
    else:
        print("Enter true string and digit")
else:
    print("Enter your age above 18")