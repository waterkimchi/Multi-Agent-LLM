from dotenv import load_dotenv
import os

load_dotenv()

st = os.getenv("APIKEY")

print(st)