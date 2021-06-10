import motor.motor_asyncio
import re

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
        result = await login_collection.find_one({"username": username, "password": password}, {'_id': 0})
        if result is None:
            return False
        else:
            return result

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
    async def set_issue(entry_id: int, entry_data):
        data_collection = db['data']
        result = await data_collection.update_one({"id": int(entry_id)}, {"$set": entry_data})
        return result

    @staticmethod
    async def get_all_issued():
        dat = []
        data_collection = db['data']
        result = data_collection.find({"issued": {"$ne": ""}}, {"_id": 0})
        for document in await result.to_list(length=100):
            dat.append(document)
        return dat

    @staticmethod
    async def get_last_inserted_item():
        dat = []
        data_collection = db['data']
        last_count = data_collection.find({}, {"_id": 0}).sort("id", -1)
        for document in await last_count.to_list(length=100):
            dat.append(document)
        return dat

    @staticmethod
    async def single_employee_data(empid: str):
        data_collection = db['users']
        result = await data_collection.find_one({"empid": empid}, {'_id': 0})
        return result

    @staticmethod
    async def update_single_employee_data(empid: str, entry_data: dict):
        data_collection = db['users']
        result = await data_collection.update_one({"empid": empid}, {"$set": entry_data})
        return result

    @staticmethod
    async def check_deleted_employee(empid: str):
        data_collection = db['users']
        result = await data_collection.find_one({"empid": empid}, {'_id': 0})
        if not result:
            return False
        else:
            return True

    @staticmethod
    async def filtered_data(field, value):
        dat = []
        data_collection = db['data']
        pat = re.compile(value, re.I)
        results = data_collection.find({ field: {'$regex': pat}}, {'_id': 0})
        for document in await results.to_list(length=100):
            dat.append(document)
        return dat

    @staticmethod
    async def filtered_data_issued(field, value):
        dat = []
        data_collection = db['data']
        pat = re.compile(value, re.I)
        results = data_collection.find({field: {'$regex': pat}, "issued": {"$ne": ""}}, {'_id': 0})
        for document in await results.to_list(length=100):
            dat.append(document)
        return dat



# { $text: { $search: "java coffee shop" } }

# { <field>: { $elemMatch: { <query1>, <query2>, ... } } }
