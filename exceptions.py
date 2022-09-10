try:
    raise Exception("Error!")
except Exception as error:
    print(error)
finally:
    print("The end!!")

class NameNotFoundException(Exception):
    pass
try:
    raise NameNotFoundException()
except NameNotFoundException:
    print('No name found!')