import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient(
    f'mongodb+srv://ali123:{"imali123"}@cluster0.xdccr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['apidb']
token_collection = db['token']


class AuthDb:

    @staticmethod
    async def check_token(token:str):
        result = token_collection.find_one({"token": token})
        if result:
            return True
        else:
            return False
