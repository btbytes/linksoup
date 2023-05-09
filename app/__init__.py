import toml
from fastapi.templating import Jinja2Templates

with open("config.toml", "r") as f:
    config = toml.load(f)
    users = config["users"]
    db_path = config["app"]["db_path"]
    secret_key = config["app"]["secret_key"]
templates = Jinja2Templates(directory="templates")
