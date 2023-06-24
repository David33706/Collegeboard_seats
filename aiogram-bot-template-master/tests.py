from utils.db_api.sqlite import Database


def test():
    db = Database(path_to_db='main.db')
    db.create_table_users()
    

    users = db.select_all_users()
    print(f"Barcha fodyalanuvchilar: {users}")

    user = db.select_user(Name="John", id=5)
    print(f"Bitta foydalanuvchini ko'rish: {user}")



test()
