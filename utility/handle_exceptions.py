from images.models import Image
from prompts.models import Prompt
from rest_framework.exceptions import NotFound 
from rest_framework.response import Response

def handle_exceptions(handler_func):
    def wrapper(*args, **kwargs):
        try:
            return handler_func(*args, **kwargs)
        except (Image.DoesNotExist, Prompt.DoesNotExist, NotFound) as exc:
            return Response({"errorMessage":str(exc)})
        except Exception as exc:
            print(exc)
            return Response(exc, 500)
    return wrapper