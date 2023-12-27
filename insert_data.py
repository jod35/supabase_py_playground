from main import client


from main import client

data = client.table("posts").insert({"title":"Letter to a christian church","description":"This was an awesome book by Sam Harris"}).execute()

print(data.data)


