import sqlite3


def create_tables():
    """
    Creates a SQLite database if it doesn't exist, along with the specified table.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS malicious_data (
                    id INTEGER PRIMARY KEY,
                    data_id INTEGER,
                    data_type TEXT,
                    url TEXT,
                    mal_type TEXT,
                    desc TEXT,
                    criticality_level INTEGER,
                    source TEXT,
                    date TEXT,
                    link TEXT
                )
            ''')
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS blocked_data (
                id INTEGER PRIMARY KEY,
                url TEXT,
                data_type TEXT,
                operation_time TEXT,
                current_status TEXT
            )
        ''')
    except sqlite3.Error as e:
        print(f"Error create_tables: {e}")


def save_to_mal_table(item):
    """
    Saves data to the malicious_data table in the database.
    """

    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO malicious_data 
                (data_id, data_type, url, mal_type, desc, criticality_level, source, date, link)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                item['data_id'], item['data_type'], item['url'], item['mal_type'],
                item['desc'], item['criticality_level'], item['source'],
                item['date'], item['link']
            ))

    except sqlite3.Error as e:
        print(f"Error save_to_mal_data_table: {e}")


def save_to_blocked_table(item,op_time):
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO blocked_data 
                (url, data_type, operation_time, current_status)
                VALUES (?, ?, ?, ?)
            ''', (
                item['url'], item['data_type'], op_time, "unblocked"
            ))
    except sqlite3.Error as e:
        print(f"Error save_to_blocked_table: {e}")


def get_data_by_column_name(column_name, table_name):
    """
    Retrieves data from the specified table by a specific column.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT {column_name} FROM {table_name}')
            data = cursor.fetchall()
            return data
    except sqlite3.Error as e:
        print(f"Error get_data_by_column_name: {e}")
        return None


def get_one_data_detail(column_name, condition_column, condition_value, table_name):
    """
    Retrieves data from the specified table by a specific condition.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT {column_name} FROM {table_name} WHERE {
                           condition_column} = ?', (condition_value,))
            data = cursor.fetchone()
            return data
    except sqlite3.Error as e:
        print(f"Error get_one_data_detail: {e}")
        return None


def clear_table_by_table_name(table_name):
    """
    Clears all records from the specified table.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            if table_name == 'malicious_data':
                cursor.execute(f'DELETE FROM malicious_data')
            elif table_name == 'blocked_data':
                cursor.execute(f'DELETE FROM blocked_data')
    except sqlite3.Error as e:
        print(f"Error clear_tables: {e}")


def drop_table(table_name):
    """
    Drops the specified table if it exists.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    except sqlite3.Error as e:
        print(f"Error drop_table: {e}")


def update_blocked_table(url, new_status,op_time):
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM blocked_data WHERE url=?", (url,))
            data = cursor.fetchone()
            if data:
                cursor.execute(
                    "UPDATE blocked_data SET current_status=?,operation_time=? WHERE id=?", (new_status, op_time, data[0]))
                conn.commit()

            else:
                print(f"URL does not exist: {url}")
    except sqlite3.Error as e:
        print(f"Error update_blocked_table: {e}")


def custom_query(query):
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f'{query}')
            data = cursor.fetchall()
            return data
    except sqlite3.Error as e:
        print(f"Error custom_query: {e}")
        return None
    
# clear_table_by_table_name("blocked_data")
# clear_table_by_table_name("malicious_data")
# drop_table("malicious_data")
# drop_table("blocked_data")
# create_tables()