from ConexionBD.cursorDelPool import CursorDelPool


class MesaDAO:
    _SELECCIONAR = 'SELECT * FROM mesas ORDER BY cod_de_mesa'
    _SELECCIONAR_UNA_MESA = 'SELECT * FROM mesas WHERE cod_de_mesa=%s'
    _INSERTAR = 'INSERT INTO mesas(pres_de_mesa_dni, cupo, nombre, horario) VALUES(%s, %s, %s, %s) RETURNING cod_de_mesa'
    _ACTUALIZAR = 'UPDATE mesas SET cod_de_mesa=%s'
    _ELIMINAR_MESA = 'DELETE FROM mesas WHERE cod_de_mesa=%s'
    _ELIMINAR_MESAS = 'DELETE FROM mesas'
    _REINICIAR_MESAS = 'TRUNCATE mesas,turnos RESTART IDENTITY'

    @classmethod
    def existeMesa(cls, codDeMesa):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR_UNA_MESA, (codDeMesa,))
            mesa = cursor.fetchone()
            if mesa is not None:
                return True
            return False

    @classmethod
    def obtenerMesa(cls, codDeMesa):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR_UNA_MESA, (codDeMesa,))
            return cursor.fetchone()

    @classmethod
    def agregarMesa(cls, pres_de_mesa_dni, cupo, nombre, horario):  # falta terminar
        with CursorDelPool() as cursor:
            mesa = (pres_de_mesa_dni, cupo, nombre, horario)
            cursor.execute(cls._INSERTAR, mesa)
            return cursor.fetchone()

    @classmethod
    def eliminarMesa(cls, cod_de_mesa):
        with CursorDelPool() as cursor:
            if cls.existeMesa(cod_de_mesa):
                cursor.execute(cls._ELIMINAR_MESA, (cod_de_mesa,))
                return cursor.rowcount
            return Exception('La mesa no se encuentra en el sistema')

    @classmethod
    def eliminarMesas(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._REINICIAR_MESAS)
            cursor.execute(cls._REINICIAR_MESAS)
            return cursor.rowcount

    @classmethod
    def obtenerNombre(cls, codDeMesa):
        if cls.existeMesa(codDeMesa):
            mesa = cls.obtenerMesa(codDeMesa)
            return mesa[3]

    @classmethod
    def obtenerMesas(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            return cursor.fetchall()

    @classmethod
    def darPresDeMesa(cls, codDeMesa):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR_UNA_MESA, (codDeMesa,))
            presDeMesa = cursor.fetchone()
            return presDeMesa
