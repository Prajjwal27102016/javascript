age = int(input("enter your age if your are is lower than 18 type e if your age is more than 18 or 18 type q"))
if age=="e":
    print("you are a child now")
else:
    ok=int(input("enter 5 if you are teenagers if not type 4"))
    if ok=="5":
        print("WOW you are a teenagers")
    elif ok =="4":
        print ("you are under 14 so you are a child")
