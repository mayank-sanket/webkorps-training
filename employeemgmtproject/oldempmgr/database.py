import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()








































































def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="employeemgmt",
            user='postgres',
            password=os.environ.get('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None