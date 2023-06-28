import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    main_url: str


# dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)


settings = Settings()
