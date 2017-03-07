

class Hello:

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
                          "</h1><p>App id: Hola<p></body></html>")    #Devuelve el contenido del diccionario, es decir, el objeto



