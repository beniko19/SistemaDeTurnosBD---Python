from ConexionBD.conexion import Conexion
from ConexionBD.loggerBase import log


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        #log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipoDeExepcion, valorDeExepcion, traceBackExeption):
        #log.debug('Se ejecuta metodo __exit__')
        if valorDeExepcion:
            self._conexion.rollback()
            log.error(
                f'Ocurrio una excepcion: {valorDeExepcion}, {tipoDeExepcion}, {traceBackExeption}, se hizo rollback')
        else:
            self._conexion.commit()
            #log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
