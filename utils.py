import uuid

def rand_string():
    return uuid.uuid4().__str__().split("-")[0]