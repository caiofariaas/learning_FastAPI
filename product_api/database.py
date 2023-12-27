# This imports the 'create_engine' function from the 'SQLAlchemy' library. This function is used to create a database engine.
#  responsible for managing the details of the database connection, execution of SQL statements, and other low-level database interactions.

from sqlalchemy import create_engine

#  'sessionmaker' is a class provided by 'SQLAlchemy' that serves as a factory for creating new 'Session' objects.
 
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./data.db'
engine = create_engine(DATABASE_URL)

# 'autocommit=False' makes the changes won't be automatically committed to the database
# 'autoflush=False' this parameter controls whether the session should automatically flush changes to database
# 'bind=engine' specifies the database engine to which the session should be bound
# this associates the session with a specific database connection.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
