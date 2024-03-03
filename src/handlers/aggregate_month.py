import json
import os
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from bson import ObjectId

from aiogram import types, F, Router

router = Router()

MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB = os.getenv('MONGODB_DB')
MONGODB_COLLECTION = os.getenv('MONGODB_COLLECTION')


@router.message(F.text)
async def aggregate_month():
    # Подключение к MongoDB
    client = AsyncIOMotorClient("MONGODB_URI")
    db = client["MONGODB_DB"]
    collection = db["MONGODB_COLLECTION"]

    # Определение дат и времени для фильтрации
    dt_from = datetime(2022, 9, 1, 0, 0, 0)
    dt_upto = datetime(2022, 12, 31, 23, 59, 0)

    # Выполнение агрегации
    pipeline = [
        {
            "$match": {
                "dt": {"$gte": dt_from, "$lte": dt_upto},
                "$expr": {"$in": [{"$month": "$dt"}, [9, 10, 11, 12]]},
            },
        },
        {
            "$group": {
                "_id": {
                    "month": {"$month": "$dt"},
                    "year": {"$year": "$dt"},
                },
                "dataset": {"$sum": "$value"},
                "labels": {
                    "$push": {
                        "$dateToString": {
                            "format": "%Y-%m-%dT00:00:00",
                            "date": "$dt",
                        }
                    }
                },
            },
        },
        {
            "$group": {
                "_id": None,
                "dataset": {"$push": "$dataset"},
                "labels": {"$push": "$labels"},
            },
        },
        {
            "$sort": {
                "_id.year": 1,
                "_id.month": 1,
            },
        },
        {
            "$project": {
                "_id": 0,
                "dataset": "$dataset",
                "labels": "$labels",
            },
        },
    ]

    result = await collection.aggregate(pipeline).to_list(length=None)

    client.close()

    # Обработка результата
    return result

