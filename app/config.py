from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "jwt_secret_key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:12345678@localhost:3306/sennightdb")


settings = Settings()
