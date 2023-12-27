from main import client

email = "jodestrevin@gmail.com"
password = "Kig2@aug"

user = client.auth.sign_in_with_password({
    "email":email,
    "password":password
})

print("logged in user: ",user)