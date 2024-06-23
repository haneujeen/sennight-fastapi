import os


class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "jwt_secret_key")
    ALGORITHM: str = os.getenv("ALGORITHM", "jwt_secret_key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:12345678@localhost:3306/sennightdb")


settings = Settings()
