import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from User import UserManager
import random
import datetime

class Manage(tk.Tk):
    '''主页面'''
    def __init__(self):
        super().__init__()

        self.title("管理系统")
        self.geometry("400x300+100+200")
        self.main()
        # 创建主界面
    def hide(self):
        self.withdraw()

    def show(self):
        self.deiconify()


    def open_login(self, user_type):
        if user_type == "用户":
            self.hide()
            w = UserLogin(self)
        else:
            self.hide()
            w = AdminLogin(self)


    def open_signup(self):
        self.hide()
        w = UserSignup(self)




    def main(self):

        label = tk.Label(self, text="欢迎使用管理系统", font=("Helvetica", 16))
        label.pack(pady=20)

        # 创建下拉框，用于选择用户或管理员登录
        user_type_var = tk.StringVar(self)
        user_type_var.set("用户")

        user_type_menu = ttk.Combobox(self, textvariable=user_type_var, values=["用户", "管理员"])
        user_type_menu.pack(pady=10)

        login_button = tk.Button(self, text="登录",height=1,width=18,command=lambda: self.open_login(user_type_var.get()))
        login_button.pack(pady=10)

        signup_button = tk.Button(self, text="注册",height=1,width=18, command=lambda: self.open_signup())
        signup_button.pack(pady=10)

        out_button = tk.Button(self, text="退出",height=1,width=18, command=lambda: self.quit())
        out_button.pack(pady=10)

class UserLogin(tk.Toplevel):
    '''用户登录'''
    def __init__(self, master):
        super().__init__()
        self.title("")
        self.geometry("400x300+100+200")
        self.main()

    def main(self):
        id_label = Label(self, text="工号", font=("Arial"))
        id_label.grid(row=0, column=0)
        pwd_label = Label(self, text="密码", font=("Arial"))
        pwd_label.grid(row=1, column=0)
        e_id = Entry(self)
        e_id.grid(row=0, column=1)
        e_pwd = Entry(self, show='*')
        e_pwd.grid(row=1, column=1)

        b1 = Button(self, text="登录", font=("Arial"), command=lambda: self.login_check(e_id.get(), e_pwd.get()))
        b1.grid(row=2, column=0)
        b2 = Button(self, text="返回", command=self.back_manage)
        b2.grid(row=2, column=1)

    def back_manage(self):
        self.destroy()
        Manage().show()

    def login_check(self, e_id, e_pwd):
        user = UserManager()
        result = user.login_check(e_id, e_pwd)
        if result == True:
            messagebox.showinfo('','登陆成功')
            self.destroy()
            self.login()
            user.count_add(e_id)
        else:
            messagebox.showinfo('',result)

    def login(self):
        UserPage().show()


class AdminLogin(tk.Toplevel):
    '''管理员登录'''
    def __init__(self, master):
        super().__init__()
        self.title("")
        self.geometry("400x300+100+200")
        self.main()

    def main(self):
        pwd = Entry(self, show="*")
        login = Button(self, text="登录", command=lambda: self.login_check(pwd.get()))
        pwd.grid(column=0, row=0)
        login.grid(column=1, row=0)
        pass
    def back_manage(self):
        self.destroy()
        Manage().show()

        pass

    def login_check(self, pwd):
        if pwd == 'admin':
            messagebox.showinfo('', '登陆成功')
            self.destroy()
            u = AdminPage(self)

        else:
            messagebox.showerror('','登陆失败，密码错误')


class UserSignup(tk.Toplevel):
    '''用户注册'''
    def __init__(self, master):
        super().__init__()
        self.title("")
        self.geometry("400x300+100+200")
        self.main()
    def main(self):
        id_label = Label(self, text="工号", font=("Arial"))
        id_label.grid(row=0, column=0)
        name_label = Label(self, text="姓名", font=("Arial"))
        name_label.grid(row=1, column=0)
        pwd_label = Label(self, text="密码", font=("Arial"))
        pwd_label.grid(row=2, column=0)
        pwd1_label = Label(self, text="密码确认", font=("Arial"))
        pwd1_label.grid(row=3, column=0)
        e_id = Entry(self)
        e_id.grid(row=0, column=1)
        e_name = Entry(self)
        e_name.grid(row=1, column=1)
        e_pwd = Entry(self, show='*')
        e_pwd.grid(row=2, column=1)
        e_pwd1 = Entry(self, show='*')
        e_pwd1.grid(row=3, column=1)

        b1 = Button(self, text="注册",
                    command=lambda: self.signup_check(e_id.get(), e_name.get(), e_pwd.get(), e_pwd1.get()))
        b1.grid(row=4, column=1)

        b2 = Button(self, text="返回登录", command=lambda: self.back_manage())
        b2.grid(row=4, column=2)

    def back_manage(self):
        self.destroy()
        Manage().show()

    def signup_check(self, e_id, e_name, e_pwd, e_pwd1):
        u = UserManager()
        if e_pwd != e_pwd1:
            messagebox.showwarning('','两次输入密码不一致')
            return
        if u.signup_check(e_id) == True:
            u.save(e_id, e_name, e_pwd)
            messagebox.showinfo('', '用户注册成功')
            self.back_manage()
        else:
            messagebox.showerror('', '工号已存在')

