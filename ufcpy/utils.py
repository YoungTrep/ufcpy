from requests import Response
from .exceptions import UFCPyError

def check_response(response: Response):
    for res in response.history:
        if 302 == res.status_code:
            raise UFCPyError("The request returned a 302 before redirecting.")