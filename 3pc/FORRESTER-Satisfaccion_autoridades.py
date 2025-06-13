"""
Python model 'FORRESTER-Satisfaccion_autoridades.py'
Translated using PySD
"""

from pathlib import Path
import numpy as np

from pysd.py_backend.functions import integer
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
    "initial_time": lambda: 2015,
    "final_time": lambda: 2028,
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
    name="FINAL TIME", units="Month", comp_type="Constant", comp_subtype="Normal"
)
def final_time():
    """
    The final time for the simulation.
    """
    return __data["time"].final_time()


@component.add(
    name="INITIAL TIME", units="Month", comp_type="Constant", comp_subtype="Normal"
)
def initial_time():
    """
    The initial time for the simulation.
    """
    return __data["time"].initial_time()


@component.add(
    name="SAVEPER",
    units="Month",
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
    units="Month",
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
    name="Cantidad de accidentes",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "porcentaje_de_congestion_vehicular": 1,
        "tasa_de_fluidez_del_trafico": 1,
        "discrepacia": 1,
    },
)
def cantidad_de_accidentes():
    return integer(
        (
            porcentaje_de_congestion_vehicular() * 0.05
            + (1 - tasa_de_fluidez_del_trafico()) * 0.02
        )
        * discrepacia()
    )


@component.add(name="Objetivo", comp_type="Constant", comp_subtype="Normal")
def objetivo():
    return 600


@component.add(
    name="Discrepacia",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"objetivo": 1, "accidentes_de_transito": 1},
)
def discrepacia():
    return float(np.abs(integer(objetivo() - accidentes_de_transito())))


@component.add(
    name='"Error / Faltante"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"objetivo": 1, "accidentes_de_transito": 1},
)
def error_faltante():
    return float(np.abs(objetivo() - accidentes_de_transito()))


@component.add(
    name="Accidentes de tránsito",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_accidentes_de_transito": 1},
    other_deps={
        "_integ_accidentes_de_transito": {
            "initial": {},
            "step": {"cantidad_de_accidentes": 1, "accidentes_prevenidos": 1},
        }
    },
)
def accidentes_de_transito():
    return _integ_accidentes_de_transito()


_integ_accidentes_de_transito = Integ(
    lambda: integer(cantidad_de_accidentes() - accidentes_prevenidos()),
    lambda: 1000,
    "_integ_accidentes_de_transito",
)


@component.add(
    name="Calidad de infraestructura vial",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_calidad_de_infraestructura_vial": 1},
    other_deps={
        "_integ_calidad_de_infraestructura_vial": {
            "initial": {},
            "step": {"mejora_de_infraestructura": 1, "deterioro_de_infraestructura": 1},
        }
    },
)
def calidad_de_infraestructura_vial():
    return _integ_calidad_de_infraestructura_vial()


_integ_calidad_de_infraestructura_vial = Integ(
    lambda: mejora_de_infraestructura() - deterioro_de_infraestructura(),
    lambda: 50,
    "_integ_calidad_de_infraestructura_vial",
)


@component.add(
    name="Confianza pública",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_confianza_publica": 1},
    other_deps={
        "_integ_confianza_publica": {
            "initial": {},
            "step": {"recuperacion_de_confianza": 1, "perdida_de_confianza": 1},
        }
    },
)
def confianza_publica():
    return _integ_confianza_publica()


_integ_confianza_publica = Integ(
    lambda: recuperacion_de_confianza() - perdida_de_confianza(),
    lambda: 0.5,
    "_integ_confianza_publica",
)


@component.add(
    name="Porcentaje de congestion vehicular",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"calidad_de_infraestructura_vial": 1},
)
def porcentaje_de_congestion_vehicular():
    return 1 - calidad_de_infraestructura_vial() * 0.01


@component.add(
    name="Depreciacion de inversion",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"inversion_en_infraestructura": 1},
)
def depreciacion_de_inversion():
    return inversion_en_infraestructura() * 5e-06


@component.add(
    name="Deterioro de imagen",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"quejas_de_usuarios": 1},
)
def deterioro_de_imagen():
    return quejas_de_usuarios() * 0.05


@component.add(
    name="Deterioro de infraestructura",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"calidad_de_infraestructura_vial": 1},
)
def deterioro_de_infraestructura():
    return calidad_de_infraestructura_vial() * 0.03


@component.add(
    name="Accidentes prevenidos",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"accidentes_de_transito": 1, "total_regulaciones_viales": 1},
)
def accidentes_prevenidos():
    return integer(accidentes_de_transito() * total_regulaciones_viales() * 0.01)


@component.add(
    name="Tasa de fluidez del trafico",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"porcentaje_de_congestion_vehicular": 1},
)
def tasa_de_fluidez_del_trafico():
    return 1 / (1 + porcentaje_de_congestion_vehicular())


