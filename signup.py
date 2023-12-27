from main import client


email = "jodestrevin@gmail.com"
password = "Kig2@aug"

user = client.auth.sign_up({"email":email,"password":password})

print("newly created user: ",user)