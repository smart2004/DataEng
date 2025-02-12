# Пример 1: Apache Spark
# Apache Spark — это мощная платформа для обработки данных, 
# которая поддерживает различные языки программирования, включая Python (через PySpark). 
# Вот пример, который демонстрирует, как использовать Spark для обработки данных.

# Установка PySpark
# Если у вас еще не установлен PySpark, вы можете установить его с помощью pip:

# pip install pyspark
# Пример кода
from pyspark.sql import SparkSession

# Создание SparkSession
spark = SparkSession.builder \
    .appName("Пример Spark") \
    .getOrCreate()

# Создание DataFrame из списка
data = [("Аня", 25, "Москва"),
        ("Борис", 30, "Санкт-Петербург"),
        ("Вера", 22, "Казань")]

columns = ["Имя", "Возраст", "Город"]
df = spark.createDataFrame(data, columns)

# Вывод исходных данных
print("Исходные данные:")
df.show()

# Фильтрация данных
filtered_df = df.filter(df['Возраст'] > 24)
print("Фильтрация по возрасту > 24:")
filtered_df.show()

# Добавление нового столбца
df = df.withColumn("Зарплата", df['Возраст'] * 1000)
print("Добавление нового столбца 'Зарплата':")
df.show()

# Группировка данных
grouped_df = df.groupBy("Город").agg({"Возраст": "avg"})
print("Средний возраст по городам:")
grouped_df.show()

# Завершение работы SparkSession
spark.stop()
