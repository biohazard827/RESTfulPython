from .dbHelper import dbHelper

class User:
    def __init__(self, userId=None, username=None, password=None, firstname=None, lastname=None, grade=None, dateOfBirth=None, lastLogin=None, enabled=None):
        self.userId = userId
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade
        self.dateOfBirth = dateOfBirth
        self.lastLogin = lastLogin
        self.enabled = enabled

    def __str__(self):
        return f"{self.userId}, {self.username}, {self.password}, {self.firstname}, {self.lastName}, {self.grade}, {self.dateOfBirth}, {self.lastLogin}, {self.enabled}"

    def add_user(self, user):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Users (Username, Password, FirstName, LastName, Grade, DateOfBirth, LastLogin, Enabled) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (user.username, user.password, user.firstname, user.lastname, user.grade, user.dateOfBirth, user.lastLogin, user.enabled))
            conn.commit()

    def get_user(self, username):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
            row = cursor.fetchone()
            if row is not None:
                self.userId = row.UserId
                self.username = row.Username
                self.password = row.Password
                self.firstname = row.FirstName
                self.lastName = row.LastName
                self.grade = row.Grade
                self.dateOfBirth = row.DateOfBirth
                self.lastLogin = row.LastLogin
                self.enabled = row.Enabled
            else: return None

    def get_userById(self, userId):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE userId = ?", (userId,))
            row = cursor.fetchone()
            if row is not None:
                self.userId = row.UserId
                self.username = row.Username
                self.password = row.Password
                self.firstname = row.FirstName
                self.lastName = row.LastName
                self.grade = row.Grade
                self.dateOfBirth = row.DateOfBirth
                self.lastLogin = row.LastLogin
                self.enabled = row.Enabled
            else: return None


    def json(self):
        return {
            'userId': self.userId,
            'username': self.username,
            'password': self.password,
            'firstname': self.firstname,
            'lastName': self.lastName,
            'grade': self.grade,
            'dateOfBirth': self.dateOfBirth,
            'lastLogin': self.lastLogin,
            'enabled': self.enabled
        }
    
    def update_user(self, user, userId):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Users SET Username = ?, Password = ?, FirstName = ?, LastName = ?, Grade = ?, DateOfBirth = ?, LastLogin = ?, Enabled = ? WHERE UserId = ?", (user.username, user.password, user.firstname, user.lastname, user.grade, user.dateOfBirth, user.lastLogin, user.enabled, userId))
            conn.commit()
    
    def delete_user(self, userId):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Users WHERE UserId = ?", (userId))
            conn.commit()

    def disable_user(self, userId):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Users SET Enabled = 0 WHERE UserId = ?", (userId))
            conn.commit()

    def enable_user(self, userId):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Users SET Enabled = 1 WHERE UserId = ?", (userId))
            conn.commit()

    def update_login(self, userId):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Users SET LastLogin = CONVERT(VARCHAR, GETDATE(), 22) WHERE UserId = ?", (userId))
            conn.commit()

    def get_all_users(self):
        return self.users.values()