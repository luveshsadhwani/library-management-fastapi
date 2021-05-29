import motor.motor_asyncio
import json
from bson.json_util import dumps, loads

client = motor.motor_asyncio.AsyncIOMotorClient(
    f'mongodb+srv://ali123:{"imali123"}@cluster0.xdccr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['apidb']
token_collection = db['token']


class AuthDb:

    @staticmethod
    # test
    async def do_insert():
        data_collection = db['data']
        document = {'token': 'aasfdgfahdsfsdf1q231'}
        result = await data_collection.insert_one(document)
        print('result %s' % repr(result.inserted_id))



    @staticmethod
    async def return_data():
        dat = []
        data_collection = db['data']
        results = data_collection.find({})
        for document in await results.to_list(length=100):
            dat.append(document)
        return dat