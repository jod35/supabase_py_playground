import os
from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

SUPABASE_API_KEY =os.getenv('SUPABASE_API_KEY')
SUPABASE_PROJECT_URL=os.getenv('SUPABASE_PROJECT_URL')


client:Client = create_client(
    supabase_url=SUPABASE_PROJECT_URL,
    supabase_key=SUPABASE_API_KEY,
)


