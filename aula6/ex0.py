#sudo apt-get update
#sudo apt-get install mongodb
#sudo systemctl start mongodb
#ss -ntlp
#mongo
#systemctl stop postgresql
#systemctl stop mysql
#systemctl stop apache2
#systemctl stop jenkins
#show dbs
#use (nome da base de dados)
#show tables
#db.usuarios.insert({_id:1, nome:'deborah', sobrenome:'sadetsky'}) -> estou add dados na base
#db.usuarios.find() #acha os dados, se vc especificar acha o dado especifico
#db.usuarios.find().pretty() #formata a saida pra ficar bonito de ver
#db.usuarios.insert({_id:2, nome:'ariel', sobrenome:'sadetsky'}) -> estou add dados na base
#db.usuarios.insert({_id:3, nome:'michel', sobrenome:'sadetsky'}) -> estou add dados na base
#db.usuarios.remove({_id:3}) #remove o dado selecionado
#db.usuarios.update({_id:1}, {nome:'zé'}) #modifica todo os dados do _id1
#db.usuarios.update({_id:1}, {$set:{nome:'zé'}}) #modifica só o nome do _id1
#pip3 install pymongo #modulo que faz conexao com o mongoDb