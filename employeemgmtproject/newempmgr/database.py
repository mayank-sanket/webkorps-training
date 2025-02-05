import psycopg2

from psycopg2.extras import RealDictCursor

# from psycopg2.extras import DictCursor

from dotenv import load_dotenv

import os
load_dotenv()

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="employeemgmt",
            user='postgres',
            password=os.environ.get('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        # self.cursor = self.connection.cursor()
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        # self.cursor = self.connection.cursor(cursor_factory=DictCursor)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()