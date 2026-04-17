from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Ecommerce"
    API_V1_STR: str = "/api/v1"

    # Database
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "MyNewPassword123"
    POSTGRES_DB: str = "fastapi"

    # Build DB URI
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
    f"postgresql+psycopg2://{self.POSTGRES_USER}:"
    f"{self.POSTGRES_PASSWORD}@"
    f"{self.POSTGRES_SERVER}:5432/"
    f"{self.POSTGRES_DB}"
)

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]

    @property
    def all_cors_origins(self) -> List[str]:
        return self.BACKEND_CORS_ORIGINS

    # Optional: Sentry
    SENTRY_DSN: str | None = None
    ENVIRONMENT: str = "local"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()