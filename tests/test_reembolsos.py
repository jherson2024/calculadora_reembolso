from src.domain.models import Reserva
from src.services.reembolso_service import calcular_reembolso


# -----------------------------
# Clases de equivalencia válidas
# -----------------------------

def test_reembolso_100_por_ciento():
    """
    Cancelación con mucha antelación (>72h)
    """
    r = Reserva(200, 80, False)
    assert calcular_reembolso(r) == 200


def test_reembolso_50_por_ciento():
    """
    Cancelación entre 24 y 72 horas
    """
    r = Reserva(200, 48, False)
    assert calcular_reembolso(r) == 100


def test_reembolso_0_por_ciento():
    """
    Cancelación de última hora (<24h)
    """
    r = Reserva(200, 10, False)
    assert calcular_reembolso(r) == 0


# -----------------------------
# Regla VIP (prioridad)
# -----------------------------

def test_vip_ultima_hora_recibe_50():
    """
    VIP siempre recibe al menos 50%
    """
    r = Reserva(200, 2, True)
    assert calcular_reembolso(r) == 100


def test_vip_en_rango_medio():
    """
    VIP en rango medio no cambia (ya es 50%)
    """
    r = Reserva(200, 30, True)
    assert calcular_reembolso(r) == 100


def test_vip_con_reembolso_total():
    """
    VIP con >72h mantiene 100%
    """
    r = Reserva(200, 80, True)
    assert calcular_reembolso(r) == 200


# -----------------------------
# Valores límite (Myers)
# -----------------------------

def test_limite_24_horas():
    r = Reserva(200, 24, False)
    assert calcular_reembolso(r) == 100


def test_limite_72_horas():
    r = Reserva(200, 72, False)
    assert calcular_reembolso(r) == 100


def test_limite_23_horas():
    r = Reserva(200, 23, False)
    assert calcular_reembolso(r) == 0


def test_limite_73_horas():
    r = Reserva(200, 73, False)
    assert calcular_reembolso(r) == 200