from ConexionBD.cursorDelPool import CursorDelPool


class VotanteDAO:
    _SELECCIONAR = 'SELECT * FROM votantes ORDER BY dni'
    _INSERTAR = 'INSERT INTO votantes(dni, nombre, edad, enf_previa, trabaja, es_pres_de_mesa, ya_voto, turno) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR_YA_VOTO = 'UPDATE votantes SET ya_voto=%s WHERE dni=%s RETURNING dni'
    _ES_PRES_DE_MESA = 'UPDATE votantes SET es_pres_de_mesa=%s WHERE dni=%s'
    _ACTUALIZAR_TURNO = 'UPDATE votantes SET turno=%s WHERE dni=%s'
    _ELIMINAR = 'DELETE FROM votantes WHERE dni=%s'
    _RECUPERAR_DATOS_CON_TURNO = 'INNER JOIN'

    @classmethod
    def insertarVotante(cls, dni, nombre, edad, enf_previa, trabaja, es_pres_de_mesa=False, ya_voto=False, turno=False):
        with CursorDelPool() as cursor:
            valores = (dni, nombre, edad, enf_previa, trabaja, es_pres_de_mesa, ya_voto, turno)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminarVotantes(cls):
        with CursorDelPool() as cursor:
            cursor.execute('DELETE FROM votantes')
            return cursor.rowcount

    @classmethod
    def eliminarVotante(cls, dni):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, (dni,))
            return cursor.rowcount

    @classmethod
    def existeVotante(cls, dni):
        with CursorDelPool() as cursor:
            cursor.execute('SELECT * FROM votantes WHERE dni=%s', (dni,))
            votante = cursor.fetchone()
            if votante is not None:
                return True
            return False

    @classmethod
    def obtenerVotante(cls, dni):
        with CursorDelPool() as cursor:
            cursor.execute('SELECT * FROM votantes WHERE dni=%s', (dni,))
            return cursor.fetchone()

    @classmethod
    def asginarTurno(cls, dni):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ACTUALIZAR_TURNO, (True, dni))
            return cursor.rowcount

    @classmethod
    def desasignarTurno(cls, dni):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ACTUALIZAR_TURNO, (False, dni))
            return cursor.rowcount

    @classmethod
    def asignarPresDeMesa(cls, dni):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ES_PRES_DE_MESA, (True, dni))
            return cursor.rowcount

    @classmethod
    def saberSiEsPresDeMesa(cls, dni):
        with CursorDelPool() as cursor:
            votante = cls.obtenerVotante(dni)
            return votante[5]

    @classmethod
    def votar(cls, dni):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ACTUALIZAR_YA_VOTO, (True, dni))
            return cursor.fetchone()

    @classmethod
    def saberSiVoto(cls, dni):
        if cls.existeVotante(dni):
            votante = cls.obtenerVotante(dni)
            return votante[6]

    @classmethod
    def saberSiTieneEnfPrevia(cls, dni):
        votante = cls.obtenerVotante(dni)
        return votante[3]

    @classmethod
    def saberSiTrabaja(cls, dni):
        votante = cls.obtenerVotante(dni)
        return votante[4]

    @classmethod
    def tieneTurno(cls, dni):
        with CursorDelPool() as cursor:
            votanteAbuscar = 'SELECT * FROM votantes WHERE dni=%s'
            cursor.execute(votanteAbuscar, (dni,))
            votante = cursor.fetchone()
            return votante[7]

    @classmethod
    def obtenerVotantes(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            return cursor.fetchall()

    @classmethod
    def cantVotantesConTurno(cls):
        result = 0
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            votantes = cursor.fetchall()
            for votante in votantes:
                if cls.tieneTurno(votante[0]):
                    result += 1
        return result
