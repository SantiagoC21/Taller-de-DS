"""
Python model 'frecuencia de mantenimiento.py'
Translated using PySD
"""

from pathlib import Path
import numpy as np

from pysd.py_backend.statefuls import Integ
from pysd import Component

__pysd_version__ = "3.14.3"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent


component = Component()

#######################################################################
#                          CONTROL VARIABLES                          #
#######################################################################

_control_vars = {
    "initial_time": lambda: 0,
    "final_time": lambda: 100,
    "time_step": lambda: 1,
    "saveper": lambda: time_step(),
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


@component.add(name="Time")
def time():
    """
    Current time of the model.
    """
    return __data["time"]()


@component.add(
    name="FINAL TIME", units="Week", comp_type="Constant", comp_subtype="Normal"
)
def final_time():
    """
    The final time for the simulation.
    """
    return __data["time"].final_time()


@component.add(
    name="INITIAL TIME", units="Week", comp_type="Constant", comp_subtype="Normal"
)
def initial_time():
    """
    The initial time for the simulation.
    """
    return __data["time"].initial_time()


@component.add(
    name="SAVEPER",
    units="Week",
    limits=(0.0, np.nan),
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time_step": 1},
)
def saveper():
    """
    The frequency with which output is stored.
    """
    return __data["time"].saveper()


@component.add(
    name="TIME STEP",
    units="Week",
    limits=(0.0, np.nan),
    comp_type="Constant",
    comp_subtype="Normal",
)
def time_step():
    """
    The time step for the simulation.
    """
    return __data["time"].time_step()


#######################################################################
#                           MODEL VARIABLES                           #
#######################################################################


@component.add(
    name="Cantidad de fallas mecanicas",
    units="Unidades",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cantidad_de_fallas_mecanicas": 1},
    other_deps={
        "_integ_cantidad_de_fallas_mecanicas": {
            "initial": {},
            "step": {
                "numero_de_veces_que_ocurre_una_falla_mecanica": 1,
                "cantidad_de_reparaciones_preventivas": 1,
                "reparacion_de_fallas_mecanicas": 1,
            },
        }
    },
)
def cantidad_de_fallas_mecanicas():
    return _integ_cantidad_de_fallas_mecanicas()


_integ_cantidad_de_fallas_mecanicas = Integ(
    lambda: numero_de_veces_que_ocurre_una_falla_mecanica()
    - cantidad_de_reparaciones_preventivas()
    - reparacion_de_fallas_mecanicas(),
    lambda: 0,
    "_integ_cantidad_de_fallas_mecanicas",
)


@component.add(
    name="Cantidad de malas maniobras",
    units="Unidades",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cantidad_promedio_de_malas_maniobras_por_vehiculo": 1,
        "cantidad_de_vehiculos_en_operacion": 1,
    },
)
def cantidad_de_malas_maniobras():
    return (
        cantidad_promedio_de_malas_maniobras_por_vehiculo()
        * cantidad_de_vehiculos_en_operacion()
    )


@component.add(
    name="Cantidad de plazas apartadas por mantenimiento",
    units="Plazas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demanda_por_mantenimiento": 1,
        "capacidad_de_atencion_por_plaza": 1,
        "disponibilidad_de_talleres": 1,
    },
)
def cantidad_de_plazas_apartadas_por_mantenimiento():
    return float(
        np.maximum(
            demanda_por_mantenimiento() / capacidad_de_atencion_por_plaza(),
            disponibilidad_de_talleres(),
        )
    )


@component.add(
    name="Cantidad de plazas ocupadas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_de_plazas": 1, "disponibilidad_de_talleres": 1},
)
def cantidad_de_plazas_ocupadas():
    return total_de_plazas() - disponibilidad_de_talleres()


@component.add(
    name="Cantidad de plazas sin asignacion de mantenimiento",
    units="Plazas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cantidad_de_plazas_ocupadas": 1, "tasa_de_liberacion_de_plazas": 1},
)
def cantidad_de_plazas_sin_asignacion_de_mantenimiento():
    return cantidad_de_plazas_ocupadas() * tasa_de_liberacion_de_plazas()


@component.add(
    name="Cantidad de reparaciones preventivas",
    units="Unidades",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cantidad_de_fallas_mecanicas": 1,
        "cantidad_de_vehiculos_destinados_a_mantenimiento_preventivo": 1,
    },
)
def cantidad_de_reparaciones_preventivas():
    return (
        cantidad_de_fallas_mecanicas()
        * cantidad_de_vehiculos_destinados_a_mantenimiento_preventivo()
    )


