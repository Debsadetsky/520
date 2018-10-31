from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
from bson import ObjectId

try:
    con = MongoClient()
    db = con['projeto'] #objeto que opera o banco de dados -> que recebe o cursor do banco de dados
    #chamo de db para ficar igual ao do mongo
except Exception as e:
    print('Erro: {}'.format(e))

usuarios = [] #nome da minha lista

for usuario in db.usuarios.find(): #usuario -> nome do item da minha lista
    usuarios.append(usuario)
#ou
#usuarios = [x for x in db.usuarios.find()] 
#faço uma cópia do cursor, mas ele deixará de ser um cursor e será uma lista

#cada elemento da lista é um dicionario

print(db.usuarios.find_one()) #traz o primeiro registro que ele encontra
print(db.usuarios.find())
pprint(usuarios) #printa mais bonito
#db.usuarios.remove({"_id":1})#remove dados do banco de dados
#db.usuarios.insert({"_id":1, "nome":"deborah", "sobrenome":"sadetsky"})#insere dados no banco de dados
#db.usuarios.update({"_id":1},{"$set":{"nome":'zé'}})#atualiza dados do banco de dados
#date = {"_id":4, "nome":"carla", "sobrenome":"sadetsky"}
#date1 = {"_id":5, "nome":"ari", "sobrenome":"sadetsky", 'hora': datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
#db.usuarios.insert(date)
#db.usuarios.insert(date1)
#pprint(usuarios)
db.usuarios.remove({"_id":ObjectId('0x7f810db86438')})