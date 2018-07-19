from zeep import Client

print "Consulta de servicio SOAP por Jean y Oscar"

cliente = Client('http://localhost:7777/ws/AcademicoWebService?wsdl')

listaEstudiantes = cliente.service.getAllEstudiante()
print "\n\nListado de estudiantes: \n" + str(listaEstudiantes)

asignaturaConsultada = cliente.service.getAsignatura(1)
print "\n\nAsignatura consultada: \n" + str(asignaturaConsultada)

profesorConsultado = cliente.service.getProfesor("031-0001-01")
print "\n\nProfesor consultado: \n" + str(profesorConsultado)