class Database:
    def __init__(self,data):
        self.data=data


def CRUD(inpu, db):
    if inpu.upper() == "C":
        crear = input("Ingrese su información: ")
        
        if crear in db.data or int(crear) in db.data:
            print("Ya se encuentra")
        else:
            db.data.append(crear)
            print(db.data)
        
    if inpu.upper()=="R":
        leer=input("ingrese su información: ")
        if leer in db.data or int(leer) in db.data:
            print(f"{leer} se encuentra en la base de datos")
        else:
            print(f"{leer} no se encuentra")
        
    if inpu.upper()=="U":
        actualizar=int(input("ingrese su información: "))
        nuevo=int(input("ingrese nuevo valor: "))
        if actualizar in db.data or int(actualizar) in db.data:
            index = db.data.index(actualizar)
            db.data[index] = nuevo
            print(f"{actualizar} se ha cambiado por {nuevo}")
            print(db.data)
        else:
            print(f"{actualizar} no se encuentra")
        
    if inpu.upper()=="D":
        delete=int(input("ingrese su información: "))
        db.data.remove(delete)
        print(db.data)


db = Database([1, 2, 3, 4, 5, 6, 7, 8, 9])
CRUD("D", db)
