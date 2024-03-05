import psycopg2

def connexionPSQL(database:str, host:str, user:str, pwd:str, port:str):
    conn = psycopg2.connect(database=database, host=host, user=user, password=pwd, port=port)
    print('status:', conn.status)
    return conn