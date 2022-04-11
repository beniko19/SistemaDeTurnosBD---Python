from Clases.SistemaDeTurnos import SistemaDeTurno
from Fixture import *

sistema = SistemaDeTurno('Sistema')

sistema.registrarVotante(dniFrodo, 'Frodo', 23, not tieneEnfPrevia, not trabaja)
sistema.registrarVotante(dniEowyn, 'Eowyn', 25, tieneEnfPrevia, not trabaja)
sistema.registrarVotante(dniBilbo, 'Bilbo', 65, tieneEnfPrevia, not trabaja)
sistema.registrarVotante(dniGandalf, 'Gandalf', 23, not tieneEnfPrevia, trabaja)
sistema.registrarVotante(dniLegolas, 'Legolas', 80, not tieneEnfPrevia, trabaja)
sistema.registrarVotante(dniGaladriel, 'Galadriel', 81, not tieneEnfPrevia, trabaja)
sistema.registrarVotante(dniArwen, 'Arwen', 50, not tieneEnfPrevia, trabaja)

numMesaEnfPreexistente = sistema.agregarMesa(dniFrodo, 1, 'Enfermedad', '8-18')
numMesaMayor65 = sistema.agregarMesa(dniBilbo, 1, 'Mayor65', '8-18')
numMesaGeneral = sistema.agregarMesa(dniGaladriel, 1, 'General', '8-18')
numMesaTrabajador = sistema.agregarMesa(dniGandalf, 1, 'Trabajador', '8-12')

print(f'Numeros de mesa generados: {numMesaEnfPreexistente} {numMesaMayor65} {numMesaGeneral} {numMesaTrabajador}')

print('Turnos generados [Paso 1]: ')
print(f'\t- {sistema.obtenerTurno(dniFrodo)}')
print(f'\t- {sistema.obtenerTurno(dniBilbo)}')
print(f'\t- {sistema.obtenerTurno(dniGaladriel)}')
print(f'\t- {sistema.obtenerTurno(dniGandalf)}')

print('\n======================================================')
print('Estado Sistema de Turnos: ')
print('-------------------------')
print(sistema.__str__())
print('\n======================================================')

sistema.registrarVotante(1, 'Nombre1', 30, False, False)
sistema.registrarVotante(2, 'Nombre2', 70, False, False)
sistema.registrarVotante(3, 'Nombre3', 30, True, False)
sistema.registrarVotante(4, 'Nombre4', 30, False, True)

print(sistema.asignarTurnos())

print(f'Cant votantes sin turno: {len(sistema.sinTurnoSegunTipoMesa())}')

mesaEnfPreexistente = sistema.asignadosAMesa(numMesaEnfPreexistente)
mesaMayor65 = sistema.asignadosAMesa(numMesaMayor65)
mesaGeneral = sistema.asignadosAMesa(numMesaGeneral)
mesaTrabajador = sistema.asignadosAMesa(numMesaTrabajador)

print(f'Cant turnos generados [Paso 3]:\nt-Turnos generados en MesaEnfPreExistente: {mesaEnfPreexistente} \n'
      f'\t-Turnos generados en MesaMayor65: {mesaMayor65} \n'
      f'\t-Turnos generados en MesaGeneral: {mesaGeneral} \n'
      f'\t-Turnos generados en MesaTrabajador: {mesaTrabajador}')

print('\n======================================================')
print('Estado Sistema de Turnos: ')
print('-------------------------')
print(sistema.__str__())
print('\n======================================================')
