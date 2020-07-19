import json
from  functools import  wraps
def to_json(func):
    @wraps(func)
    def wrapped(*args,**kwargs):
        return json.dumps(func(*args,**kwargs))
    return wrapped
if __name__== "__main__":
    @to_json
    def get_data():
        return {'data': 42}

    print(get_data())  # вернёт '{"data": 42}'