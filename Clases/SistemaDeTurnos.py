from Clases.Votante import Votante
from Clases.Mesa import Mesa
from Clases.Turno import Turno


class SistemaDeTurno:
    num = 1

    def __init__(self, nombre):
        self._nombre = nombre

    # Votantes Metodos
    def registrarVotante(self, dni, nombre, edad, enf_previa, trabaja, es_pres_de_mesa=False, ya_voto=False, turno=False):
        return Votante.registrarVotante(dni, nombre, edad, enf_previa, trabaja, es_pres_de_mesa, ya_voto, turno)

    def eliminarTodosLosVotantes(self):
        return Votante.vaciarListaDeVotantes()

    def eliminarVotante(self, dni):
        if Votante.estaRegistrado(dni):
            if Votante.yaVoto(dni):
                return Votante.eliminarVotante(dni)
            return Exception('El votante aun no ha votado')
        return Exception('El votante no esta registrado')

    def saberSiVotantateEstaRegistrado(self, dni):
        return Votante.estaRegistrado(dni)

    def votantesConTurno(self):
        return Votante.cantVotantesConTurno()

    def asignarTurnos(self):
        votantes = Votante.obtenerVotantes()
        mesas = Mesa.obtenerMesas()
        cantTurnosAsignados = 0
        for votante in votantes:
            for mesa in mesas:
                if not Votante.tieneTurno(votante[0]) and not Votante.yaVoto(votante[0]):
                    # Asignar a mesa general
                    if (votante[3] is False and votante[4] is False and votante[2] <= 65) and mesa[3] == 'General':
                        Turno.agregarTurno(mesa[0], votante[0], )
                        Votante.asginarTurno(votante[0])
                        cantTurnosAsignados += 1
                        continue
                    # Asignar a mesa enfermedad
                    elif votante[3] is True and mesa[3] == 'Enfermedad':
                        Turno.agregarTurno(mesa[0], votante[0], )
                        Votante.asginarTurno(votante[0])
                        cantTurnosAsignados += 1
                        continue
                    # Asignar a mesa trabaja
                    elif votante[4] is True and mesa[3] == 'Trabajador':
                        Turno.agregarTurno(mesa[0], votante[0], )
                        Votante.asginarTurno(votante[0])
                        cantTurnosAsignados += 1
                        continue
                    # Asignar a mesa mayor65
                    elif votante[2] >= 65 and mesa[3] == 'Mayor65':
                        Turno.agregarTurno(mesa[0], votante[0], )
                        Votante.asginarTurno(votante[0])
                        cantTurnosAsignados += 1
        return cantTurnosAsignados

    def votar(self, dni):
        if Votante.estaRegistrado(dni):
            if not Votante.yaVoto(dni):
                Turno.eliminarTurno(dni, None)
                return Votante.votar(dni)
            else:
                return Exception('El votante ya voto')
        return Exception('El votante no esta registrado en el sistema')

    def sinTurnoSegunTipoMesa(self):
        votantesSinTurno = list()
        contMesaEnfPrevia = 0
        contMesaTrabajadores = 0
        contMesaPersonaMayor = 0
        contMesaGeneral = 0
        votantes = Votante.obtenerVotantes()
        for votante in votantes:
            if not Votante.tieneTurno(votante[0]):
                if Votante.saberSiTieneEnfPrevia(votante[0]):
                    contMesaEnfPrevia += 1
                elif Votante.saberSiTrabaja(votante[0]):
                    contMesaTrabajadores += 1
                elif votante[2] >= 65:
                    contMesaPersonaMayor += 1
                else:
                    contMesaGeneral += 1
        mesaEnfermedades = ('MesaEnfermedades', contMesaEnfPrevia)
        mesaPersonaMayor = ('MesaPersonaMayot', contMesaPersonaMayor)
        mesaTrabajadores = ('MesaTrabajadores', contMesaTrabajadores)
        mesaGeneral = ('MesaGeneral', contMesaGeneral)
        votantesSinTurno.append(mesaEnfermedades)
        votantesSinTurno.append(mesaPersonaMayor)
        votantesSinTurno.append(mesaTrabajadores)
        votantesSinTurno.append(mesaGeneral)
        return votantesSinTurno

    # Mesas Metodos
    def agregarMesa(self, pres_de_mesa_dni, cupo, nombre, horario):
        if Votante.estaRegistrado(pres_de_mesa_dni) and not Votante.tieneTurno(pres_de_mesa_dni):
            cod_de_mesa = Mesa.agregarMesa(pres_de_mesa_dni, cupo, nombre, horario)
            Turno.agregarTurno(cod_de_mesa, pres_de_mesa_dni)
            Votante.asignarPresDeMesa(pres_de_mesa_dni)
            Votante.asginarTurno(pres_de_mesa_dni)
            return cod_de_mesa
        else:
            raise Exception('El votante no esta registrado en el sistema')

    def eliminarMesa(self, codDeMesa):
        if Turno.existeTurnoConMesa(codDeMesa):
            Turno.eliminarTurno(None, codDeMesa)
            return Mesa.eliminarMesa(codDeMesa)
        return Mesa.eliminarMesa(codDeMesa)

    def asignadosAMesa(self,codDeMesa):
        if Mesa.existeMesa(codDeMesa):
            return Turno.obtenerVotantesEnMesa(codDeMesa)

    def obtenerTurno(self, dni):
        if Votante.estaRegistrado(dni):
            if not Votante.yaVoto(dni):
                return Turno.consultarTurno(dni)
            return Exception('El votante ya voto')
        return Exception('El votante no esta registrado en el sistema')

    def eliminarMesas(self):
        Turno.eliminarTurnos()
        return Mesa.eliminarMesas()

    def eliminarTodosLosTurnos(self):
        return Turno.eliminarTurnos()

    def obtenerTurnos(self):
        turnosVotantes = list()
        votantes = Votante.obtenerVotantes()
        for votante in votantes:
            if Votante.tieneTurno(votante[0]):
                turnosVotantes.append(Turno.consultarTurno(votante[0]))
        return turnosVotantes

    def __str__(self):
        return f'{self._nombre}\n\nCantidad de votantes en espera de asignacion de turno: {self.sinTurnoSegunTipoMesa()}\n\n\nTurno de votantes:\n\n {self.obtenerTurnos()}' \
               f'\n\nMesas habilitadas en el sistema:\n\n {Mesa.obtenerMesas()}'
