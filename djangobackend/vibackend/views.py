from email import message
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Camara, Telefono
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class CamaraView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            camaras = list(Camara.objects.filter(id=id).values())
            if len(camaras)>0:
                cam=camaras[0]
                mensaje = {'message': "exitoso", 'camaras': cam}
            else:
                mensaje = {'message': "camara no encontrada"}
            return JsonResponse(mensaje)
        else:
            camaras = list(Camara.objects.values())
            if len(camaras) > 0:
                mensaje = {'message': "exitoso", 'camaras': camaras}
            else:
                mensaje = {'message': "camara no encontrada"}
            return JsonResponse(mensaje)

    def post(self, request):
        carga= json.loads(request.body.decode('utf-8'))
        Camara.objects.create(nombre=carga['nombre'],source=carga['source'])
        mensaje = {'message': "exitoso"}
        return JsonResponse(mensaje)

    def put(self, request, id=0):
        datos = json.loads(request.body)
        camaras = list(Camara.objects.filter(id=id).values())
        if len(camaras)>0:
            cam=Camara.objects.get(id=id)
            cam.nombre=datos['nombre']
            cam.source=datos['source']
            cam.save()
            mensaje = {'message': "exitoso"}
        else:
            mensaje = {'message': "camara no encontrada"}
        return JsonResponse(mensaje)
        

    def delete(self, request, id):
        camaras = list(Camara.objects.filter(id=id).values())
        if len(camaras)>0:
            Camara.objects.filter(id=id).delete()
            mensaje = {'message': "exitoso"}
        else:
            mensaje = {'message': "Camara no encontrada"}
        return JsonResponse(mensaje)

    
class TelefonoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            telefonos = list(Telefono.objects.filter(id=id).values())
            if len(telefonos)>0:
                tel=telefonos[0]
                mensaje = {'message': "exitoso", 'telefonos': tel}
            else:
                mensaje = {'message': "telefono no encontrado"}
            return JsonResponse(mensaje)
        else:
            telefonos = list(Telefono.objects.values())
            if len(telefonos) > 0:
                mensaje = {'message': "exitoso", 'telefonos': telefonos}
            else:
                mensaje = {'message': "telefono no encontrado"}
            return JsonResponse(mensaje)

    def post(self, request):
        carga= json.loads(request.body.decode('utf-8'))
        Telefono.objects.create(numero=carga['numero'],nombre=carga['nombre'],chatid=carga['chatid'])
        mensaje = {'message': "exitoso"}
        return JsonResponse(mensaje)

    def put(self, request, id=0):
        datos = json.loads(request.body)
        telefonos = list(Telefono.objects.filter(id=id).values())
        if len(telefonos)>0:
            tel=Telefono.objects.get(id=id)
            tel.nombre=datos['numero']
            tel.nombre=datos['nombre']
            tel.source=datos['chatid']
            tel.save()
            mensaje = {'message': "exitoso"}
        else:
            mensaje = {'message': "telefono no encontrado"}
        return JsonResponse(mensaje)
        

    def delete(self, request, id):
        telefonos = list(Telefono.objects.filter(id=id).values())
        if len(telefonos)>0:
            Telefono.objects.filter(id=id).delete()
            mensaje = {'message': "exitoso"}
        else:
            mensaje = {'message': "telefono no encontrado"}
        return JsonResponse(mensaje)