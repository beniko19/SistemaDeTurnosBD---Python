from ConexionBD.cursorDelPool import CursorDelPool


class TurnosDAO:
    _SELECCIONAR = 'SELECT t.dni_votante, v.nombre, t.id_mesa, m.nombre, m.horario FROM turnos t JOIN votantes v ON t.dni_votante=v.dni JOIN mesas m ON t.id_mesa=m.cod_de_mesa WHERE m.cod_de_mesa=%s'
    _INSERTAR = 'INSERT INTO turnos(dni_votante, id_mesa) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE mesas SET cod_de_mesa=%s'
    _ELIMINAR = 'DELETE FROM turnos'
    _ELIMINAR_POR_DNI = 'DELETE FROM turnos WHERE dni_votante=%s'
    _ELIMINAR_POR_ID_MESA = 'DELETE FROM turnos WHERE id_mesa=%s'
    _SELECT_TURNO = 'SELECT t.dni_votante, v.nombre, v.ya_voto, t.id_mesa, m.nombre, m.horario FROM turnos t JOIN votantes v ON t.dni_votante=v.dni JOIN mesas m ON t.id_mesa=m.cod_de_mesa WHERE t.dni_votante=%s'

    @classmethod
    def agregarTurno(cls, dni_votante, id_mesa):
        with CursorDelPool() as cursor:
            turno = (dni_votante, id_mesa)
            cursor.execute(cls._INSERTAR, turno)
            return cursor.rowcount

    @classmethod
    def existeTurnoConMesa(cls, codDeMesa):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR, (codDeMesa,))
            turno = cursor.fetchone()
            if turno is not None:
                return True
            return False

    @classmethod
    def eliminarTurno(cls, dni_votante=None, id_mesa=None):
        with CursorDelPool() as cursor:
            if dni_votante is not None:
                cursor.execute(cls._ELIMINAR_POR_DNI, (dni_votante,))
                return cursor.rowcount
            cursor.execute(cls._ELIMINAR_POR_ID_MESA, (id_mesa,))
            return cursor.rowcount

    @classmethod
    def eliminarTurnos(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR)
            return cursor.rowcount

    @classmethod
    def consultarTurno(cls, dni_votante):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT_TURNO, (dni_votante,))
            return cursor.fetchone()

    @classmethod
    def obtenerDniVotante(cls, id_mesa):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR, (id_mesa,))
            turno = cursor.fetchone()
            return turno[1]

    @classmethod
    def obtenerVotantesEnMesa(cls, codDeMesa):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR, (codDeMesa,))
            return cursor.fetchall()
