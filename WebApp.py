#!/usr/bin/python3

"""
webAppMulti class
Root for hierarchy of classes implementing web applications
Each class can dispatch to serveral web applications, depending
on the prefix of the resource name
Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles (2009-15)
jgb @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
October 2009, February 2015
"""

import socket
import hola
import adios
import aleat
import suma


class app:
    """Application to which webApp dispatches. Does the real work
    Usually real applications inherit from this class, and redefine
    parse and process methods"""

    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information.
        request: HTTP request received from the client
        rest:    rest of the resource name after stripping the prefix
        """

        return None

    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>" +
                          "Dumb application just saying 'It works!'" +
                          "</h1><p>Introduce a valid resource<p></body></html>")    #Devuelve el contenido del diccionario, es decir, el objeto


class webApp:
    """Root of a hierarchy of classes implementing web applications
    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def select(self, request):
        """Selects the application (in the app hierarchy) to run.
        Having into account the prefix of the resource obtained
        in the request, return the class in the app hierarchy to be
        invoked. If prefix is not found, return app class
        """

        resource = request.split(' ', 2)[1]  #Me quedo con el recurso /hola, por ejemplo
        for prefix in self.apps.keys():      #Self.apps.keys() quiere decir que del diccionario me quedo solo con la parte de keys, es decir, los recursos, /hola;/adios;/aleat y /suma
            if resource.startswith(prefix):  #Si coincide el recurso con la key del diccionario, continúo
                print("Running app for prefix: " + prefix + \
                    ", rest of resource: " + resource[len(prefix):] + ".")   #Escribo el recurso y si hay algo detrás
                return (self.apps[prefix], resource[len(prefix):])           #Devuelvo el objeto al que se refiere el recurso, es decir, hola, y lo que vaya detrás
        print("Running default app")
        return (self.myApp, resource)

    def __init__(self, hostname, port, apps):
        """Initialize the web application."""

        self.apps = apps
        self.myApp = app()

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        while True:
            print('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print('HTTP request received (going to parse and process):')
            Request = recvSocket.recv(2048).decode('utf-8')
            print(Request)
            (theApp, rest) = self.select(Request)
            parsedRequest = theApp.parse(Request, rest)                    #Devuelve un null
            (returnCode, htmlAnswer) = theApp.process(parsedRequest)       #Devuelve el código de estado y la html
            print('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n", 'utf-8'))
            recvSocket.close()

if __name__ == "__main__":
	hola = hola.Hello()
	adios = adios.Bye()
	suma = suma.Sum()
	aleat	=	aleat.Aleat()
	testWebApp = webApp("localhost", 1234, {'/hola': hola,
                                            '/adios' : adios,
											'/suma':	suma,
											'/aleat':	aleat})

