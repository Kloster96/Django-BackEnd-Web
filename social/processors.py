from .models import Link



def funcion_procesos(request):
    proceso={}
    links = Link.objects.all()
    for link in links:
        proceso[link.key] = link.url
    return proceso