import csv
from tkinter import messagebox
class UserManager:
    def __init__(self, csv_file='csv.csv'):
        self.csv_file = 'csv.csv'
        self.users = self.load_users()



    def count_add(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                user['times'] = str(int(user['times']) + 1)
                break

    def save(self, id, name, pwd, times=0):
        with open(self.csv_file, 'a+') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([id, pwd, times, name])
            return

    def signup_check(self, id):
        for user in self.users:
            if user['id'] == id:
                return False
        return True

    def find(self, id):
        with open(self.csv_file, newline='', encoding='gbk') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['id'] == id:
                    return True
        return None


    def login_check(self, id, pwd):
        for user in self.users:
            if user['id'] == id:
                if user['pwd'] == pwd:
                    return True
                else:
                    return '密码错误'
        return '没有该用户，请注册'


    def load_users(self):
        try:
            with open(self.csv_file, 'r', newline='', encoding='gbk') as file:
                reader = csv.DictReader(file)
                users = list(reader)
                return users
        except FileNotFoundError:
            return []

    def save_users(self):
        with open(self.csv_file, 'w', newline='', encoding='gbk') as file:
            fieldnames = ["username", "password", "work_count", "name"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.users)



    def get_all_users_info(self):
        return [(user['id'], user['times'], user['name']) for user in self.users]

    def update_user_info(self, id, new_name, new_pwd):
        for user in self.users:
            if user['id'] == id:
                user['name'] = new_name
                user['pwd'] = new_pwd
                self.save_users()

