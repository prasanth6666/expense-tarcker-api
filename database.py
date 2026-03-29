from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
Database_URL = mysql+pymysql://root:password@localhost/expense_tracker
engine = create_engine(Database_URL)
SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

