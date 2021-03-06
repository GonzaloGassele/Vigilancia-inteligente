from vidgear.gears import CamGear
from pandas import DataFrame

options = {'THREADED_QUEUE_MODE': False}

def active_cam():
    cap=[[0,1,0],[1,1,0],[2,1,0],[3,1,0],[4,1,0],[5,1,0],[6,1,0],[7,1,0]]
    cap[0][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.103.149/cgi-bin/main.cgi',**options,backend= 'cv2.CAP_FFMPEG ').start()# Galpon motos
    cap[1][1]=CamGear(source='rtsp://contralor:Villegas555@100.100.34.179/cgi-bin/main.cgi',**options,backend= 'cv2.CAP_FFMPEG ').start()# Polo lateral
    cap[2][1]=CamGear(source='rtsp://contralor:Villegas555@100.100.34.183/cgi-bin/main.cgi',**options,backend= 'cv2.CAP_FFMPEG ').start()# Atras del polo
    cap[3][1]=CamGear(source='rtsp://contralor:Villegas555@100.100.34.184/cgi-bin/main.cgi',**options,backend= 'cv2.CAP_FFMPEG ').start()# Polo frente
    cap[4][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.103.233/cgi-bin/main.cgi',**options,backend= 'cv2.CAP_FFMPEG ').start()# Estacionamiento emision
    cap[5][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.103.234/cgi-bin/main.cgi',**options,backend= 'cv2.CAP_FFMPEG ').start()# Baños
    cap[6][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.102.105/cgi-bin/main.cgi',**options,backend= 'cv2.CAP_FFMPEG ').start()# Entrada de pacheco
    cap[7][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.102.98/cgi-bin/main.cgi',**options,backend= 'cv2.CAP_FFMPEG ').start()# Entrada de pacheco 2
    cap[0][2]= 'Hay una persona en el galpon de las motos'
    cap[1][2]='Hay una persona en el costado del polo'
    cap[2][2]='Hay una persona atras del polo'
    cap[3][2]='Hay una persona en la entrada del polo'
    cap[4][2]='Hay una persona en el estacionamiento de emision'
    cap[5][2]='Hay una persona en el sector de baños'
    cap[6][2]='Hay una persona en la entrada de pacheco'
    cap[7][2]='Hay una persona en la entrada de pacheco 2'
    
    return cap

def read_camera (cap):
    frames=[[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3]]
    for j ,i ,t in cap: 
        frames[j][0]=i.read()
        frames[j][1]= [t]
    return frames

def stop_cam(cap):
    cap[0][1].stop()
    cap[1][1].stop()
    cap[2][1].stop()
    cap[3][1].stop()
    cap[4][1].stop()
    cap[5][1].stop()
    cap[6][1].stop()
    cap[7][1].stop()


def save_txt(boxes,frame,year_month):
    x= ((boxes['xmin']+boxes['xmax'])/2)/frame.shape[1]
    y= ((boxes['ymin']+boxes['ymax'])/2)/frame.shape[0]
    w= ((boxes['xmax']+boxes['xmin'])/2)/frame.shape[1]
    h= ((boxes['ymax']+boxes['ymin'])/2)/frame.shape[0]
    classes= boxes['class']
    labeling= DataFrame(list(zip(classes,x,y,w,h)))
    labeling.to_csv('labels/'+str(year_month)+'.txt', sep=' ',header=False, index= False)


