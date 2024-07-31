import sys
import sqlite3

conn = None

try:
    conn = sqlite3.connect('spam.db')
except sqlite3.DatabaseError as err:
    print(err)
    sys.exit()
else:
    result = conn.execute("select 5")
finally:  # whether or not an error was raised
    if conn:
        conn.close()
