from ClasesDAO.MesaDAO import MesaDAO


class Mesa:

    @classmethod
    def agregarMesa(cls, pres_de_mesa_dni, cupo, nombre, horario):
        return MesaDAO.agregarMesa(pres_de_mesa_dni, cupo, nombre, horario)

    @classmethod
    def eliminarMesa(cls, codDeMesa):
        return MesaDAO.eliminarMesa(codDeMesa)

    @classmethod
    def eliminarMesas(cls):
        return MesaDAO.eliminarMesas()

    @classmethod
    def darPresDeMesa(cls, codDeMesa):
        if MesaDAO.existeMesa(codDeMesa):
            return MesaDAO.darPresDeMesa(codDeMesa)

    @classmethod
    def asignadosAMesa(cls, codDeMesa):
        if cls.existeMesa(codDeMesa):
            return True
        return False

    @classmethod
    def obtenerMesas(cls):
        return MesaDAO.obtenerMesas()

    @classmethod
    def existeMesa(cls, codDeMesa):
        return MesaDAO.existeMesa(codDeMesa)

    @classmethod
    def obtenerMesas(cls):
        return MesaDAO.obtenerMesas()
