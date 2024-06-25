from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:12345678@localhost:3306/sennightlogdb")


settings = Settings()