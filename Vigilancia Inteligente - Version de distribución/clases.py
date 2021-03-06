from ast import Del
from datetime import datetime
from mailbox import NoSuchMailboxError
from cv2 import resize
from torch.hub import load
from Alert import SaveImage, telegram_msj


from vidgear.gears import CamGear

class camara():
    def __init__(self, nombre, source):
        self.nombre = nombre
        self.source = source
        self.estado = 0
    
    def getDatos(self):
        print(f"Nombre: {self.nombre} \n")

    def prenderCamara(self):
        if self.estado == 0:
            options = {'THREADED_QUEUE_MODE': False}
            CamGear(source=f'{self.source}',**options).start()
            print(f"Camara {self.nombre} encendida")
            self.estado=1
        #else:
            #print(f"La camara {self.nombre} ya estaba encendida")

        

    def leerCamara(self):
        options = {'THREADED_QUEUE_MODE': False}
        frames=CamGear(source=f'{self.source}',**options).read()
        print("la camara esta leyendo los datos")
        return frames

    def detect(self, telefonos):

        model= load('ultralytics/yolov5', 'yolov5s6')# modelo

        #configuración del modelo
        model.conf = 0.75#confidence threshold (0-1)
        model.classes= [0]# detección de personas

        #cap=f.active_cam()
        frame=self.leerCamara()
        print("la camara esta leyendo los datos")
        if None is frame:
            frame=self.leerCamara()
        else:
            img= resize(self ,(0,0),fx=0.3,fy=0.3)
            texto= self.nombre
            result= model(img)
            result.render() 
            labels = result.xyxyn[0][:, -1].cpu().numpy()
                
            if (labels.all()==0):
                print(texto)
                img_path= SaveImage(img)
                t=str(self)
                for tel in range(len(telefonos)):
                    telegram_msj(telefonos[tel].numero,t,img_path)

    def apagarCamara(self):
        if self.estado==1:
            options = {'THREADED_QUEUE_MODE': False}
            CamGear(source=f'{self.source}',**options).stop()
            print(f"Camara {self.nombre} apagada")
        else:
            print(f"La camara {self.nombre} ya estaba apagada")
        



class telefono():
    def __init__(self, numero, nombre, chatid):
        self.numero = numero
        self.nombre = nombre
        self.chatid = chatid
    
    def getDatos(self):
        print(f"Numero: {self.numero} \n")
        print(f"Nombre: {self.nombre} \n")
        print(f"Chat ID: {self.chatid} \n")

camaras=[]
telefonos=[]

def agregarCamara():
    print("Ingresar nombre de la camara:")
    nombre = input()
    print("Ingresar source de la camara:")
    source = input()
    camaras.append(camara(nombre,source))

def eliminarCamara():
    print("Ingresar nombre de la camara ha eliminar:")
    nombre = input()
    for i in range(len(camaras)):
        if camaras[i].nombre==nombre:
            del camaras[i]
            print("camara eliminada")
            break


def agregarTel():
    print("Ingresar numero de telefono:")
    numerotel = input()
    print("Ingresar nombre de la persona:")
    nombretel = input()
    telefonos.append(camara(numerotel,nombretel))

'''agregarCamara()
agregarCamara()

for i in range(len(camaras)):
    camaras[i].getDatos()
    #camaras[i].prenderCamara()

#eliminarCamara()

for i in range(len(camaras)):
    camaras[i].getDatos()
    camaras[i].apagarCamara()

for i in range(len(camaras)):
    camaras[i].detect()'''
