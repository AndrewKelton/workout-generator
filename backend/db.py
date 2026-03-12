import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
  return psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    database=os.getenv("DB_NAME", "workout_gen"),
    user=os.getenv("DB_USER", "workout_user"),
    password=os.getenv("DB_PASSWORD", "workout1234")
  )
