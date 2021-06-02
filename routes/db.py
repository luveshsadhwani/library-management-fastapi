import motor.motor_asyncio

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
        results = data_collection.find({}, {'_id': 0})
        for document in await results.to_list(length=100):
            dat.append(document)
        return dat

    @staticmethod
    async def check_token(token: str):
        result = await token_collection.find_one({"token": token})
        return result

    @staticmethod
    async def login_check(username, password):

        login_collection = db['login']
        result = await login_collection.find_one({"username": username, "password": password})
        if result is None:
            return False
        else:
            return True

    @staticmethod
    async def post_data(data: dict):
        data_collection = db['data']
        await data_collection.insert_one(data)
        print("Done")

    @staticmethod
    async def count_data():
        data_collection = db['data']
        result = await data_collection.count_documents({})
        return result

    @staticmethod
    async def update_data(entry_id: int, entry_data: dict):
        data_collection = db['data']
        result = await data_collection.update_one({"id": int(entry_id)}, {"$set": entry_data})
        return result

    @staticmethod
    async def delete(entry: dict):
        data_collection = db['data']
        result = await data_collection.delete_one(entry)
        return result

    @staticmethod
    async def find_one_entity(entity_id: int):
        data_collection = db['data']
        result = await data_collection.find_one({"id": entity_id}, {'_id': 0})
        return result

    @staticmethod
    async def set_issue(entry_id: int, issued):
        data_collection = db['data']
        result = await data_collection.update_one({"id": int(entry_id)}, {"$set": {'issued': issued}})
        return result
