import os


class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "jwt_secret_key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_DAYS: int = 30


settings = Settings()
