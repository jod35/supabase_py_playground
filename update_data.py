from main import client


data = client.table("posts").update({"title":"Is the Catholic Church a source for bad?","description":"This was a bad debate"}).filter("id","eq","2").execute()

print("updated data",data)