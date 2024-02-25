from os import path

from dotenv import load_dotenv
from environs import Env


BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

env = Env()
env.read_env()