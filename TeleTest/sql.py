import sqlite3

class SQLite:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_list(self, user_id):

        with self.connection:
            return self.cursor.execute("SELECT * FROM `MyTable` WHERE `id_user` = ?", (user_id,)).fetchall()

    def add_list(self, user_id, text):

        with self.connection:
            return self.cursor.execute("INSERT INTO `MyTable` (`id_user`, `list`) VALUES(?,?)", (user_id, text))

    def delete_list(self, id, user_id):

        with self.connection:
            c=self.get_list(user_id)
            print(c)
            if(len(c)>id):
                return
            return self.cursor.execute("DELETE FROM MyTable WHERE id= ?", (c[id-1][0],))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()