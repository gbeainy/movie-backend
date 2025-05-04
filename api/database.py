"""Database configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLACLHEMY_DATABASE_URL = "sqlite:///./movies.db"

# Créer un moteur de base de données (engine) qui établit la connexion avec notre base SQLite (movies.db)
engine = create_engine(
    SQLACLHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Définir SessionLocal, qui permet de créer des sessions pour intéragir avec la base de données.
Sessionlocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# Définir Base, qui servira de classe de base pour nos modèles SQLAlchemy.
Base = declarative_base()

# if __name__ == "__main__":
#     try:
#         with engine.connect() as conn:
#             print("Connection à la databse réussie")
#     except Exception as e:
#         print("Erreur de connexion à la database : {e}")