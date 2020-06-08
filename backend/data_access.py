import psycopg2

def connect_to_db():
    conn = psycopg2.connect("host=host.docker.internal dbname=cloud_reminders user=postgresadmin password=admin123 port=32420")
    return conn

def close_db_conn(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

def insert(data):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO task (description, urgency, status) VALUES ('"  + data[0] + "',"  + data[1]  + ",'" + data[2] + "');")
    close_db_conn(conn, cur)

def delete(task_id):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM task WHERE task_id = " + task_id + ";")
    close_db_conn(conn, cur)

def select_all():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM task")
    return cur.fetchall()


