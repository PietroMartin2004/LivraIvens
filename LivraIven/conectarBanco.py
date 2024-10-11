import pymongo

def conectar_banco():
    import pymongo
    return pymongo.MongoClient("mongodb+srv://PMART:Ivens3560@pmart.xnmtt.mongodb.net/")