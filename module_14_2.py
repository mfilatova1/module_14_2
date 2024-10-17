import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor=connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', f'{i*10}', "1000"))
#
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "User1"))
#
# for i in range(1, 11):
#     if i % 2 != 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f'User{i + 2}'))
#
#
# cursor.execute("DELETE FROM Users WHERE id IN (1, 4, 7, 10)")
#
# cursor.execute("SELECT id, username, email, age, balance FROM Users WHERE age != ?", (60,))
#
# for user in cursor.fetchall():
#     print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

cursor.execute("DELETE FROM Users WHERE id = ?", ("6", ))
cursor.execute("SELECT COUNT(*) FROM Users")
#total1 = cursor.fetchone()[0]
#print(total1)
cursor.execute("SELECT SUM(balance) FROM Users")
#total2 = cursor.fetchone()[0]
#print(total2)
cursor.execute("SELECT AVG(balance) FROM Users")
total3 = cursor.fetchone()[0]
print(total3)

connection.commit()
connection.close()