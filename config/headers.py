import os
from dotenv import load_dotenv


load_dotenv()


class Headers:


    # def basic(self, xtask):
    #     return {
    #         "Authorization": f"Bearer {...}",
    #         "X-Task-Id": xtask
    #     }


    basic = {
        "Authorization": f"Bearer {os.getenv('TOKEN')}",
        "X-Task-Id": "API-1"
    }

print(Headers.basic)