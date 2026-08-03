import os
from dotenv import load_dotenv

load_dotenv()

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")
if APP_SECRET_KEY is None or APP_SECRET_KEY == "":
	raise RuntimeError('В APP_SECRET_KEY ничего не найдено')