@component.add(
    name="Cantidad de vehiculos destinados a mantenimiento correctivo",
    units="Vehiculos",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "proporcion_de_vehiculos_que_van_a_mantenimiento_correctivo": 1,
        "vehiculos_que_se_retiran_por_mantenimiento": 1,
    },
)
def cantidad_de_vehiculos_destinados_a_mantenimiento_correctivo():
    return (
        proporcion_de_vehiculos_que_van_a_mantenimiento_correctivo()
        * vehiculos_que_se_retiran_por_mantenimiento()
    )


@component.add(
    name="Cantidad de vehiculos destinados a mantenimiento preventivo",
    units="Vehiculos",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "vehiculos_que_se_retiran_por_mantenimiento": 1,
        "proporcion_de_vehiculos_que_van_a_mantenimiento_correctivo": 1,
    },
)
def cantidad_de_vehiculos_destinados_a_mantenimiento_preventivo():
    return vehiculos_que_se_retiran_por_mantenimiento() * (
        1 - proporcion_de_vehiculos_que_van_a_mantenimiento_correctivo()
    )


@component.add(
    name="Cantidad de vehiculos en mantenimiento",
    units="Vehiculos",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_de_la_flota": 1, "disponibilidad_de_la_flota": 1},
)
def cantidad_de_vehiculos_en_mantenimiento():
    return total_de_la_flota() - disponibilidad_de_la_flota()


@component.add(
    name="Cantidad de vehiculos en operacion",
    units="Vehiculos",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cantidad_de_vehiculos_en_operacion": 1},
    other_deps={
        "_integ_cantidad_de_vehiculos_en_operacion": {
            "initial": {},
            "step": {
                "vehiculos_asignados_a_operar": 1,
                "vehiculos_devueltos_al_deposito": 1,
            },
        }
    },
)
def cantidad_de_vehiculos_en_operacion():
    return _integ_cantidad_de_vehiculos_en_operacion()


_integ_cantidad_de_vehiculos_en_operacion = Integ(
    lambda: vehiculos_asignados_a_operar() - vehiculos_devueltos_al_deposito(),
    lambda: 30,
    "_integ_cantidad_de_vehiculos_en_operacion",
)


@component.add(
    name="Cantidad de vehiculos que terminan el mantenimiento por semana",
    units="Vehiculos",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cantidad_de_vehiculos_que_terminan_el_mantenimiento_por_semana():
    return 20


@component.add(
    name="Cantidad promedio de malas maniobras por vehiculo",
    units="Unidades",
    comp_type="Constant",
    comp_subtype="Normal",
)
def cantidad_promedio_de_malas_maniobras_por_vehiculo():
    return 15


@component.add(
    name="Capacidad de atencion por plaza",
    units="Plazas",
    comp_type="Constant",
    comp_subtype="Normal",
)
def capacidad_de_atencion_por_plaza():
    return 1


@component.add(
    name="Demanda de operacion",
    units="Vehiculos",
    comp_type="Constant",
    comp_subtype="Normal",
)
def demanda_de_operacion():
    return 30


@component.add(
    name="Demanda por mantenimiento",
    units="Plazas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cantidad_de_vehiculos_destinados_a_mantenimiento_correctivo": 1,
        "cantidad_de_vehiculos_destinados_a_mantenimiento_preventivo": 1,
    },
)
def demanda_por_mantenimiento():
    return (
        cantidad_de_vehiculos_destinados_a_mantenimiento_correctivo()
        + cantidad_de_vehiculos_destinados_a_mantenimiento_preventivo()
    )


@component.add(
    name="Disponibilidad de la flota",
    units="Vehiculos",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_disponibilidad_de_la_flota": 1},
    other_deps={
        "_integ_disponibilidad_de_la_flota": {
            "initial": {},
            "step": {
                "vehiculos_que_regresan_de_mantenimiento": 1,
                "vehiculos_asignados_a_operar": 1,
                "vehiculos_que_se_retiran_por_mantenimiento": 1,
            },
        }
    },
)
def disponibilidad_de_la_flota():
    return _integ_disponibilidad_de_la_flota()


_integ_disponibilidad_de_la_flota = Integ(
    lambda: vehiculos_que_regresan_de_mantenimiento()
    - vehiculos_asignados_a_operar()
    - vehiculos_que_se_retiran_por_mantenimiento(),
    lambda: 0,
    "_integ_disponibilidad_de_la_flota",
)


@component.add(
    name="Disponibilidad de talleres",
    units="Plazas",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_disponibilidad_de_talleres": 1},
    other_deps={
        "_integ_disponibilidad_de_talleres": {
            "initial": {},
            "step": {
                "cantidad_de_plazas_sin_asignacion_de_mantenimiento": 1,
                "cantidad_de_plazas_apartadas_por_mantenimiento": 1,
            },
        }
    },
)
def disponibilidad_de_talleres():
    return _integ_disponibilidad_de_talleres()


_integ_disponibilidad_de_talleres = Integ(
    lambda: cantidad_de_plazas_sin_asignacion_de_mantenimiento()
    - cantidad_de_plazas_apartadas_por_mantenimiento(),
    lambda: 40,
    "_integ_disponibilidad_de_talleres",
)


