from config.base_test import BaseTest


class TestWishlist(BaseTest):

    # def test_get_all_users(self):
    #     user = self.api_users.create_user()
    #     users_list = self.api_users.get_all_users(offset=0, limit=20)
    #     user_exists = any(element.email == user.email for element in users_list.users)

    # def test_get_user(self):
    #     user = self.api_users.create_user()
    #     self.api_users.get_user_by_uuid(user.uuid)
    #     print(user.uuid)

    def test_get_wishlist(self):
        user = self.api_users.create_user()
        self.api_wishlist.get_users_wishlist_by_uuid(user.uuid)
