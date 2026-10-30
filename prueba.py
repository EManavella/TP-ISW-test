import pytest
from DestinoFinal import condicion_final
 
# ---- 1) Pruebas por TABLA DE DECISIÓN ---------------

TABLA_DECISION = [
    # (Id, regularidad, AD, TPs, asistencia, resultado esperado)
    ("R1",  8, 8, True,  90, "Promocionado"), 
    ("R2",  8, 4, True,  90, "Regular"),
    ("R5a", 8, 8, True,  50, "Libre"),
    ("R5b", 8, 4, True,  50, "Libre"),
    ("R4a", 8, 8, False, 90, "Libre"),
    ("R4b", 8, 4, False, 90, "Libre"),
    ("R4c", 8, 8, False, 50, "Libre"),
    ("R4d", 8, 4, False, 50, "Libre"),
    ("R3a", 4, 8, True,  90, "Libre"),
    ("R3b", 4, 4, True,  90, "Libre"),
    ("R3c", 4, 8, True,  50, "Libre"),
    ("R3d", 4, 4, True,  50, "Libre"),
    ("R3e", 4, 8, False, 90, "Libre"),
    ("R3f", 4, 4, False, 90, "Libre"),
    ("R3g", 4, 8, False, 50, "Libre"),
    ("R3h", 4, 4, False, 50, "Libre"),
]
 
@pytest.mark.parametrize(
    "id, reg, ad, tps, asistencia, esperado",
    TABLA_DECISION,
    ids=[fila[0] for fila in TABLA_DECISION],
)
def test_tabla_de_decision(id, reg, ad, tps, asistencia, esperado):
    assert condicion_final(reg, ad, tps, asistencia) == esperado
 
 
# ---- 2) Pruebas por VALORES LÍMITE ------------------------------------------

VALORES_LIMITE = [
    # (Id, regularidad, AD, TPs, asistencia, esperado)
    # Limite de la regularidad (6)
    ("C1a", 5,      8, True, 90, "Libre"),
    ("C1b", 5.99,   8, True, 90, "Libre"),
    ("C1c", 6,      4, True, 90, "Regular"),
    ("C1d", 6.01,   4, True, 90, "Regular"),

    # Limite de AD (6)
    ("C4a", 8,  5,    True, 90, "Regular"),
    ("C4b", 8,  5.99, True, 90, "Regular"),
    ("C4c", 8,  6,    True, 90, "Promocionado"),
    ("C4d", 8,  6.01, True, 90, "Promocionado"),

    # Limite de asistencia (75)
    ("C2a", 8,  4, True, 74,   "Libre"),
    ("C2b", 8,  4, True, 74.9, "Libre"),
    ("C2c", 8,  4, True, 75,   "Regular"),
    ("C2d", 8,  8, True, 75,   "Promocionado"),
    ("C2e", 8,  4, True, 76,   "Regular"),

    # Extremos validos del dominio
    ("C*a", 0,  0,  False, 0,   "Libre"),
    ("C*b", 10, 10, True,  100, "Promocionado"),
]
 
 
@pytest.mark.parametrize(
    "id, reg, ad, tps, asistencia, esperado",
    VALORES_LIMITE,
    ids=[fila[0] for fila in VALORES_LIMITE],
)
def test_valores_limite(id, reg, ad, tps, asistencia, esperado):
    assert condicion_final(reg, ad, tps, asistencia) == esperado
 