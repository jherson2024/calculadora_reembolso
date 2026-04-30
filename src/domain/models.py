from dataclasses import dataclass

@dataclass
class Reserva:
    """
    Representa una reserva de hotel.

    Atributos:
        monto (float): Monto total de la reserva.
        horas_anticipacion (int): Horas antes de la cancelación.
        es_vip (bool): Indica si el cliente es VIP.
    """
    monto: float
    horas_anticipacion: int
    es_vip: bool