@component.add(
    name="Numero de veces que ocurre una falla mecanica",
    units="Unidades",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"tasa_de_fallas_mecanicas": 1, "cantidad_de_malas_maniobras": 1},
)
def numero_de_veces_que_ocurre_una_falla_mecanica():
    return tasa_de_fallas_mecanicas() * cantidad_de_malas_maniobras()


@component.add(
    name="Proporcion de vehiculos que van a mantenimiento correctivo",
    comp_type="Constant",
    comp_subtype="Normal",
)
def proporcion_de_vehiculos_que_van_a_mantenimiento_correctivo():
    return 0.4


@component.add(
    name="Reparacion de fallas mecanicas",
    units="Unidades",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cantidad_de_fallas_mecanicas": 1,
        "cantidad_de_vehiculos_destinados_a_mantenimiento_correctivo": 1,
    },
)
def reparacion_de_fallas_mecanicas():
    return (
        cantidad_de_fallas_mecanicas()
        * cantidad_de_vehiculos_destinados_a_mantenimiento_correctivo()
    )


@component.add(name="Tasa de asignacion", comp_type="Constant", comp_subtype="Normal")
def tasa_de_asignacion():
    return 0.7


@component.add(
    name="Tasa de fallas mecanicas", comp_type="Constant", comp_subtype="Normal"
)
def tasa_de_fallas_mecanicas():
    return 0.05


@component.add(
    name="Tasa de inoperatividad por fallas",
    comp_type="Constant",
    comp_subtype="Normal",
)
def tasa_de_inoperatividad_por_fallas():
    return 0.05


@component.add(
    name="Tasa de liberacion de plazas",
    units="Vehiculos/Semanas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cantidad_de_vehiculos_que_terminan_el_mantenimiento_por_semana": 1,
        "tiempo_promedio_de_mantenimiento": 1,
    },
)
def tasa_de_liberacion_de_plazas():
    return (
        cantidad_de_vehiculos_que_terminan_el_mantenimiento_por_semana()
        / tiempo_promedio_de_mantenimiento()
    )


@component.add(
    name="Tasa de retorno al deposito", comp_type="Constant", comp_subtype="Normal"
)
def tasa_de_retorno_al_deposito():
    return 0.1


@component.add(
    name="Tiempo promedio de mantenimiento",
    units="Semanas",
    comp_type="Constant",
    comp_subtype="Normal",
)
def tiempo_promedio_de_mantenimiento():
    return 2


@component.add(
    name="Total de la flota",
    units="Vehiculos",
    comp_type="Constant",
    comp_subtype="Normal",
)
def total_de_la_flota():
    return 50


@component.add(name="Total de plazas", comp_type="Constant", comp_subtype="Normal")
def total_de_plazas():
    return 40


@component.add(
    name="Vehiculos asignados a operar",
    units="Vehiculos",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demanda_de_operacion": 1,
        "tasa_de_asignacion": 1,
        "disponibilidad_de_la_flota": 1,
    },
)
def vehiculos_asignados_a_operar():
    return float(
        np.minimum(
            demanda_de_operacion(), disponibilidad_de_la_flota() * tasa_de_asignacion()
        )
    )


@component.add(
    name="Vehiculos devueltos al deposito",
    units="Vehiculos",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cantidad_de_vehiculos_en_operacion": 1,
        "tasa_de_retorno_al_deposito": 1,
    },
)
def vehiculos_devueltos_al_deposito():
    return cantidad_de_vehiculos_en_operacion() * tasa_de_retorno_al_deposito()


@component.add(
    name="Vehiculos operativos que mostraron fallas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cantidad_de_vehiculos_en_operacion": 1, "tasa_de_fallas_mecanicas": 1},
)
def vehiculos_operativos_que_mostraron_fallas():
    return cantidad_de_vehiculos_en_operacion() * tasa_de_fallas_mecanicas()


@component.add(
    name="Vehiculos que regresan de mantenimiento",
    units="Vehiculos",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cantidad_de_vehiculos_en_mantenimiento": 1,
        "tiempo_promedio_de_mantenimiento": 1,
    },
)
def vehiculos_que_regresan_de_mantenimiento():
    return cantidad_de_vehiculos_en_mantenimiento() / tiempo_promedio_de_mantenimiento()


@component.add(
    name="Vehiculos que se retiran por mantenimiento",
    units="Vehiculos",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "tasa_de_inoperatividad_por_fallas": 1,
        "vehiculos_operativos_que_mostraron_fallas": 1,
    },
)
def vehiculos_que_se_retiran_por_mantenimiento():
    return (
        tasa_de_inoperatividad_por_fallas()
        * vehiculos_operativos_que_mostraron_fallas()
    )
