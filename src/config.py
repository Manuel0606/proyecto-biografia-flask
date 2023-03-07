from pymongo import MongoClient
import certifi

mongo = 'mongodb+srv://manuel:admin@cluster0.yzc2dr9.mongodb.net/?retryWrites=true&w=majority'
certificado = certifi.where()

def Conexion():
    try:
        client = MongoClient(mongo, tlsCAFile=certificado)
        db = client['bd_usuarios']
    except ConnectionError:
        print('Error de conexión')
    
    return db

