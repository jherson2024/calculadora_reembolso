class ReembolsoError(Exception):
    """
    Excepción base para errores de reembolsos.
    """
    pass


class MontoInvalidoError(ReembolsoError):
    """
    Se lanza cuando el monto de la reserva es inválido.
    """
    pass


class HorasInvalidasError(ReembolsoError):
    """
    Se lanza cuando las horas de anticipación son inválidas.
    """
    pass