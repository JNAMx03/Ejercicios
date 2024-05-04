#CANTIDAD NUMEROS DECIMALES CON FORMAT
# res = 5
# print("{0:.2f}".format(res))
# print(f"{res:.2f}")

#SWITCH
# def lunes():
# 	print('lunes')

# def martes():
# 	print('martes')

# def miercoles():
# 	print('miércoles')

# def jueves():
# 	print('jueves')

# def viernes():
# 	print('viernes')

# def sabado():
# 	print('sábado')

# def domingo():
# 	print('domingo')

# def error():
# 	print('error')

# def xd(dia):
#     switch_semana = {
#         1: lunes,
#         2: martes,
#         3: miercoles,
#         4: jueves,
#         5: viernes,
#         6: sabado,
#         7: domingo
#     }

#     #tomamos la función asociada a la variable y la invocamos
#     switch_semana.get(dia, error)()

# dia = 5
# xd(dia)

a = "TestCaseTestCase"
b = "Case"

c = a.find(b, 5, len(a))
print(c)