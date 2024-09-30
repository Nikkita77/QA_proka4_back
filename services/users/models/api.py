import requests
import allure
from utils.helper import Helper
from config.headers import Headers
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints

from services.users.models.model_list_of_users import UserListModel
from services.users.models.model_user import UserModel


class UsersAPI(Helper):

    def __init__(self):
        self._payloads = Payloads()
        self._endpoints = Endpoints()
        self._headers = Headers()

    @allure.step("Get all users")
    def get_all_users(self, offset=0, limit=10, expected_result=True) -> UserListModel:
        response = requests.get(
            url=self._endpoints.get_users,
            headers=self._headers.basic,
            params={
                "offset": offset,
                "limit": limit
            },
            verify=False
        )
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UserListModel(**response.json())
        else:
            assert response.status_code != 200, response.json()
        self.attach_response(response.json())
        return model

    @allure.step("Create user")
    def create_user(self, expected_result=True) -> UserModel:
        response = requests.post(
            url=self._endpoints.create_user,
            headers=self._headers.basic,
            json=self._payloads.create_user_payload(),
            verify=False
        )
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UserModel(**response.json())
        else:
            assert response.status_code != 200, response.json()
        self.attach_response(response.json())
        return model

    @allure.step("Get user by uuid")
    def get_user_by_uuid(self, uuid, expected_result=True) -> UserModel:
        response = requests.get(
            url=self._endpoints.get_user_by_uuid(uuid),
            headers=self._headers.basic,
            verify=False
        )
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UserModel(**response.json())
        else:
            assert response.status_code != 200, response.json()
        self.attach_response(response.json())
        return model
