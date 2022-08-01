import hashlib

s = "Python Bootcamp"


def string_hash(string: str):
    """ Hashing a string """
    hash_object = hashlib.sha224(string.encode())
    return hash_object.hexdigest()


print(string_hash(s))
