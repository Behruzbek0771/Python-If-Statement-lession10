phone = input("enter phone: ")

if phone.startswith(("90", "91")):
    print("beeline")
else:
    if phone.startswith(("93", "94")):
        print("Ucel")
    else:
        if phone.startswith(("99", "95")):
            print("Uzmobile")
        else:
            if phone.startswith(("88", "97")):
                print("Mobiuz")
            else:
                print("nomalum")