import json
import zipfile
import os

api_token = {"username":"leonel19","key":"10906b559a984915e3510922e9bfc99f"}

##Conectar a kaggle
with open('C:/Users/Putin/.kaggle/kaggle.json','w') as file:
	json.dump(api_token,file)

location = "C:/Users/Putin/Documents/Proyecto_parcial/dataset"

##Validaciones

if not os.path.exists(location):

	os.nkdir(location)

else:
	for root, dirs, files in os.walk(location, topdown=False):
		for name in files:
			os.remove(os.path.join(root,name)) ##elimina todos los archivos
		for name in dirs:
			os.rmdir(os.path.join(root,name)) ##elimina todas las carpetas

##Descargar dataset de kaggle

os.system("kaggle datasets download -d henryshan/starbucks -p C:/Users/Putin/Documents/proyecto_parcial/dataset")

##Descomprimir el archivo de kaggle
os.chdir(location)
for file in os.listdir():
	zip_ref = zipfile.ZipFile(file,"r") ##Lee archivo .zip
	zip_ref.extractall() ##extrae contenido del archivo .zip
	zip_ref.close() ##cierra el archivo