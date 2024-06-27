from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:12345678@localhost:3306/sennightlogdb")
    HOST: str = os.getenv("HOST", "localhost")
    PORT: str = os.getenv("PORT", "8000")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "jwt_secret_key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")


settings = Settings()