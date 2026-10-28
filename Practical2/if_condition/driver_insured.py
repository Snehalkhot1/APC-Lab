marital = input("Married? (yes/no): ")
gender = input("Gender (male/female): ")
age = int(input("Enter age: "))

if marital == "yes":
    print("Driver is Insured")
elif marital == "no":
    if gender == "male" and age > 30:
        print("Driver is Insured")
    elif gender == "female" and age > 25:
        print("Driver is Insured")
    else:
        print("Driver is Not Insured")