import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="cafe",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["default.toml", ".secrets.toml"],
    environments=["development", "production"],
    env_switcher="cafe_env",
    load_dotenv=False,
)
