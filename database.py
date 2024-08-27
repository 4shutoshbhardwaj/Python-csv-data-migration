from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'mysql+pymysql://username:password@sql12.freesqldatabase.com/sql12728040'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
