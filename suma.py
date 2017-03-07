
class Sum:

    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information.
        request: HTTP request received from the client
        rest:    rest of the resource name after stripping the prefix
        """
        
        return rest

    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """
        try:
         sumando1 = parsedRequest[1]
         sumando2 = parsedRequest[3]
         result = int(sumando1) + int(sumando2)
         return ("200 OK", "<html><body><h1>" +
                          "Dumb application just saying 'It works!'" +
                          "</h1><p>El resultado es: " + str(result) + "<p></body></html>")    #Devuelve el contenido del diccionario, es decir, el objeto

        except IndexError:
         print("Introduce los sumandos")
