

def check_file_data():
    try:
        lst_user_file = open("user_data.ubank", "r", encoding="utf-8")
        lst_user = lst_user_file.readlines()
        lst_user_file.close()
    except FileNotFoundError:
        lst_user_file = open("user_data.ubank", "w", encoding="utf-8")
        lst_user_file.close()


check_file_data()


def get_user_list():
    user_list = open("user_data.ubank", "r", encoding="utf-8").readlines()
    user_list = [e.replace("\n","") for e in user_list]

    return user_list


def check_user_exist(iban):
    lst_user = get_user_list()

    if iban not in lst_user:
        return True
    else:
        return False


def add_new_user(data):

    if check_user_exist(data) is True:
        open("user_data.ubank", "a", encoding="utf-8").write(str(data)+"\n")
        print("new account added")
    else:
        print("user exsit")

