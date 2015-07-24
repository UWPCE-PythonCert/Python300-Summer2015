import os
import sqlite3
from utils import show_table_metadata

DB_FILENAME = 'book.db'
SCHEMA_FILENAME = 'ddl.sql'
DB_IS_NEW = not os.path.exists(DB_FILENAME)

def main():
    with sqlite3.connect(DB_FILENAME) as conn:
        #conn =  sqlite3.connect(DB_FILENAME)
        if DB_IS_NEW:
            print 'Creating schema'
            with open(SCHEMA_FILENAME, 'rt') as f:
                schema = f.read()
                conn.executescript(schema)
        else:
            print "Database exists, introspecting:"
            tablenames = ['author', 'book']
            cursor = conn.cursor()
            for name in tablenames:
                print "\n"
                show_table_metadata(cursor, name)
        #conn.close()

if __name__ == '__main__':
    main()
