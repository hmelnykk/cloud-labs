import pymysql

conn = pymysql.connect(
    host="database-for-labs.mysql.database.azure.com",
    user="hmelnykk@database-for-labs",
    password="password",
    database="test",
    ssl={
        "cert_reqs": 0,       # Disable certificate verification
        "check_hostname": False
    }
)

cursor = conn.cursor()
cursor.execute("SELECT 1;")
print(cursor.fetchone())
conn.close()
