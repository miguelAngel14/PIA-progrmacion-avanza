import datetime
#utilize el import para importar los tipo de fechas
class CONTACTO:
     #Se difinio la clases y sus atributos
     #se utilizo un constructuro para los atributos del objeto
   def __init__(self,NickName,Nombre,Correo,Telefono,FechaNacimiento,Gasto,Registro=datetime.datetime.now()):
        self.NickName = NickName
        self.Nombre= Nombre
        self.Correo = Correo
        self.Telefono= Telefono
        self.FechaNacimiento = FechaNacimiento
        self.Gasto= Gasto
        self.Registro= Registro
 


