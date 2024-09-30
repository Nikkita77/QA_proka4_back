from services.users.api import UsersAPI
from services.wishlists.api import WishlistsAPI


class BaseTest:

    def setup_method(self):
        self.api_users = UsersAPI()
        self.api_wishlist = WishlistsAPI()
