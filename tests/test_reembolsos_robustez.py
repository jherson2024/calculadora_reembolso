import pytest
from src.domain.models import Reserva
from src.services.reembolso_service import calcular_reembolso
from src.exceptions import MontoInvalidoError, HorasInvalidasError


# -----------------------------
# Casos inválidos (robustez)
# -----------------------------

def test_monto_negativo_lanza_error():
    """
    El sistema debe rechazar montos negativos
    """
    with pytest.raises(MontoInvalidoError):
        calcular_reembolso(Reserva(-100, 48, False))


def test_horas_negativas_lanza_error():
    """
    El sistema debe rechazar horas negativas
    """
    with pytest.raises(HorasInvalidasError):
        calcular_reembolso(Reserva(100, -5, False))


def test_monto_cero_valido():
    """
    Caso borde: monto 0 debe devolver 0
    """
    r = Reserva(0, 48, False)
    assert calcular_reembolso(r) == 0


def test_horas_extremadamente_grandes():
    """
    Robustez: valores grandes siguen funcionando
    """
    r = Reserva(200, 10000, False)
    assert calcular_reembolso(r) == 200