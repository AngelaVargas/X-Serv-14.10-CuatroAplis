
import random

class Aleat:

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

        num = random.randint(1,1000000)

        return ("200 OK", "<html><body><h1>" +
                          "Dumb application just saying 'It works!'" +
                          "</h1><p><a href=http://localhost:1234/aleat/" + str(num) + ">Dame otra</a><p></body></html>")    #Devuelve el contenido del diccionario, es decir, el objeto
