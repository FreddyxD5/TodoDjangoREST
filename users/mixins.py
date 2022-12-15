import json
class Persona:
    def __init__(self, nombre, documento) -> None:
        self.nombre = nombre
        self.documento = documento

    def __str__(self):
        return f"{self.nombre} - {self.documento}"


class DictMixin:
    def to_dict(self):        
        return self.__dict__


class JsonMixin:
    def to_json(self):                
        return json.dumps(self.to_dict())


# class Empleado(DictMixin, JsonMixin, Persona):
#     def __init__(self, nombre, documento, pago) -> None:
#         Persona.__init__(self, nombre, documento)
#         self.pago = pago


class Empleado(DictMixin, JsonMixin, Persona):
    def __init__(self, nombre, documento, skills, datos_familia) -> None:
        Persona.__init__(self, nombre, documento)
        self.skills = skills
        self.datos_familia = datos_familia

        
a = Empleado("jesus","54545",["amable","Respetuoso","puntual"], {"Padre":"jesus","Madre":"Maria"})
print(a.to_dict())
print(a.to_json())