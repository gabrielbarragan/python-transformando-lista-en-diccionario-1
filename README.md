## Transformando lista en diccionario - 1 

Define la función `get_first_and_last` que recibe una lista como argumento y retorna un diccionario `dict`:

- El primer elemento de la lista será la clave `key` del diccionario.
- El último elemento de la lista será el valor `value` de esta clave.

Es importante desarrollar tu código usando `unittest` para verificar que tu programa se comporta y produce el resultado deseado.


```python
"""get_first_and_last function goes here"""

...

```

```python
"""Ejemplo de entrada"""

print(get_first_and_last(["oro", "arroz", "molido"]))
>> {'oro': 'molido'}

```

```
#unittest - TDD

$ python test_get_first_and_last.py
```