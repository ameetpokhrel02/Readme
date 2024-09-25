week1 =input("Enter the week name: ").lower()

if week1 == "saturday" or week1 == "sunday":
    print("Happy Weekends")
elif week1 in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Enjoy your week days")
else:
    print("Invalid")