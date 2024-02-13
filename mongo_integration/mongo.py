import datetime
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://gusprado:uSAK2HE9C2bftfVk@atlas-test.8xzpaox.mongodb.net/")


db = client.test
"""
test connection
collection = db.test_collection
print(collection)
"""

cliente1 = {
    "nome": "Gustavo",
    "cpf ": "990887400",
    "endereco": "Rua dos bobos no. 0",
    "conta": {
        "tipo": "corrente", 
        "agencia": "0001",
        "numero": 1234,
        "saldo": 100
    },
    "created_at": datetime.datetime.utcnow()
}

cliente2 = {
    "nome": "Michael",
    "cpf" :"008768912",
    "endereco": "Rua dos bobos no. 100",
    "conta": {
        "tipo": "poupanca",
        "agencia": "0001",
        "numero": 3344,
        "saldo": 500
    },
    "created_at": datetime.datetime.utcnow()
}

cliente = db.cliente

# Persist on DB
#cliente.insert_many([cliente1, cliente2])

document_count = db.cliente.count_documents({})

print(f"Quantidade de registros: {document_count}\n")

for client in db.cliente.find({}):
    print(client)

