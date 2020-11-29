#Un alumno desea saber cuál será su calificación final
#Dicha calificación se compone de los siguientes porcentajes
#55% del promedio de sus calificaciones parciales
#30% de la calificación del examen final
#15% del trabajo final

parcial1 = float(input('Dime calificacion del parcial 1:'))
parcial2 = float(input('Dime calificacion del parcial 2:'))
parcial3 = float(input('Dime calificacion del parcial 3:'))
examen = float(input('Dime calificacion del examen final:'))
trabajo= float(input('Dime calificacion del trabajo final:'))
calificacion_final = ((parcial1 + parcial2 + parcial3)/ 3 ) * 0.55 + 0.3 * examen + 0.15 * trabajo
print('Calificacion final: %.2f' % calificacion_final) # 2.f % es para redondear a dos decimales