class UserPage(tk.Toplevel):
    '''用户主页'''
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("400x600+100+200")
        # 创建字典：车型和对应的等级列表
        self.cars = [
            "车型1",
            "车型2",
            "车型3",
            "车型4",
            "车型5",
        ]

        self.levels = ["等级1", "等级2", "等级3", "等级4", "等级5"]

        self.car_frame = Frame(self)
        self.noise_frame = Frame(self)
        # wrap=tk.WORD的作用是在单词边界处换行，而不是在字符边界处。
        self.text_box = Text(self.car_frame, wrap=tk.WORD, width=40, height=10)
        self.noise_text = Text(self.noise_frame,wrap=tk.WORD, width=40, height=10)

        self.main()

    def main(self):

        # 创建选择车型和等级的下拉菜单
        car_var = tk.StringVar()
        car_var.set("请选择车型")
        car_option_menu = tk.OptionMenu(self, car_var, *self.cars)

        level_var = tk.StringVar()
        level_var.set("请选择等级")
        level_option_menu = tk.OptionMenu(self, level_var, *self.levels)
        start_button = tk.Button(self, text="启动", command=lambda: self.start(car_var.get(), level_var.get()))




        Label(self.car_frame, text="车辆：").pack()


        noise_button = tk.Button(self.noise_frame, text="记录噪音", command=lambda: self.handle_noise())
        quit_button = tk.Button(self, text="返回主页面", command=lambda: self.back_manage())
        level_option_menu.pack()
        car_option_menu.pack()
        start_button.pack()
        self.car_frame.pack()
        self.text_box.pack(pady=10)
        self.noise_text.pack()
        self.noise_frame.pack(pady=10)


        noise_button.pack()
        quit_button.pack()




    def start(self, selected_car, selected_level):
        if selected_car == "请选择车型" or selected_level == "请选择等级":
            messagebox.showwarning("警告", "请选择车型和等级再启动！")
        else:
            message = f"{selected_car}：{selected_level}"
            self.text_box.config(state=tk.NORMAL)
            # 将文本框设置为可编辑状态，以便后续插入文本。
            self.text_box.insert(tk.END, f"{message}\n")
            # 在文本框末尾（END）插入消息内容。
            self.text_box.config(state=tk.DISABLED)
            # 将文本框设置为只读状态，以防止用户编辑或修改其中的内容。

    def handle_noise(self):
        noise_level = random.randint(0, 100)
        noise_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        noise_info = f"噪音等级：{noise_level}，时间：{noise_time}\n"
        self.noise_text.insert(tk.END, noise_info)


    def back_manage(self):
        self.destroy()
        Manage().show()
        pass

    def hide(self):
        self.withdraw()

    def show(self):
        self.deiconify()

class AdminPage(tk.Toplevel):
    '''管理员主页'''
    def __init__(self, master):
        super().__init__()
        self.title("")
        self.geometry("400x300+100+200")
        u = UserManager()
        self.users = u.users
        self.tree = ttk.Treeview(self)
        self.create_user_list()

    def main(self):
        pass
    def create_user_list(self):

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree["columns"] = ("id", "name", "times", "pwd")
        self.tree.column("#0", width=0, stretch=tk.NO)  # 隐藏默认的第一列
        self.tree.column("id", width=50)
        self.tree.column("name", width=50)
        self.tree.column("times", width=50)
        self.tree.column("pwd", width=50)

        self.tree.heading("id", text="工号")
        self.tree.heading("name", text="姓名")
        self.tree.heading("times", text="工次")
        self.tree.heading("pwd", text="密码")

        for user in self.users:
            self.tree.insert("", tk.END, values=(user["id"], user["name"], user["times"], user["pwd"]))

        self.tree.bind("<ButtonRelease-1>", self.on_click)



    def on_click(self, event):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

        item = self.tree.selection()
        if item:
            edit_frame = tk.Frame(self)
            edit_frame.pack()

            edit_button = tk.Button(edit_frame, text="编辑", command=lambda: self.edit_user(item))
            edit_button.pack(side=tk.LEFT, padx=5)

            delete_button = tk.Button(edit_frame, text="删除", command=lambda: self.delete_user(item))
            delete_button.pack(side=tk.LEFT, padx=5)

            quit_button = tk.Button(edit_frame, text="退出", command=lambda: self.back_manage())
            quit_button.pack(side=tk.LEFT, padx=5)

    def edit_user(self, item):
        user_info = self.tree.item(item, "values")
        print(f"Edit user: {user_info}")

    def delete_user(self, item):
        user_info = self.tree.item(item, "values")
        print(f"Delete user: {user_info}")

    def back_manage(self):
        self.destroy()
        Manage().show()

if __name__ == "__main__":
    app = Manage()
    app.mainloop()