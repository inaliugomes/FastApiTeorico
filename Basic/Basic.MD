# Types

Sabemos que en Python existen diferentes tipos de datos, desde los más básicos hasta los que podemos crear nosotros mediante clases, que también son considerados tipos de datos.

En FastAPI podemos indicar qué tipo de datos son los parámetros de una función usando `:` seguido del tipo de dato. Por ejemplo:

```python
def get_full_name(firstName: str, lastName: str):
    # Al indicar a Python que firstName y lastName son strings,
    # se activan los métodos de string disponibles
    full_name = firstName.title() + " " + lastName.title()
    return full_name
````
El beneficio de utilizar esta aproximación es que también podemos evitar errores si el usuario final pasa un valor de un tipo que el programa no espera.

Otro beneficio es que, si el programa conoce el tipo de datos que estamos pasando, puede ayudarnos con el autocompletado, lo que facilita escribir código más completo y seguro.

## Type Class

Como mencioné arriba, en programación las clases también son consideradas tipos de datos. Es decir, pueden ser usadas como tipo de datos en los parámetros de nuestras funciones, lo cual permite validar y acceder a sus propiedades y métodos.

````Python
class Person:
    def __init__(self, name: str):
        self.name = name

# Al usar correctamente la tipificación del objeto,
# el IDE nos ayuda a validar las propiedades del objeto
def get_person_name(person: Person):
    return person.name
````
Cuando no sabemos qué tipo de dato vamos a manejar, podemos usar Any, que permite que el parámetro pueda ser de cualquier tipo.

````Python 
from typing import Any, List

# Una función que puede recibir cualquier tipo de parámetro
def get_type(p: Any):
    print(type(p))

# Una función que recibe un argumento del tipo List,
# y además los valores de esta lista deben ser strings
def process_item(item: List[str]):
    print(item)

# La clave es del tipo str y el valor puede ser cualquier tipo, incluso listas
def process_items(item: dict[str, Any]):
    for item_name, item_price in item.items():
        print(item_name)
        print(item_price)
````
También podemos indicar que un parámetro puede ser de un tipo específico o None, es decir, que el parámetro es opcional.
````python 
def say_hi(name: str | None):
    if name is not None:
        print(name)
    else:
        print("Hello")
````

Por ejemplo, en FastAPI podemos definir endpoints así:
````python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
````
Aquí estamos indicando que los argumentos pueden ser nulos (None) o tener un tipo específico. Esto ayuda a validar datos y mantener nuestro código más seguro y legible.