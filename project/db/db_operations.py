import sqlite3
from features.methods import get_current_date

def create_specified_table(table_name):
    """
    Creates a SQLite database if it doesn't exist, along with the specified table.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            if table_name == "malicious_data":
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS malicious_data (
                        id INTEGER PRIMARY KEY,
                        data_id INTEGER,
                        data_type TEXT,
                        url TEXT,
                        resolved_ip TEXT,
                        type TEXT,
                        desc TEXT,
                        criticality_level INTEGER,
                        source TEXT,
                        date TEXT,
                        link TEXT
                    )
                ''')
            elif table_name == "fw_rules":
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS fw_rules (
                    id INTEGER PRIMARY KEY,
                    url TEXT,
                    resolved_ip TEXT,
                    operation_time TEXT,
                    current_status TEXT
                )
            ''')
    except sqlite3.Error as e:
        print(f"Error: {e}")

def save_to_specified_table(data,table_name):
    """
    Saves data to the specified table in the database.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            for item in data['items']:
                if table_name == "malicious_data":
                    cursor.execute('''
                        INSERT INTO malicious_data 
                        (data_id, data_type, url, resolved_ip, type, desc, criticality_level, source, date, link)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        item['data_id'] , item['data_type'], item['url'], item['resolved_ip'], item['type'], 
                        item['desc'], item['criticality_level'], item['source'], 
                        item['date'], item['link']
                    ))
                else:
                    cursor.execute('''
                        INSERT INTO fw_rules 
                        (resolved_ip, url, operation_time, current_status)
                        VALUES (?, ?, ?, ?)
                    ''', (
                        item['resolved_ip'], item['url'], item['operation_time'], item['current_status']
                    ))
    except sqlite3.Error as e:
        print(f"Error: {e}")

def get_data_by_column_name(column_name,table_name):
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
        print(f"Error: {e}")
        return None

def get_one_data_detail_from_specified_table(column_name, condition_column, condition_value,table_name):
    """
    Retrieves data from the specified table by a specific condition.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT {column_name} FROM {table_name} WHERE {condition_column} = ?', (condition_value,))
            data = cursor.fetchone()
            return data
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None

def clear_table_by_table_name(table_name):
    """
    Clears all records from the specified table.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM {table_name}')
    except sqlite3.Error as e:
        print(f"Error: {e}")

def drop_table(table_name):
    """
    Drops the specified table if it exists.
    """
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    except sqlite3.Error as e:
        print(f"Error: {e}")


def update_fw_rule(url, new_status):
    try:
        with sqlite3.connect('project/db/surfsentry_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fw_rules WHERE url=?", (url,))
            data = cursor.fetchone()
            if data:
                today = get_current_date()
                cursor.execute("UPDATE fw_rules SET current_status=?,operation_time=? WHERE id=?", (new_status, today, data[0]))
                conn.commit()
                
            else:
                print(f"URL does not exist: {url}")
    except sqlite3.Error as e:
        print(f"Error: {e}")