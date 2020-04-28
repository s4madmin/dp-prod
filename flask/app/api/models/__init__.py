import psycopg2
import os

# ----------------------------------------------------------
# Private functions
# ----------------------------------------------------------
def _runSql(sql, data=None, type="select", printSql=False):
    """Run sql statement.

    Example:
    > result = _runSql("select * from users where email=%s", (email,))
    > [('jarnyc@unimelb.edu.au', 'dofdlfjlejjce', 'admin')]

    data should be a tuple, even if one element.
    type should be one of {"select","update"}

    Returns a list of tuples corresponding to the columns of the selection if type=="select".
    If type=="update", returns the number of rows affected by the update.

    If printSql is True, then the actual sql being executed will be printed
    """
    
    postgres_username = os.environ["POSTGRES_USERNAME"]
    postgres_password = os.environ["POSTGRES_PASSWORD"]
    postgres_database_name = os.environ["POSTGRES_DATABASE_NAME"]
    postgres_port = os.environ["POSTGRES_PORT"]
    postgres_uri = os.environ["PSQL_URI"]
    conn = psycopg2.connect(postgres_uri)
    cursor = conn.cursor()
    mongo_uri = os.environ["MONGO_URI"]

    if printSql:  # To see the actual sql executed, use mogrify:
        print(cursor.mogrify(sql, data))
        
    cursor.execute(sql, data)

    if type=="select":
        result = cursor.fetchall()
    elif type=="update":
        result = cursor.rowcount
        conn.commit()  # doesn't update the database permanently without this

    cursor.close()
    conn.close()
    return result

# ----------------------------------------------------------
# Useful for defining a class property
# ----------------------------------------------------------
class classproperty(object):
    
    def __init__(self, f):
        self.f = classmethod(f)
    def __get__(self, *a):
        return self.f.__get__(*a)()