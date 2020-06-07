import psycopg2

def connect_to_db():
    conn = psycopg2.connect("host=host.docker.internal dbname=cloud_reminders user=postgresadmin password=admin123 port=32420")
    return conn

def insert(data):
    conn = connect_to_db()
    cur = conn.cursor()
    print(data[0])
    print(data[1])
    print(data[2])
    cur.execute("INSERT INTO task (description, urgency, status) VALUES ('"  + data[0] + "',"  + data[1]  + ",'" + data[2] + "');")
    conn.commit()
    cur.close()
    conn.close()

