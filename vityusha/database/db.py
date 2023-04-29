import pymongo
from aiogram.types import Message

CLIENT = pymongo.MongoClient('mongodb://localhost:27017/')
DB = CLIENT.Vitka
COLLECT = DB.creators



