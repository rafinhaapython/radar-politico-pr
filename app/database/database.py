from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/radar.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)