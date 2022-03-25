import sqlite3

con = sqlite3.connect("Users_info.sqlite")
cur = con.cursor()
result = cur.execute("""SELECT join_in FROM auth""").fetchall()


def join_in_account(login, password):
    global result
    # account cycle
    for i in result:
        login_in_db = i[0].split()[0]
        password_in_db = i[0].split()[1]
        if login_in_db == login and password_in_db == password:
            return 'Success!'
    return 'Bad password or login'


def registration(login, password):
    global result
    # account cycle
    for i in result:
        login_in_db = i[0].split()[0]
        if login_in_db == login:
            return 'Such a profile has already been registered'
    cur.execute('INSERT INTO auth(join_in) VALUES(?)', (str(login + ' ' + password),))
    con.commit()
    return 'Success!'


def edit_profile(id):
    """changing login details"""


def delete_profile(id):
    """deleting an account"""


def clear(table):
    """func for developers"""


print(registration(input(), input()))
