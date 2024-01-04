from sqlmodel import Session, SQLModel, create_engine

from .config import settings

# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

# Base = declarative_base()
engine = create_engine(settings.DATABASE_URL, echo=True)

connect_args={"check_same_thread":False}

def create_tables():
    SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session