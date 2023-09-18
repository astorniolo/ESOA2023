from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

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


# Utilizacion de Templates
def saludo2View(request):
    documento_HTML=open("C:/Users/acspr/OneDrive/ESOA/ESOA2023/TAP/U6/Django/HolaMundo/HolaMundo/Templates/saludo2.html")
    template=Template(documento_HTML.read())
    documento_HTML.close()
    
    ctx=Context()
    return HttpResponse( template.render(ctx))

    
def saludo3View(request):
    nombre="Andrea"
    edad=56
    signo="Virgo"
    materias=["SGBD","AAS","PROGRAMACION"]
    
    ctx={"nombre_profe":nombre,"edad_profe":edad,"signo_profe":signo,"materias_profe":materias}
    
    return HttpResponse( request,'saludo3.html',ctx)
    
    