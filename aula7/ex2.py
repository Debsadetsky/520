#sudo systemctl start postgresql
#sudo su
#su - postgres
#psql
#create user admin password '4linux';
#create database projeto
#owner admin;
#\q
#sair
#exit
#psql -h localhost -U admin projeto
#projeto=> create table produtos(id serial primary key, nome varchar(50), preco money, quantidade smallint);
#pip3 install psycopg2-binary

from psycopg2 import connect

try:
    con = connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con.cursor()

except Exception as e:
    print('ERRO:{}'.format(e))
    exit()

produto = input('Digite o nome do produto! ')
preco = input('Quanto vai custar? ')
qtd = int(input('Quantos produtos? '))
cur.execute("insert into produtos (nome, preco, quantidade)\
    values('{}', '{}', {})".format(produto, preco, qtd))

con.commit()
cur.execute("select * from produtos where preco between '5' and '200';")

print(cur.fetcho

con.close()