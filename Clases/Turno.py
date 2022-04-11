from ClasesDAO.turnosDAO import TurnosDAO


class Turno:

    @classmethod
    def consultarTurno(cls, dni):
        return TurnosDAO.consultarTurno(dni)

    @classmethod
    def agregarTurno(cls, id_mesa, pres_de_mesa_dni):
        return TurnosDAO.agregarTurno(pres_de_mesa_dni, id_mesa)

    @classmethod
    def existeTurnoConMesa(cls, cod_de_mesa):
        return TurnosDAO.existeTurnoConMesa(cod_de_mesa)

    @classmethod
    def eliminarTurno(cls, dni_votante, cod_de_mesa):
        return TurnosDAO.eliminarTurno(dni_votante, cod_de_mesa)

    @classmethod
    def obtenerVotantesEnMesa(cls, codDeMesa):
        return TurnosDAO.obtenerVotantesEnMesa(codDeMesa)

    @classmethod
    def eliminarTurnos(cls):
        return TurnosDAO.eliminarTurnos()
