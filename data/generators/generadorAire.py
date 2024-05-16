import random


def generarDatosCalidadAire():
    
    listaDatos=[]
    for i in  range(1000):
        nombre=random.choice(['ana perez','jose jimeno','marco polo','martha lucrecia','karen andrea'])
        comuna=random.randint(1,14)
        ica= random.randint(10,80)
        fecha=random.choice(['2024-05-16','2024-05-17','2024-05-18'])
        correo=random.choice(['1correo@correo.com','2correo@correo.com','3correo@correo.com','4correo@correo.com','5correo@correo.com'])

        encuesta=[nombre,comuna,ica,fecha,correo]

        listaDatos.append(encuesta)
    return listaDatos


print(generarDatosCalidadAire())


def generarDatosRuidoAmbiental():
    
    listaDatos=[]
    for i in  range(1000):
        comuna=random.randint(1,14)
        direccion=random.choice(['Calle 68 #47-74','Cl 100 #10-20','cr20 # 80-80','cr68#60-70','cl12#43a-100'])
        nombre=random.choice(['ana perez','jose jimeno','marco polo','martha lucrecia','karen andrea'])
        decibeliosdiurnos= random.randint(10,80)
        decibeliosnocturnos= random.randint(10,60)
        fecha=random.choice(['2024-05-16','2024-05-17','2024-05-18'])

        

        encuesta=[comuna,direccion,nombre,decibeliosdiurnos,decibeliosnocturnos,fecha]

        listaDatos.append(encuesta)
    return listaDatos


print(generarDatosRuidoAmbiental())



def generarDatosSiembraArboles():
    
    listaDatos=[]
    for i in  range(1000):
        corregimiento=random.randint(1,14)
        hectarias_sembradas= random.randint(10,80)
        EspecieSembrada=random.choice(['Calle 68 #47-74','Cl 100 #10-20','cr20 # 80-80','cr68#60-70','cl12#43a-100'])
        nombreArbol=random.choice(['ana perez','jose jimeno','marco polo','martha lucrecia','karen andrea'])
        fecha=random.choice(['2024-05-16','2024-05-17','2024-05-18'])
        correo=random.choice(['1correo@correo.com','2correo@correo.com','3correo@correo.com','4correo@correo.com','5correo@correo.com'])
    

        

        encuesta=[corregimiento,hectarias_sembradas,EspecieSembrada,nombreArbol,fecha,correo]

        listaDatos.append(encuesta)
    return listaDatos


print(generarDatosSiembraArboles())




def generarDatosVehiculosComuna():
    
    listaDatos=[]
    for i in  range(1000):
        tipoVehiculo=random.choice(['Bus','Moto','Particular','Camion'])
        tipoCombustible=random.choice(['Gasolina','gas','diesel','electrico'])
        nombre=random.choice(['ana perez','jose jimeno','marco polo','martha lucrecia','karen andrea'])
        FrecuenciaUsoVehiculo=random.choice(['1 dia a la semana','','2 dias a la semana','3 dias a la semana','4 dias a la semana ','toda la semana'])
        dirreccion=random.choice(['Calle 68 #47-74','Cl 100 #10-20','cr20 # 80-80','cr68#60-70','cl12#43a-100'])
        

        encuesta=[corregimiento,hectarias_sembradas,EspecieSembrada,nombreArbol,fecha,correo]

        listaDatos.append(encuesta)
    return listaDatos


print(generarDatosSiembraArboles())




# **** Cantidad de vehiculos por comunas ***

# tipo de vehiculos
# tipo de combustible que usa
# nombre
# fecuencia de uso de vehiculo
#dirreccion
# tecnomecanica
# cantidad de vehiculos por barrio