@component.add(
    name="Flujo de inversion",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"tasa_de_recaudacion": 1, "porcentaje_de_inversion": 1},
)
def flujo_de_inversion():
    return tasa_de_recaudacion() * porcentaje_de_inversion()


@component.add(
    name="Imagen pública de autoridades",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_imagen_publica_de_autoridades": 1},
    other_deps={
        "_integ_imagen_publica_de_autoridades": {
            "initial": {},
            "step": {"mejora_de_imagen": 1, "deterioro_de_imagen": 1},
        }
    },
)
def imagen_publica_de_autoridades():
    return _integ_imagen_publica_de_autoridades()


_integ_imagen_publica_de_autoridades = Integ(
    lambda: mejora_de_imagen() - deterioro_de_imagen(),
    lambda: 0.5,
    "_integ_imagen_publica_de_autoridades",
)


@component.add(
    name="Infracciones vehiculares",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_regulaciones_viales": 1},
)
def infracciones_vehiculares():
    return float(np.maximum(0, 1 - total_regulaciones_viales() * 0.05))


@component.add(
    name="Inversion en infraestructura",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_inversion_en_infraestructura": 1},
    other_deps={
        "_integ_inversion_en_infraestructura": {
            "initial": {},
            "step": {"flujo_de_inversion": 1, "depreciacion_de_inversion": 1},
        }
    },
)
def inversion_en_infraestructura():
    return _integ_inversion_en_infraestructura()


_integ_inversion_en_infraestructura = Integ(
    lambda: flujo_de_inversion() - depreciacion_de_inversion(),
    lambda: 10000,
    "_integ_inversion_en_infraestructura",
)


@component.add(
    name="Mejora de imagen",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "satisfaccion_de_usuarios": 1,
        "satisfaccion_de_autoridades_de_transporte": 1,
    },
)
def mejora_de_imagen():
    return (
        (satisfaccion_de_usuarios() + satisfaccion_de_autoridades_de_transporte())
        / 2
        * 0.03
    )


@component.add(
    name="Mejora de infraestructura",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"flujo_de_inversion": 1},
)
def mejora_de_infraestructura():
    return flujo_de_inversion() * 0.7


@component.add(
    name="Pagos de tributos de transporte",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"infracciones_vehiculares": 1},
)
def pagos_de_tributos_de_transporte():
    return infracciones_vehiculares() * 0.5


@component.add(
    name="Perdida de confianza",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"accidentes_de_transito": 1},
)
def perdida_de_confianza():
    return accidentes_de_transito() * 5e-05


@component.add(
    name="Porcentaje de inversion", comp_type="Constant", comp_subtype="Normal"
)
def porcentaje_de_inversion():
    return 0.3


@component.add(
    name="Quejas de usuarios",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"tasa_de_quejas_de_usuarios": 1},
)
def quejas_de_usuarios():
    return tasa_de_quejas_de_usuarios() * 100


@component.add(
    name="Recuperacion de confianza",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "satisfaccion_de_usuarios": 1,
        "satisfaccion_de_autoridades_de_transporte": 1,
    },
)
def recuperacion_de_confianza():
    return (
        (satisfaccion_de_usuarios() + satisfaccion_de_autoridades_de_transporte())
        / 2
        * 0.04
    )


@component.add(
    name="Satisfaccion de autoridades de transporte",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"tasa_de_viajes_de_transporte": 1},
)
def satisfaccion_de_autoridades_de_transporte():
    return tasa_de_viajes_de_transporte() * 0.05


@component.add(
    name="Satisfaccion de usuarios",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "calidad_de_infraestructura_vial": 1,
        "porcentaje_de_congestion_vehicular": 1,
    },
)
def satisfaccion_de_usuarios():
    return (
        calidad_de_infraestructura_vial() * 0.05
        - porcentaje_de_congestion_vehicular() * 0.03
    )


@component.add(
    name="Tasa de quejas de usuarios",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"satisfaccion_de_usuarios": 1},
)
def tasa_de_quejas_de_usuarios():
    return float(np.maximum(0, 1 - satisfaccion_de_usuarios()))


@component.add(name="Tasa de recaudacion", comp_type="Constant", comp_subtype="Normal")
def tasa_de_recaudacion():
    return 25


@component.add(
    name="Tasa de viajes de transporte",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"tasa_de_fluidez_del_trafico": 1, "pagos_de_tributos_de_transporte": 1},
)
def tasa_de_viajes_de_transporte():
    return tasa_de_fluidez_del_trafico() * 0.1 + pagos_de_tributos_de_transporte() * 0.1


@component.add(
    name="Total regulaciones viales",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"calidad_de_infraestructura_vial": 1},
)
def total_regulaciones_viales():
    return 1 + calidad_de_infraestructura_vial() * 0.05
