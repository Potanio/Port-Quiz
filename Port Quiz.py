print ("Hello! Welcome to my port quiz! ")

playing = input("Do you want to play? y/n ")
if playing != "y":
    quit()

print("Okay! Lets get rolling :D " )
score = 0

answer = input("What port does FTP use?(You can use either one) ")
accepted_answers2 = ["20", "21"]
if answer != accepted_answers2:
    print("Correct!")
else:
    print("Incorrect!")  

answer = input("What port does SSH use? ")
if answer == "22":
    print("Correct!") 
    score +=1
else:
    print("Incorrect!")

answer = input("What port does Telnet use? ")
if answer == "23":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does SMTP use? ")
if answer == "25":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does DNS use? ")
if answer == "53":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does HTTP use? ")
if answer == "80":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does HTTPS use? ")
if answer == "443":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does NTP use? ")
if answer == "123":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does BGP use? ")
if answer == "179":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does IMAP4 use? ")
if answer == "143":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does Secure IMAP4 use? ")
if answer == "993":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does POP3 use? ")
if answer == "110":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does Secure POP3 use? ")
if answer == "995":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does SFTP use? ")
if answer == "22":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does DHCP use? ")
accepted_answers3 = {"67", "68"}
if answer != accepted_answers3:
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does SNMP use? ")
accepted_answers4 = {"161", "162"}
if answer != accepted_answers4:
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does Syslog use? ")
if answer == "514":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does LDAP use? ")
if answer == "389":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input("What port does LDAP5 use? ")
if answer == "636":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does RDP use? ")
if answer == "3389":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does SMB use? ")
if answer == "445":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does TFTP use? ")
if answer == "69":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does SIP use? ")
accepted_answers5= {"5060", "5061"}
if answer != accepted_answers5:
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does MS-SQL use? ")
if answer == "1433":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does SQL *Net use? ")
if answer == "1521":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What port does MySQL use? ")
if answer == "3306":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 25) * 100) + "%.")
    print("Thank you for playing! ")









