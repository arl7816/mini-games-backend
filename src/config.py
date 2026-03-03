from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

# 3 main ways of adding attributes

# 1 REQUIRED: <name>: <type>
# 2 Optional <name>: <type> = <default>
# 3 Secret but required: <name>: <Secret Class such as SecretStr>

class Settings(BaseSettings):
    
    # required attributes
    DB_LOCATION: str
    

    # optional attributes
    APP_PORT: int = 8000 
    DEBUG_MODE: bool = False

    # look for a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Instantiate once to use across the project
settings = Settings()