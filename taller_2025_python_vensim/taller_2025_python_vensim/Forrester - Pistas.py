"""
Python model 'Forrester - Pistas.py'
Translated using PySD
"""

from pathlib import Path

from pysd.py_backend.functions import integer
from pysd.py_backend.statefuls import Integ

__pysd_version__ = "2.2.0"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent

_subscript_dict = {}

_namespace = {
    "TIME": "time",
    "Time": "time",
    "Cantidad de litros de pintura": "cantidad_de_litros_de_pintura",
    "Cantidad de mano de obra persona": "cantidad_de_mano_de_obra_persona",
    "Cantidad de maquinarias total": "cantidad_de_maquinarias_total",
    "Cantidad maquinas asfaltos": "cantidad_maquinas_asfaltos",
    "Monto Total Pistas": "monto_total_pistas",
    "Pistas asfaltadas": "pistas_asfaltadas",
    "Pistas Construidas": "pistas_construidas",
    "Pistas en construccion": "pistas_en_construccion",
    "Pistas obsoletas": "pistas_obsoletas",
    "Tasa Pistas Construccion": "tasa_pistas_construccion",
    "Tasa Pistas Obsoletas": "tasa_pistas_obsoletas",
    "FINAL TIME": "final_time",
    "INITIAL TIME": "initial_time",
    "SAVEPER": "saveper",
    "TIME STEP": "time_step",
}

_dependencies = {
    "cantidad_de_litros_de_pintura": {"pistas_asfaltadas": 1},
    "cantidad_de_mano_de_obra_persona": {"pistas_asfaltadas": 1},
    "cantidad_de_maquinarias_total": {"pistas_asfaltadas": 1},
    "cantidad_maquinas_asfaltos": {"pistas_asfaltadas": 1},
    "monto_total_pistas": {"pistas_en_construccion": 1},
    "pistas_asfaltadas": {"pistas_construidas": 1},
    "pistas_construidas": {"_integ_pistas_construidas": 1},
    "pistas_en_construccion": {"pistas_construidas": 1, "tasa_pistas_construccion": 1},
    "pistas_obsoletas": {"pistas_construidas": 1, "tasa_pistas_obsoletas": 1},
    "tasa_pistas_construccion": {},
    "tasa_pistas_obsoletas": {},
    "final_time": {},
    "initial_time": {},
    "saveper": {"time_step": 1},
    "time_step": {},
    "_integ_pistas_construidas": {
        "initial": {},
        "step": {"pistas_en_construccion": 1, "pistas_obsoletas": 1},
    },
}

##########################################################################
#                            CONTROL VARIABLES                           #
##########################################################################

_control_vars = {
    "initial_time": lambda: 2022,
    "final_time": lambda: 2032,
    "time_step": lambda: 1,
    "saveper": lambda: time_step(),
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data["time"]()


def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 2032
    Units: Año
    Limits: (None, None)
    Type: constant
    Subs: None

    El período final de la simulación.
    """
    return __data["time"].final_time()


def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 2022
    Units: Año
    Limits: (None, None)
    Type: constant
    Subs: None

    El período inicial de la simulación.
    """
    return __data["time"].initial_time()


def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: Año
    Limits: (0.0, None)
    Type: component
    Subs: None

    La frecuencia con la que se almacena la salida.
    """
    return __data["time"].saveper()


def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 1
    Units: Año
    Limits: (0.0, None)
    Type: constant
    Subs: None

    The time step for the simulation.
    """
    return __data["time"].time_step()


##########################################################################
#                             MODEL VARIABLES                            #
##########################################################################


def cantidad_de_litros_de_pintura():
    """
    Real Name: Cantidad de litros de pintura
    Original Eqn: INTEGER(Pistas asfaltadas*0.6)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return integer(pistas_asfaltadas() * 0.6)


def cantidad_de_mano_de_obra_persona():
    """
    Real Name: Cantidad de mano de obra persona
    Original Eqn: INTEGER(Pistas asfaltadas*0.3)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return integer(pistas_asfaltadas() * 0.3)


def cantidad_de_maquinarias_total():
    """
    Real Name: Cantidad de maquinarias total
    Original Eqn: INTEGER(Pistas asfaltadas*0.5)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return integer(pistas_asfaltadas() * 0.5)


def cantidad_maquinas_asfaltos():
    """
    Real Name: Cantidad maquinas asfaltos
    Original Eqn: INTEGER(Pistas asfaltadas*0.4)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return integer(pistas_asfaltadas() * 0.4)


def monto_total_pistas():
    """
    Real Name: Monto Total Pistas
    Original Eqn: Pistas en construccion*1200
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return pistas_en_construccion() * 1200


def pistas_asfaltadas():
    """
    Real Name: Pistas asfaltadas
    Original Eqn: INTEGER(Pistas Construidas*0.8)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return integer(pistas_construidas() * 0.8)


def pistas_construidas():
    """
    Real Name: Pistas Construidas
    Original Eqn: INTEG ( Pistas en construccion-Pistas obsoletas, 130)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_pistas_construidas()


def pistas_en_construccion():
    """
    Real Name: Pistas en construccion
    Original Eqn: INTEGER(Pistas Construidas*Tasa Pistas Construccion)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return integer(pistas_construidas() * tasa_pistas_construccion())


def pistas_obsoletas():
    """
    Real Name: Pistas obsoletas
    Original Eqn: INTEGER(Pistas Construidas*Tasa Pistas Obsoletas)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return integer(pistas_construidas() * tasa_pistas_obsoletas())


def tasa_pistas_construccion():
    """
    Real Name: Tasa Pistas Construccion
    Original Eqn: 0.03
    Units:
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.03


def tasa_pistas_obsoletas():
    """
    Real Name: Tasa Pistas Obsoletas
    Original Eqn: 0.009
    Units:
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.009


_integ_pistas_construidas = Integ(
    lambda: pistas_en_construccion() - pistas_obsoletas(),
    lambda: 130,
    "_integ_pistas_construidas",
)
