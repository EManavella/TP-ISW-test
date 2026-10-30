
NOTA_MIN = 6
ASISTENCIA_MIN = 75

# Validaciones valores

def _validar_numero(nombre, valor, minimo, maximo):
    if not isinstance(valor, (int, float)) or isinstance(valor, bool):
        raise ValueError(f"{nombre} deve se numerico ")
    if not minimo <= valor <= maximo:
        raise ValueError(f"{nombre} debe estar entre {minimo} y {maximo}")

def _validar(parcial_reg , parcial_ad, tps_aprobados, asistencia):
    
    _validar_numero("parcial_reg", parcial_reg, 0, 10)
    _validar_numero("parcial_ad", parcial_ad, 0, 10)
    _validar_numero("asistencia", asistencia, 0, 100)

    if not isinstance(tps_aprobados, bool):
        raise ValueError("tps_aprobados debe ser True or False")


# Calculo condicion final
def condicion_final(parcial_reg, parcial_ad, tps_aprobados, asistencia):
    _validar(parcial_reg, parcial_ad, tps_aprobados, asistencia)

    es_reg = (
        parcial_reg >= NOTA_MIN
        and tps_aprobados
        and asistencia >= ASISTENCIA_MIN
    )

    if es_reg and parcial_ad >= NOTA_MIN:
        return "Promocionado"
    elif es_reg and parcial_ad < NOTA_MIN:
        return "Regular"
    else:
        return "Libre"

# menu

def _pedir_numero(mensaje):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print (" Entrada invalida: ingrese un numero.")

def _pedir_si_no(mensaje):
    while True:
        texto = input(mensaje).strip().lower()
        if texto in ("s", "si", "sí"):
            return True
        elif texto in ("n", "no"):
            return False
        else:
            print ("  Entrada invalida: ingrese 'si' o 'no'.")

def cargar_notas():
    print("\n--- Carga de datos del alumno ---")
    parcial_reg = _pedir_numero("Ingrese la nota del parcial de regularidad: ")
    if parcial_reg >= NOTA_MIN:
        parcial_ad = _pedir_numero("Ingrese la nota del parcial de AD: ")
    else:
        parcial_ad = 0;
    tps_aprobados = _pedir_si_no("TPs entregados y aprobados? (s/n): ")
    asistencia = _pedir_numero("Ingrese el porcentaje (%) de Asistencia: ")

    try:
        resultado = condicion_final(parcial_reg, parcial_ad, tps_aprobados, asistencia )
        print (f"\n>>> La condicion final del alumno es: {resultado}")
    except ValueError as error:
        print(f"\n [Error] {error}")

if __name__ == "__main__":
    print(condicion_final(8, 7, True, 90))   # PROMOCIONADO
    print(condicion_final(6, 4, True, 80))   # REGULAR
    print(condicion_final(5, 9, True, 80))   # LIBRE