import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                host="176.123.160.78",
                password="kWOWtIb_",
                port="5432"
            )  
            self.cursor = self.conn.cursor()
            print("Подключение к базе данных успешно!")
        except Exception as e:
            print(f"Ошибка подключения: {e}")

# Пример использования
if __name__ == "__main__":
    db = Database()

    # Данные для добавления
    table_name = 'something'
    something_data = {
        'name': 'Пример',
        'description': 'Это пример описания.'
    }

    # Формирование SQL-запроса для добавления данных
    columns = something_data.keys()
    values = [something_data[column] for column in columns]
    
    insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
        sql.Identifier(table_name),
        sql.SQL(', ').join(map(sql.Identifier, columns)),
        sql.SQL(', ').join(sql.Placeholder() * len(values))
    )

    try:
        db.cursor.execute(insert_query, values)
        db.conn.commit()
        print("Данные успешно добавлены!")
    except Exception as e:
        print(f"Ошибка при добавлении данных: {e}")
        db.conn.rollback()

    # Закрытие соединения
    db.cursor.close()
    db.conn.close()
    print("Соединение с базой данных закрыто.")