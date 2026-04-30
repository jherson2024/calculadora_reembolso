from src.domain.models import Reserva
from src.domain.rules import calcular_porcentaje_base, aplicar_regla_vip
from src.exceptions import MontoInvalidoError, HorasInvalidasError


def calcular_reembolso(reserva: Reserva) -> float:
    """
    Calcula el monto de reembolso para una reserva.

    Flujo:
    1. Validaciones (robustez)
    2. Cálculo del porcentaje base
    3. Aplicación de regla VIP
    4. Resultado final
    """

    # --- Validaciones (TDD - robustez) ---
    if reserva.monto < 0:
        raise MontoInvalidoError("El monto no puede ser negativo")

    if reserva.horas_anticipacion < 0:
        raise HorasInvalidasError("Las horas no pueden ser negativas")

    # --- Reglas de negocio ---
    porcentaje = calcular_porcentaje_base(reserva.horas_anticipacion)
    porcentaje = aplicar_regla_vip(porcentaje, reserva.es_vip)

    # --- Resultado ---
    reembolso = reserva.monto * porcentaje

    return reembolso