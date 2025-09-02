med=(input("enter cold if you are very very sick if not enter good"))
if med=="cold":
    print("DONT GO TO SCHOOL EVEN THERE IS A TEST")
else:
    ok=int(input("enter 4 if your temprature is lower than 90 if not enter 5"))
    if ok==4:
        print("now really dont go to school")
    elif ok==5:
        print("you can go to school :)")