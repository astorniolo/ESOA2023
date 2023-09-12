from django.http import HttpResponse
import datetime

def saludoView(request):   #primer view controlador
    return HttpResponse("Hola Mundo !!!! esta es mi primer pagina")

def despedidaView(request):   #primer view controlador
    return HttpResponse("nos olemos luego..........")

def verFechaView(request):   #primer view controlador
    fechaActual=datetime.datetime.now()
    documentoHTML="""<html>
                        <body>
                            <h1>
                                fecha y hora actuales : %s
                            </h1>
                        </body>
                    </html>
                  """ % fechaActual

    return HttpResponse(documentoHTML)

def nombreParametroView(request,nombre):

    fechaActual=datetime.datetime.now()
    documentoHTML="""<html>
                        <body>
                            <h1>
                                Hola %s  !! ahora: %s
                            </h1>
                        </body>
                    </html>
                  """ % (nombre,fechaActual)
    return HttpResponse(documentoHTML)