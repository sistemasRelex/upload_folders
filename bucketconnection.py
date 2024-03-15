from google.cloud import storage
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'celestial-now-314016-ffdcf4598d13.json'

client = storage.Client()


def connect_to_bucket():

    # Crea una instancia del cliente de Storage
    client = storage.Client()

    # Especifica tu ID de proyecto de GCP y el nombre del bucket
    project_id = 'celestial-now-314016'
    bucket_name = 'digitizer-ftp-files'

    try:
        # Obtiene el bucket
        bucket = client.get_bucket(bucket_name)
        print(f"Conexión exitosa al bucket '{bucket_name}' en el proyecto '{project_id}'")
        return bucket
    except Exception as e:
        print(f"No se pudo conectar al bucket: {e}")
        return None



# Conecta al bucket
bucket = connect_to_bucket()

# Si la conexión es exitosa, puedes realizar operaciones en el bucket
if bucket:
    # Por ejemplo, lista los blobs (objetos) dentro del bucket
    blobs = bucket.list_blobs(max_results=10)
    print("Contenido del bucket:")
    for blob in blobs:
        print(f"- {blob.name}")

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False


for root, dirs, files in os.walk("./boxes-to-upload", True):
   for name in files:
           ruta = root + "/" + name
           ruta = ruta.replace("\\" , "/").strip("./")
           
           print(ruta)
           print(name)
           file_path = rf"C:/Users/PC/Documents/RELEX/DIGITALIZADOR/Bucket/{ruta}"
           upload_to_bucket(f'{ruta}', f'{file_path}', 'digitizer-ftp-files')
