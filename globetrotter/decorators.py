from functools import wraps
from sanic.response import json
from pydantic import ValidationError

def handle_exceptions(func):
    @wraps(func)
    async def wrapper(request, *args, **kwargs):
        try:
            return await func(request, *args, **kwargs)
        except ValidationError as e:
            return json({"error": "Validation failed", "details": e.errors()}, status=400)
        except Exception as e:
            return json({"error": str(e)}, status=500) 
    return wrapper