import sqlite3

# Подключение к базе данных (или создание новой)
conn = sqlite3.connect('tables_creation.db')

# Создание курсора для выполнения запросов
cursor = conn.cursor()

# Пример выполнения SQL-кода

# Создание таблиц
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department_id INTEGER,
    salary REAL
);
""")

# Вставка данных
cursor.execute("INSERT INTO departments (department_name) VALUES (?), (?), (?);", 
                ('HR', 'Engineering', 'Sales'))

cursor.execute("INSERT INTO employees (name, department_id, salary) VALUES (?, ?, ?);", 
                ('Alice', 1, 60000))

cursor.execute("INSERT INTO employees (name, department_id, salary) VALUES (?, ?, ?);", 
                ('Bob', 2, 80000))

cursor.execute("INSERT INTO employees (name, department_id, salary) VALUES (?, ?, ?);", 
                ('Charlie', 2, 75000))

cursor.execute("INSERT INTO employees (name, department_id, salary) VALUES (?, ?, ?);", 
                ('David', 3, 50000))

# Сохранение изменений
conn.commit()

# Вып
