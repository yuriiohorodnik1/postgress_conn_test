import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server"""
    conn = None
    try:
        #read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print("Connecting to the database")
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement VERSION
        cur.execute(query="SELECT version();")

        # display the PostgreSQL version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PosgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("DB connection closed")


if __name__ == "__main__":
    connect()
