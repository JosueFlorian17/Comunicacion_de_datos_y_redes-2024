class S3Bucket:
    def __init__(self):
         self.buckets = {} # Lista de buckets con los objetos establecidos para cada uno

    def create_bucket(self,name):
         self.buckets[name]={} # Se creará el bucket "name" y será introducido a la lista de buckets con un valor de diccionario para poder asignarle múltiples archivos


    def put_object(self,bucket,key,data):
        if bucket in self.buckets: # Se valida que sea un bucket existente y asignamos al bucket el objeto
            self.buckets[bucket][key]=data
        else:
            return "El bucket seleccionado no existe, creélo primero"

            
    def get_object(self,bucket,key): # Si existe el bucket y objeto, imprimimos su valor 
        print (self.buckets.get(bucket, {}).get(key,None))
            

s3=S3Bucket()

s3.create_bucket("mybucket")
s3.put_object("mybucket","file1.txt","Hello, S3 Bucket!")


s3.put_object("mybucket","file2.txt","VA MOS")

s3.get_object("mybucket","file1.txt")
s3.get_object("mybucket","file2.txt")

s3.create_bucket("newbucket")
s3.put_object("newbucket","archivo.txt","Muy buenas tardes, estoy en newbucket")
s3.get_object("newbucket","archivo.txt")


print(s3.buckets)
