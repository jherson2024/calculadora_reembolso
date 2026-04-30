def calcular_porcentaje_base(horas: int) -> float:
    """
    Calcula el porcentaje base de reembolso según las horas de anticipación.

    Reglas:
    - > 72 horas → 100%
    - 24 a 72 horas → 50%
    - < 24 horas → 0%
    """
    if horas > 72:
        return 1.0
    elif 24 <= horas <= 72:
        return 0.5
    else:
        return 0.0


def aplicar_regla_vip(porcentaje: float, es_vip: bool) -> float:
    """
    Aplica la regla VIP:
    - Un cliente VIP recibe al menos 50% de reembolso.
    """
    if es_vip and porcentaje < 0.5:
        return 0.5
    return porcentaje