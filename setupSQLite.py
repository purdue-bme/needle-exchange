import sqlite3
import datetime
	def init():
  conn = sqlite3.connect('data.db')
  createTable(conn)
  conn.close()
	def create_table(conn):
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS answers (
      id INTEGER AUTOINCREMENT,
      questionsId INTEGER,
      answer INTEGER,
      createdAt TIMESTAMP
      )''')
  conn.commit()
	def add_new_answer(questionId, answer):
  now = datetime.datetime.now().ctime()
  c = conn.cursor()
  c.execute('''INSERT INTO answers (questionId, answer, createdAt) VALUES (?, ?, ?)''',
      (questionId, answer, now))
  conn.commit()
