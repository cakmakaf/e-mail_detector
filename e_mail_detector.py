with open("Random_Text.txt","r",encoding="utf-8") as file:
    for e_mail in file:
        e_mail = e_mail[:-1]
        if (e_mail.endswith(".com") and e_mail.find("@") != -1):
            print(e_mail)

