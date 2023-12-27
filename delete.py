from main import client


deleted_data = client.table("posts").delete().eq("id","3").execute()