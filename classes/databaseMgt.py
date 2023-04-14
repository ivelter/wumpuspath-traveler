import apsw
import apsw.ext
import os

class DataBase:
    database = None

async def initDB():
    """
    Loads the database and initializes it if it doesn't exist yet.
    """
    i = False
    if not os.path.isfile("data/db"):
        i = True
    DataBase.database = apsw.Connection("data/db")
    #apsw.ext.log_sqlite()
    if i:
        initTables()

def initTables():
    """
    Called when the database is first created. Creates all the necessary tables
    for the bot to function properly.
    """
    getDB().execute("""
    CREATE TABLE Players(
        pid,
        discordid,
        lvl,
        strength,
        currhp,
        maxhp,
        joindate
    );
    """)

def getDB():
    return DataBase.database

def execute(instruction: str):
    """Execute a given SQL instruction on the database.
    Use it with caution as it is vulnerable to SQL injections."""
    getDB().execute(instruction)

def insert(table: str, values: list):
    """
    Executes an insert command with the specified table and values.
    :param table: Table
    :param values: List of values
    """
    query = f"INSERT INTO {table} VALUES ({'?,' * (len(values)-1)}" + "?);"
    getDB().execute(query, values)

def insertnone(table: str, values: dict):
    """
    Executes an insert command with the specified table and values.
    Null values are allowed, contrary to regular insert(str, list).
    :param table: Table
    :param values: Dictionary of attribute names:value
    """
    columns = ""
    for data in values.keys():
        columns += (data + ',')
    columns.removesuffix('')
    query = f"INSERT INTO {table} ({columns}) VALUES ({'?,' * (len(values)-1)}" + "?);"
    getDB().execute(query, [value for value in values.values()])

def sanitizeInput(s: str) -> str:
    """
    Removes quotes from string to prevent injections
    :param s: string to sanitize
    :return: sanitized string
    """
    s.replace('"', "")
    s.replace("'", "")
    return s
