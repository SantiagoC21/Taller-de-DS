"""
Python model 'Forrester - Losas.py'
Translated using PySD
"""

from pathlib import Path
import numpy as np

from pysd.py_backend.functions import integer
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
    name="Gastos Totales Losas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"losas_en_contruccion": 1, "mantenimiento_losas": 1},
)
def gastos_totales_losas():
    return losas_en_contruccion() * 1200 + mantenimiento_losas()


@component.add(
    name="Losas Deportivas Construidas",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_losas_deportivas_construidas": 1},
    other_deps={
        "_integ_losas_deportivas_construidas": {
            "initial": {},
            "step": {"losas_en_contruccion": 1, "losas_obsoletas": 1},
        }
    },
)
def losas_deportivas_construidas():
    return _integ_losas_deportivas_construidas()


_integ_losas_deportivas_construidas = Integ(
    lambda: losas_en_contruccion() - losas_obsoletas(),
    lambda: 90,
    "_integ_losas_deportivas_construidas",
)


@component.add(
    name="Losas en contruccion",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"losas_deportivas_construidas": 1, "tasa_losas_construccion": 1},
)
def losas_en_contruccion():
    return integer(losas_deportivas_construidas() * tasa_losas_construccion())


@component.add(
    name="Losas obsoletas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"losas_deportivas_construidas": 1, "tasa_losas_obsoletas": 1},
)
def losas_obsoletas():
    return integer(losas_deportivas_construidas() * tasa_losas_obsoletas())


@component.add(
    name="Mantenimiento Losas",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"losas_deportivas_construidas": 1},
)
def mantenimiento_losas():
    return losas_deportivas_construidas() * 12


@component.add(
    name="Tasa Losas Construccion", comp_type="Constant", comp_subtype="Normal"
)
def tasa_losas_construccion():
    return 0.02


@component.add(name="Tasa Losas Obsoletas", comp_type="Constant", comp_subtype="Normal")
def tasa_losas_obsoletas():
    return 0.009
