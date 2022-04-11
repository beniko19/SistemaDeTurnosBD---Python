from ClasesDAO.VotanteDAO import VotanteDAO


class Votante:

    @classmethod
    def registrarVotante(cls, dni, nombre, edad, enf_previa, trabaja, es_pres_de_mesa, ya_voto, turno):
        return VotanteDAO.insertarVotante(dni, nombre, edad, enf_previa, trabaja, es_pres_de_mesa, ya_voto, turno)

    @classmethod
    def vaciarListaDeVotantes(cls):
        return VotanteDAO.eliminarVotantes()

    @classmethod
    def eliminarVotante(cls, dni):
        if cls.estaRegistrado(dni):
            return VotanteDAO.eliminarVotante(dni)
        return Exception('El votante no esta registrado')

    @classmethod
    def estaRegistrado(cls, dni):
        return VotanteDAO.existeVotante(dni)

    @classmethod
    def obtenerVotante(cls, dni):
        if cls.estaRegistrado(dni):
            return VotanteDAO.obtenerVotante(dni)
        return Exception('El votante no esta registrado')

    @classmethod
    def asignarPresDeMesa(cls, dni):
        if cls.estaRegistrado(dni):
            if not cls.esPresDeMesa(dni):
                return VotanteDAO.asignarPresDeMesa(dni)
            else:
                return Exception('El votanta ya es presidente de mesa')
        else:
            return Exception('El presidente no esta registrado')

    @classmethod
    def esPresDeMesa(cls, dni):
        if cls.estaRegistrado(dni):
            return VotanteDAO.saberSiEsPresDeMesa(dni)
        return Exception('El votante no esta registrado')

    @classmethod
    def tieneTurno(cls, dni):
        if cls.estaRegistrado(dni):
            return VotanteDAO.tieneTurno(dni)
        return Exception('El votante no esta registrado')

    @classmethod
    def votar(cls, dni):
        VotanteDAO.votar(dni)
        return cls.desasignarTurno(dni)

    @classmethod
    def cantVotantesConTurno(cls):
        return VotanteDAO.cantVotantesConTurno()

    @classmethod
    def asginarTurno(cls, dni_votante):
        if Votante.estaRegistrado(dni_votante):
            return VotanteDAO.asginarTurno(dni_votante)
        return Exception('El votante no esta registrado')

    @classmethod
    def desasignarTurno(cls, dni_votante):
        if Votante.estaRegistrado(dni_votante):
            return VotanteDAO.desasignarTurno(dni_votante)
        return Exception('El votante no esta registrado')

    @classmethod
    def obtenerVotantes(cls):
        return VotanteDAO.obtenerVotantes()

    @classmethod
    def yaVoto(cls, dni):
        if Votante.estaRegistrado(dni):
            return VotanteDAO.saberSiVoto(dni)
        return Exception('El votante no esta registrado')

    @classmethod
    def saberSiTieneEnfPrevia(cls, dni):
        if Votante.estaRegistrado(dni):
            return VotanteDAO.saberSiTieneEnfPrevia(dni)
        return Exception('El votante no esta registrado')

    @classmethod
    def saberSiTrabaja(cls, dni):
        if Votante.estaRegistrado(dni):
            return VotanteDAO.saberSiTrabaja(dni)
        return Exception('El votante no esta registrado')
