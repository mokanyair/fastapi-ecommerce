import time
from app.db.session import engine
from sqlalchemy.exc import OperationalError
from app.db.base_class import Base

def init_db():
    max_retries = 10
    for i in range(max_retries):
        try:
            Base.metadata.create_all(bind=engine)
            print(" Database connected and tables created")
            return
        except OperationalError:
            print("Waiting for DB...")
            time.sleep(2)

    raise Exception(" Could not connect to database")