import sqlite3
import os
from features import helper_methods, blocking_operations

user_name = os.getlogin()
db_directory = os.path.join('C:\\Users', user_name,
                            'AppData', 'Local', 'SurfSentry')
db_path = os.path.join(db_directory, 'surfsentry_db.db')
os.makedirs(db_directory, exist_ok=True)


def create_db():
    """
    Creates a SQLite database if it doesn't exist.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS malicious_data (
                    id INTEGER PRIMARY KEY,
                    data_id TEXT,
                    data_type TEXT,
                    address TEXT UNIQUE,
                    mal_type TEXT,
                    desc TEXT,
                    severity INTEGER,
                    source TEXT,
                    data_date TEXT,
                    current_status TEXT,
                    operation_time TEXT,
                    update_date TEXT,
                    link TEXT 
                )
            ''')
    except sqlite3.Error as e:
        print(f"Error create_db: {e}")


def save_to_table(entry):
    """
    Saves data to the malicious_data table in the database.
    """

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO malicious_data 
                (data_id, data_type, address, mal_type, desc, severity, source, data_date, current_status, operation_time, update_date, link)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                entry['data_id'], entry['data_type'], entry['address'], entry['mal_type'],
                entry['desc'], entry['severity'], entry['source'],
                entry['data_date'], entry['current_status'], entry['op_time'], entry['update_date'], entry['link']
            ))

    except sqlite3.Error as e:
        print(f"Error save_to_table: {e}")
        return None


def update_entry_status(address, new_status, op_time):
    """
    Update the malicious_data table entry.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE malicious_data SET current_status=?,operation_time=? WHERE address=?", (new_status, op_time, address))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error update_entry_status: {e}")


def get_last_entry_date():
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT data_date FROM malicious_data ORDER BY data_id DESC LIMIT 1')
            entry = cursor.fetchone()
            return entry
    except sqlite3.Error as e:
        print(f"Error get_last_entry_date: {e}")
        return None


def get_data_by_specified_condition(column_name, condition_column, condition_value):
    """
    Retrieves data from the malicious_data table by a specific column and condition.
    """
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(f"SELECT {column_name} FROM malicious_data WHERE {
                       condition_column} = ?", (condition_value,))
        data = cursor.fetchall()
        if data:
            data_dict = [dict(row) for row in data]
            return data_dict
    except sqlite3.Error as e:
        print(f"Error get_data_by_specified_condition: {e}")
        return None
    finally:
        conn.close()


def get_data_by_column_name(column_name):
    """
    Retrieves data from the malicious_data table by a specific column.
    """
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(f"SELECT {column_name} FROM malicious_data")
        data = cursor.fetchall()
        if data:
            data_dict = [dict(row) for row in data]
            return data_dict
    except sqlite3.Error as e:
        print(f"Error get_data_by_column_name: {e}")
        return None
    finally:
        conn.close()


def get_entry_details(column_name, address):
    """
    Retrieves data from the specified table by a specific condition.
    """
    try:

        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT {column_name} FROM malicious_data WHERE address = ?", (address,))

        entry = cursor.fetchone()
        if entry:
            entry_dict = dict(entry)
            return entry_dict
    except sqlite3.Error as e:
        print(f"Error get_entry_details: {e}")
        return None
    finally:
        conn.close()


def remove_entry(address):
    """
    Remove the malicious_data table entry.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"DELETE FROM malicious_data WHERE address = ?", (address,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error remove_entry: {e}")


def clear_table():
    """
    Clears all records from the malicious_data table.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM malicious_data")
    except sqlite3.Error as e:
        print(f"Error clear_table: {e}")


def drop_table():
    """
    Drops the malicious_data table if it exists.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS malicious_data")
    except sqlite3.Error as e:
        print(f"Error drop_table: {e}")


def check_address_exists(address):
    """
    Checks if the given address already exists in the database.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM malicious_data WHERE address = ?", (address,))
            count = cursor.fetchone()[0]
            if count > 0:
                return True
            else:
                return False
    except sqlite3.Error as e:
        print(f"Error check_address_exists: {e}")
        return None


def clear_old_data():
    """
    Clears the outdated data that doesn't match today's date in the database..
    """
    today = helper_methods.get_current_date_utc().split()[0]
    data = get_data_by_specified_condition(
        column_name='address,data_date',
        condition_column='source',
        condition_value='"USOM"')

    if data:
        for entry in data:
            address = entry['address']
            entry_date = entry['data_date']
            
            if entry_date.split()[0] != today:
                blocking_operations.manage_entry(
                    entry=entry, operation='remove')
                remove_entry(address=address)


def custom_query(query):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f'{query}')
            data = cursor.fetchall()
            return data
    except sqlite3.Error as e:
        print(f"Error custom_query: {e}")
        return None
