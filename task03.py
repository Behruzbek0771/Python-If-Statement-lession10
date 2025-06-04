a = input("Bitta harf kiriting: ")

if a.isalpha():
    if a.isupper():
        print("Katta harf")
    if a.islower():
        print("Kichik harf")
else:
    print("Faqat harf kiriting.")
