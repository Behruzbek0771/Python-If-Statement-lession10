email = input()

idx = email.find("@")
if "@" in email and "." not in email[:idx + 1] and " " not in email:
    print("ok")
else:
    print("error")