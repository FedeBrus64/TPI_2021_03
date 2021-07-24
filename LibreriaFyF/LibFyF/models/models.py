from typing import NamedTuple, Optional


class cliente(NamedTuple):
    nro_cli: int
    nombre_cli: str
    apellido_cli: str 
    email_cli: str
    usuario_cli: str 
    contraseña_cli: str 


class empleado(NamedTuple):
    nro_emp: int
    nombre_cli: str 
    apellido_cli: str
    email_cli: str 
    usuario_cli: str
    contraseña_cli: str 
    #fecha_inicio: date