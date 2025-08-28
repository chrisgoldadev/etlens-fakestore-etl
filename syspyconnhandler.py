import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(r'secrets.env')
    
class ConnectionHandler:
    
    @staticmethod
    def connect_to_database(database=None):

        # Neon daje pełny connection string w zmiennej DATABASE_URL
        con_str = os.getenv("DATABASE_URL")

        # SQLAlchemy oczekuje drivera, więc wymuszamy psycopg i SSL
        if con_str.startswith("postgresql://"):
            con_str = con_str.replace("postgresql://", "postgresql+psycopg://", 1)
        if "sslmode=" not in con_str:
            sep = "&" if "?" in con_str else "?"
            con_str = f"{con_str}{sep}sslmode=require"

        engine = create_engine(con_str)
        return engine

