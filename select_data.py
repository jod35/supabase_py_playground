from main import client


data = client.table('posts').select("*").execute()

print("data",data)