# Builtins é como o objeto global do javascript. Para acessar o seus métodos
# e propriedades, utilizamos a notação de ponto (.).

print(__builtins__.type(1))  # <class 'int'>
print(type(1))  # We can omit "__builtins__"

print('Hello')
# help(dir)
dir()  # list of object keys
__builtins__._  # last operation result
