class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self._access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        user_list.append(self)


    def add_user(self, user_list, user):
        if user in user_list:
            print('User already exists')
            return
        if isinstance(user, User):
            user_list.append(user)
            print(f'User {user.get_name()} added')
        else:
            print('Invalid user object')

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f'User {user.get_name()} removed')
                return
        print(f'User with ID {user_id} not found')

def show_users(user_list):
    for user in user_list:
        print(f'User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}')

user_list = []

user1 = User(1, 'John')
user2 = User(2, 'Jane')
user3 = User(3, 'Bob')

admin = Admin(4, 'Michael')

admin.add_user(user_list, admin)
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)
admin.add_user(user_list, user3)

show_users(user_list)

admin.remove_user(user_list, 1)
admin.remove_user(user_list, 5)

show_users(user_list)
