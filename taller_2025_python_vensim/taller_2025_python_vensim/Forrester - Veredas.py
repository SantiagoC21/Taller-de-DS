"""
Python model 'Forrester - Veredas.py'
Translated using PySD
"""

from pathlib import Path
import numpy as np

from pysd.py_backend.statefuls import Integ
from pysd import Component

__pysd_version__ = "3.14.2"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent


component = Component()

#######################################################################
#                          CONTROL VARIABLES                          #
#######################################################################

_control_vars = {
    "initial_time": lambda: 2022,
    "final_time": lambda: 2032,
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
    name="FINAL TIME", units="Año", comp_type="Constant", comp_subtype="Normal"
)
def final_time():
    """
    El período final de la simulación.
    """
    return __data["time"].final_time()


@component.add(
    name="INITIAL TIME", units="Año", comp_type="Constant", comp_subtype="Normal"
)
def initial_time():
    """
    El período inicial de la simulación.
    """
    return __data["time"].initial_time()


@component.add(
    name="SAVEPER",
    units="Año",
    limits=(0.0, np.nan),
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time_step": 1},
)
def saveper():
    """
    La frecuencia con la que se almacena la salida.
    """
    return __data["time"].saveper()


@component.add(
    name="TIME STEP",
    units="Año",
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
    name="Gastos Totales Veredas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"veredas_en_construccion": 1, "mantenimiento_veredas": 1},
)
def gastos_totales_veredas():
    return veredas_en_construccion() * 1200 + mantenimiento_veredas()


@component.add(
    name="Mantenimiento Veredas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"veredas_construidas": 1},
)
def mantenimiento_veredas():
    return veredas_construidas() * 12


@component.add(
    name="Tasa Veredas Construccion", comp_type="Constant", comp_subtype="Normal"
)
def tasa_veredas_construccion():
    return 0.05


@component.add(
    name="Tasa Veredas Obsoletas", comp_type="Constant", comp_subtype="Normal"
)
def tasa_veredas_obsoletas():
    return 0.008


@component.add(
    name="Veredas Construidas",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_veredas_construidas": 1},
    other_deps={
        "_integ_veredas_construidas": {
            "initial": {},
            "step": {"veredas_en_construccion": 1, "veredas_obsoletas": 1},
        }
    },
)
def veredas_construidas():
    return _integ_veredas_construidas()


_integ_veredas_construidas = Integ(
    lambda: veredas_en_construccion() - veredas_obsoletas(),
    lambda: 100,
    "_integ_veredas_construidas",
)


@component.add(
    name="Veredas en construccion",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"veredas_construidas": 1, "tasa_veredas_construccion": 1},
)
def veredas_en_construccion():
    return veredas_construidas() * tasa_veredas_construccion()


@component.add(
    name="Veredas obsoletas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"veredas_construidas": 1, "tasa_veredas_obsoletas": 1},
)
def veredas_obsoletas():
    return veredas_construidas() * tasa_veredas_obsoletas()
