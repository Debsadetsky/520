#pip3 install
from psycopg2 import connect
try:
    con = connect('host = localhost dbname=projeto user=admin password=4linux')
    cur = con.cursor()

except Exception as e:
    print('ERRO: {}'.format(e))
    exit()

cur.execute("select * from produtos;")

print(cur.futchone())

cur.close()
con.close()