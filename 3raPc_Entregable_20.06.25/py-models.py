import sys
import os
import sqlite3
import pandas as pd
import numpy as np
import pysd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton,
    QTableWidget, QTableWidgetItem, QLabel, QScrollArea
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# ------------------- Diccionarios -------------------

# modelos_info del código 2 (PySD y SQLite)
modelos_info_simulacion = {
    'Frecuencia de mantenimiento': {
        'mdl_file': 'FORRESTER/frecuencia-de-mantenimiento-forrester.mdl',
        'table': 'Frecuencia_de_mantenimiento',
        'columns_vensim': [
            'Cantidad de fallas mecanicas',
            'Numero de veces que ocurre una falla mecanica',
            'Cantidad de reparaciones preventivas',
            'Reparacion de fallas mecanicas',
            'Cantidad de malas maniobras',
            'Cantidad promedio de malas maniobras por vehiculo',
            'Cantidad de vehiculos en operacion',
            'Vehiculos asignados a operar',
            'Vehiculos devueltos al deposito',
            'Demanda por mantenimiento',
            'Capacidad de atencion por plaza',
            'Cantidad de plazas ocupadas',
            'Cantidad de vehiculos destinados a mantenimiento correctivo',
            'Cantidad de vehiculos destinados a mantenimiento preventivo',
            'Disponibilidad de la flota',
            'Vehiculos que regresan de mantenimiento',
            'Vehiculos que se retiran por mantenimiento',
            'Disponibilidad de talleres',
            'Cantidad de plazas sin asignacion de mantenimiento',
            'Cantidad de plazas apartadas por mantenimiento',
            'Objetivo1',
            'Discrepancia1',
            'Objetivo2',
            'Discrepancia2',
            'Objetivo3',
            'Discrepancia3',
            'Objetivo4',
            'Discrepancia4',
            'Proporcion de vehiculos que van a mantenimiento correctivo',
            'Tasa de asignacion',
            'Tasa de fallas mecanicas',
            'Tasa de inoperatividad por fallas',
            'Tasa de reparacion de fallas mecanicas',
            'Tasa de reparaciones preventivas',
            'Tasa de retorno al deposito',
            'Total de la flota',
            'Cantidad de vehiculos que terminan el mantenimiento por semana',
            'Tasa de liberacion de plazas',
            'Demanda de operacion'
        ],
        'columns_sqlite': [
            
            'Cantidad_de_fallas_mecanicas',
            'Numero_de_veces_que_ocurre_una_falla_mecanica',
            'Cantidad_de_reparaciones_preventivas',
            'Reparacion_de_fallas_mecanicas',
            'Cantidad_de_malas_maniobras',
            'Cantidad_promedio_de_malas_maniobras_por_vehiculo',
            'Cantidad_de_vehiculos_en_operacion',
            'Vehiculos_asignados_a_operar',
            'Vehiculos_devueltos_al_deposito',
            'Demanda_por_mantenimiento',
            'Capacidad_de_atencion_por_plaza',
            'Cantidad_de_plazas_ocupadas',
            'Cantidad_de_vehiculos_destinados_a_mantenimiento_correctivo',
            'Cantidad_de_vehiculos_destinados_a_mantenimiento_preventivo',
            'Disponibilidad_de_la_flot',
            'Vehiculos_que_regresan_de_mantenimiento',
            'Vehiculos_que_se_retiro_por_mantenimiento',
            'Disponibilidad_de_talleres',
            'Cantidad_de_plazas_sin_asignacion_de_mantenimiento',
            'Cantidad_de_plazas_apartadas_por_mantenimiento',
            'Objetivo1',
            'Discrepancia1',
            'Objetivo2',
            'Discrepancia2',
            'Objetivo3',
            'Discrepancia3',
            'Objetivo4',
            'Discrepancia4',
            'Proporcion_vehiculos_mantenimiento_correctivo',
            'Tasa_asignacion',
            'Tasa_fallas_mecanicas',
            'Tasa_inoperatividad_fallas',
            'Tasa_reparacion_fallas_mecanicas',
            'Tasa_reparaciones_preventivas',
            'Tasa_retorno_deposito',
            'Total_de_la_flota',
            'Cantidad_de_vehiculos_que_terminan_el_mantenimiento_por_semana',
            'Tasa_de_liberacion_de_plazas',
            'Demanda_de_operacion'
        ]
    },
    'Satisfaccion de autoridades': {
        'mdl_file': 'FORRESTER/satisfaccion_autoridades-forrester.mdl',
        'table': 'Satisfaccion_de_autoridades',
        'columns_vensim': [
            'Accidentes de tránsito',
            'Accidentes prevenidos',
            'Calidad de infraestructura vial',
            'Cantidad de accidentes',
            'Confianza pública',
            'Congestion vehicular',
            'Depreciacion de inversion',
            'Deterioro de imagen',
            'Deterioro de infraestructura',
            'Fluidez del trafico',
            'Flujo de inversion',
            'Imagen pública de autoridades',
            'Infracciones vehiculares',
            'Inversion en infraestructura',
            'Mejora de imagen',
            'Mejora de infraestructura',
            'Pagos de tributos de transporte',
            'Perdida de confianza',
            'Porcentaje de inversion',
            'Quejas de usuarios',
            'Recuperacion de confianza',
            'Satisfaccion de autoridades de transporte',
            'Satisfaccion de usuarios',
            'Tasa de quejas de usuarios',
            'Tasa de recaudacion',
            'Tasa de viajes de transporte',
            'Total regulaciones viales',
        ],
        'columns_sqlite': [
            
            'Accidentes_de_transito',
            'Accidentes_prevenidos',
            'Calidad_de_infraestructura_vial',
            'Cantidad_de_accidentes',
            'Confianza_publica',
            'Congestion_vehicular',
            'Depreciacion_de_inversion',
            'Deterioro_de_imagen',
            'Deterioro_de_infraestructura',
            'Fluidez_del_trafico',
            'Flujo_de_inversion',
            'Imagen_publica_de_autoridades',
            'Infracciones_vehiculares',
            'Inversion_en_infraestructura',
            'Mejora_de_imagen',
            'Mejora_de_infraestructura',
            'Pagos_tributos_de_transporte',
            'Perdida_de_confianza',
            'Porcentaje_de_inversion',
            'Quejas_de_usuarios',
            'Recuperacion_de_confianza',
            'Satisfaccion_de_autoridades_de_transporte',
            'Satisfaccion_de_usuarios',
            'Tasa_de_quejas_de_usuarios',
            'Tasa_de_recaudacion',
            'Tasa_de_viajes_de_transporte',
            'Total_regulaciones_viales'
        ]
    },
    'Satisfaccion de usuario': {
        'mdl_file': 'FORRESTER/satisfaccion-usuario-forrester.mdl',
        'table': 'Satisfaccion_de_usuario',
        'columns_vensim': [
            'Accidentes antiguos',
            'Casos resueltos',
            'Conductores consumidores de alcohol',
            'Conductores que dejan de consumir alcohol',
            'Congestion vehicular',
            'Estrategias de ejecucion de obras',
            'Estres a transportistas',
            'Extorsiones a transportistas',
            'Extorsiones ocurridas',
            'Fluidez del trafico',
            'Infraestructura vial',
            'Insatisfaccion de usuarios',
            'Nivel de educación vial',
            'Nivel de satisfaccion de usuarios',
            'Nuevos accidentes',
            'Satisfaccion de usuarios',
            'Tasa de accidentes de transporte',
            'Tasa de conductores que consumen alcohol',
            'Tasa de educacion vial',
            'Tasa de extorsiones a transportistas',
            'Tasa de inversion de mantener los vehiculos en buen estado',
            'Tasa de satisfaccion de usuarios',
            'Tasa de seguridad en transportes',
            'Tasas de pagos ilicitos en construcción vial',
            'Total de accidentes de transporte',
            'Total de conductores con consumo de alcohol',
            'Total de vehiculos de transporte publico en buen estado',
            'Total de vehiculos en buen estado',
            'Uso del transporte publico',
            'Vehiculos de transporte en mal estado',
            'Vehiculos de transporte publico en buen estado',
            'Vehiculos descompuestos',
            'Vehiculos en buen estado'
        ],
        'columns_sqlite': [
        
            'Accidentes_antiguos',
            'Casos_resueltos',
            'Conductores_consumidores_de_alcohol',
            'Conductores_que_dejan_de_consumir_alcohol',
            'Congestion_vehicular',
            'Estrategias_de_ejecucion_de_obras',
            'Estres_a_transportistas',
            'Extorsiones_a_transportistas',
            'Extorsiones_ocurridas',
            'Fluidez_del_trafico',
            'Infraestructura_vial',
            'Insatisfaccion_de_usuarios',
            'Nivel_de_educacion_vial',
            'Nivel_de_satisfaccion_de_usuarios',
            'Nuevos_accidentes',
            'Satisfaccion_de_usuarios',
            'Tasa_de_accidentes_de_transporte',
            'Tasa_de_conductores_que_consumen_alcohol',
            'Tasa_de_educacion_vial',
            'Tasa_de_extorsiones_a_transportistas',
            'Tasa_de_inversion_de_mantener_los_vehiculos_en_buen_estado',
            'Tasa_de_satisfaccion_de_usuarios',
            'Tasa_de_seguridad_en_transportes',
            'Tasas_de_pagos_ilicitos_en_construccion_vial',
            'Total_de_accidentes_de_transporte',
            'Total_de_conductores_con_consumo_de_alcohol',
            'Total_de_vehiculos_de_transporte_publico_en_buen_estado',
            'Total_de_vehiculos_en_buen_estado',
            'Uso_del_transporte_publico',
            'Vehiculos_de_transporte_en_mal_estado',
            'Vehiculos_de_transporte_publico_en_buen_estado',
            'Vehiculos_descompuestos',
            'Vehiculos_en_buen_estado'
        ]
    },
    'Seguridad vial': {
        'mdl_file': 'FORRESTER/seguridad-vial-forrester.mdl',
        'table': 'Seguridad_vial',
        'columns_vensim': [
            'Costo promedio mantenimiento infraestructura',
            'Dispositivos de seguridad vial instalados nuevos',
            'Dispositivos de seguridad vial retirados por falla',
            'Dispositivos viales operativos',
            'Equipamiento vial adquirida',
            'Fondos asignados para mantenimiento',
            'Gastos en mantenimiento',
            'Gastos Totales Infraestructura seguridad vial',
            'Infraestructura de seguridad vial',
            'Infraestructura de seguridad vial en ejecución',
            'Infraestructura de seguridad vial obsoleta',
            'Infraestructura en mantenimiento',
            'Presupuesto mantenimiento de infraestructura',
            'Secciones reparadas',
            'Secciones retiradas para mantenimiento',
            'Servicios tecnicos para seguridad vial',
            'Tasa de instalación de nuevos dispositivos',
            'Tasa de mantenimiento correctivo seguridad',
            'Tasa de mantenimiento infraestructura',
            'Tasa de reparación de infraestructura seguridad',
            'Tasa de retiro de dispositivos por falla',
            'Tasa Ejecucion Seguridad Vial',
            'Tasa Infraestructura Seguridad Vial Obsoletas'
        ],
        'columns_sqlite': [
            'Costo_promedio_mantenimiento_infraestructura',
            'Dispositivos_seguridad_vial_instalados_nuevos',
            'Dispositivos_seguridad_vial_retirados_por_falla',
            'Dispositivos_viales_operativos',
            'Equipamiento_vial_adquirida',
            'Fondos_asignados_para_mantenimiento',
            'Gastos_en_mantenimiento',
            'Gastos_Totales_Infraestructura_seguridad_vial',
            'Infraestructura_seguridad_vial',
            'Infraestructura_seguridad_vial_en_ejecucion',
            'Infraestructura_seguridad_vial_obsoleta',
            'Infraestructura_en_mantenimiento',
            'Presupuesto_mantenimiento_de_infraestructura',
            'Secciones_reparadas',
            'Secciones_retiradas_para_mantenimiento',
            'Servicios_tecnicos_para_seguridad_vial',
            'Tasa_de_instalacion_de_nuevos_dispositivos',
            'Tasa_de_mantenimiento_correctivo_seguridad',
            'Tasa_de_mantenimiento_infraestructura',
            'Tasa_de_reparacion_de_infraestructura_seguridad',
            'Tasa_de_retiro_de_dispositivos_por_falla',
            'Tasa_Ejecucion_Seguridad_Vial',
            'Tasa_Infrastructure_Seguridad_Vial_Obsoletas'
        ]
    },
    'Eficiencia de movilidad': {
        'mdl_file': 'FORRESTER/eficiencia-de-movilidad-forrester.mdl',
        'table': 'Eficiencia_de_movilidad',
        'columns_vensim': [
            'Calidad de la infraestructura vial',
            'Calidad de transporte publico',
            'Cantidad del transporte informal',
            'Casos que han sido solucionados',
            'Congestion vehicular',
            'Cruce de pista indebidos',
            'Dificultad de movilidad',
            'Eficiencia de movilidad',
            'Estrategias de ejecucion de obras',
            'Estres a transportistas',
            'Extorsiones a transportistas',
            'Facilidad de movilidad',
            'Fluidez del trafico',
            'Infracciones antiguas',
            'Infracciones nuevas',
            'Nivel de educacion vial',
            'Paradas no autorizadas',
            'Poblacion que utiliza aplicaciones de transporte',
            'Politicas de regulacion de transporte',
            'Seguridad',
            'Tasa de educacion vial',
            'Tasa de extorsiones a transportistas',
            'Tasa de infracciones',
            'Tasa de inversión de infraestructura',
            'Tasa de personas que usan aplicaciones de transporte',
            'Tasa de presion de pasajeros',
            'Tasa de seguridad',
            'Tasa de transeuntes que cruzan indebidamente',
            'Tasa de vehiculos de transporte publico en buen estado',
            'Tasa de vehiculos en circulacion',
            'Total de infracciones',
            'Total de vehiculos en circulación',
            'Transportistas extorsionados',
            'Uso del transporte publico',
            'Usuarios de aplicaciones',
            'Usuarios que dejan de usar aplicaciones',
            'Vehiculos circulantes',
            'Vehiculos que ya no circulan'
        ],
        'columns_sqlite': [
         
            'Calidad_de_la_infraestructura_vial',
            'Calidad_de_transporte_publico',
            'Cantidad_del_transporte_informal',
            'Casos_que_han_sido_solucionados',
            'Congestion_vehicular',
            'Cruce_de_pista_indebidos',
            'Dificultad_de_movilidades',
            'Eficiencia_de_movilidades',
            'Estrategias_de_ejecucion_de_obras',
            'Estres_a_transportistas',
            'Extorsiones_a_transportistas',
            'Facilidad_de_movilidades',
            'Fluidez_del_trafico',
            'Infracciones_antiguas',
            'Infracciones_nuevas',
            'Nivel_de_educacion_vial',
            'Paradas_no_autorizadas',
            'Poblacion_que_utiliza_aplicaciones_de_transporte',
            'Politicas_de_regulacion_de_transporte',
            'Seguridad',
            'Tasa_de_educacion_vial',
            'Tasa_de_extorsiones_a_transportistas',
            'Tasa_de_infracciones',
            'Tasa_de_inversion_de_infraestructura',
            'Tasa_de_personas_que_usan_aplicaciones_de_transporte',
            'Tasa_de_presion_de_pasajeros',
            'Tasa_de_seguridad',
            'Tasa_de_transeuntes_que_cruzan_indebidamente',
            'Tasa_de_vehiculos_de_transporte_publico_en_buen_estado',
            'Tasa_de_vehiculos_en_circulacion',
            'Total_de_infracciones',
            'Total_de_vehiculos_en_circulacion',
            'Transportistas_extorsionados',
            'Uso_del_transporte_publico',
            'Usuarios_de_aplicaciones',
            'Usuarios_que_dejan_de_usar_aplicaciones',
            'Vehiculos_circulantes',
            'Vehiculos_que_ya_no_circulan', 
        ]
    }
}

# modelos_info del código 1 (Interfaz)
modelos_info = {
    'Frecuencia_de_mantenimiento': {
        'submodelos': {
            'Disponibilidad_de_la_flot': {
                'variables': [
                    'Disponibilidad_de_la_flot', 'Vehiculos_que_regresan_de_mantenimiento', 
                    'Vehiculos_que_se_retiro_por_mantenimiento', 'Vehiculos_asignados_a_operar',
                    'Total_de_la_flota', 'Tasa_inoperatividad_fallas', 'Demanda_de_operacion',
                    'Tasa_fallas_mecanicas', 'Objetivo1', 'Discrepancia1'
                ],
                'graficar': [
                    'Disponibilidad_de_la_flot', 'Vehiculos_que_regresan_de_mantenimiento',
                    'Vehiculos_que_se_retiro_por_mantenimiento'
                ]
            },

            'Cantidad_de_fallas_mecanicas': {
                'variables': [
                    'Cantidad_de_fallas_mecanicas', 'Numero_de_veces_que_ocurre_una_falla_mecanica',
                    'Reparacion_de_fallas_mecanicas', 'Cantidad_de_reparaciones_preventivas',
                    'Tasa_reparacion_fallas_mecanicas', 'Tasa_reparaciones_preventivas',
                    'Cantidad_de_vehiculos_destinados_a_mantenimiento_correctivo',
                    'Cantidad_de_vehiculos_destinados_a_mantenimiento_preventivo',
                    'Objetivo2', 'Discrepancia2'
                ],
                'graficar': [
                    'Cantidad_de_fallas_mecanicas', 'Numero_de_veces_que_ocurre_una_falla_mecanica',
                    'Reparacion_de_fallas_mecanicas'
                ]
            },

            'Cantidad_de_vehiculos_en_operacion': {
                'variables': [
                    'Cantidad_de_vehiculos_en_operacion', 'Vehiculos_asignados_a_operar',
                    'Vehiculos_devueltos_al_deposito', 'Tasa_asignacion', 'Demanda_de_operacion',
                    'Tasa_retorno_deposito', 'Cantidad_de_malas_maniobras',
                    'Cantidad_promedio_de_malas_maniobras_por_vehiculo', 'Objetivo3', 'Discrepancia3'
                ],
                'graficar': [
                    'Cantidad_de_vehiculos_en_operacion', 'Vehiculos_asignados_a_operar',
                    'Vehiculos_devueltos_al_deposito'
                ]
            },

            'Disponibilidad_de_talleres': {
                'variables': [
                    'Disponibilidad_de_talleres','Cantidad_de_plazas_sin_asignacion_de_mantenimiento', 'Cantidad_de_plazas_apartadas_por_mantenimiento',
                    'Cantidad_de_plazas_ocupadas', 'Demanda_por_mantenimiento', 
                    'Cantidad_de_vehiculos_destinados_a_mantenimiento_preventivo',
                    'Proporcion_vehiculos_mantenimiento_correctivo', 'Capacidad_de_atencion_por_plaza',
                    'Tasa_de_liberacion_de_plazas', 'Cantidad_de_vehiculos_que_terminan_el_mantenimiento_por_semana',
                    'Objetivo4', 'Discrepancia4'
                ],
                'graficar': [
                    'Disponibilidad_de_talleres', 'Cantidad_de_plazas_sin_asignacion_de_mantenimiento',
                    'Cantidad_de_plazas_apartadas_por_mantenimiento'
                ]
            }
        }
    },
    'Satisfaccion_de_autoridades': {
        'submodelos': {
            'Inversion_en_infraestructura': {
                'variables': [
                    'Inversion_en_infraestructura', 'Flujo_de_inversion', 'Depreciacion_de_inversion', 
                    'Porcentaje_de_inversion', 'Tasa_de_recaudacion'
                ],
                'graficar': [
                    'Inversion_en_infraestructura', 'Flujo_de_inversion',
                    'Depreciacion_de_inversion'
                ]
            },

            'Calidad_de_infraestructura_vial': {
                'variables': [
                    'Calidad_de_infraestructura_vial', 'Mejora_de_infraestructura', 'Deterioro_de_infraestructura',
                    'Total_regulaciones_viales', 'Satisfaccion_de_usuarios', 'Congestion_vehicular', 'Fluidez_del_trafico'
                ],
                'graficar': [
                    'Calidad_de_infraestructura_vial', 'Mejora_de_infraestructura',
                    'Deterioro_de_infraestructura'
                ]
            },

            'Confianza_publica': {
                'variables': [
                    'Confianza_publica', 'Recuperacion_de_confianza', 'Perdida_de_confianza', 
                    'Satisfaccion_de_autoridades_de_transporte', 'Satisfaccion_de_usuarios', 'Tasa_de_viajes_de_transporte'
                ],
                'graficar': [
                    'Confianza_publica', 'Recuperacion_de_confianza',
                    'Perdida_de_confianza'
                ]
            },

            'Imagen_publica_de_autoridades': {
                'variables': [
                    'Imagen_publica_de_autoridades', 'Mejora_de_imagen', 'Deterioro_de_imagen', 'Tasa_de_quejas_de_usuarios',
                    'Quejas_de_usuarios', 'Satisfaccion_de_usuarios', 'Satisfaccion_de_autoridades_de_transporte'
                ],
                'graficar': [
                    'Imagen_publica_de_autoridades', 'Mejora_de_imagen',
                    'Deterioro_de_imagen'
                ]
            }
        
        }
    },
    'Satisfaccion_de_usuario': {
        'submodelos': {
            'Total_de_vehiculos_en_buen_estado': {
                'variables': [
                    'Total_de_vehiculos_en_buen_estado', 'Vehiculos_en_buen_estado', 'Vehiculos_descompuestos',
                    'Tasa_de_inversion_de_mantener_los_vehiculos_en_buen_estado'
                ],
                'graficar': [
                    'Total_de_vehiculos_en_buen_estado', 'Vehiculos_en_buen_estado',
                    'Vehiculos_descompuestos'
                ]
            },

            'Total_de_vehiculos_de_transporte_publico_en_buen_estado': {
                'variables': [
                    'Total_de_vehiculos_de_transporte_publico_en_buen_estado', 'Vehiculos_de_transporte_publico_en_buen_estado',
                    'Vehiculos_de_transporte_en_mal_estado', 'Uso_del_transporte_publico', 'Nivel_de_educacion_vial',
                    'Tasa_de_educacion_vial'
                ],
                'graficar': [
                    'Total_de_vehiculos_de_transporte_publico_en_buen_estado', 'Vehiculos_de_transporte_publico_en_buen_estado',
                    'Vehiculos_de_transporte_en_mal_estado'
                ]
            },

            'Total_de_conductores_con_consumo_de_alcohol': {
                'variables': [
                    'Total_de_conductores_con_consumo_de_alcohol', 'Conductores_consumidores_de_alcohol',
                    'Conductores_que_dejan_de_consumir_alcohol', 'Tasa_de_conductores_que_consumen_alcohol',
                    'Nivel_de_educacion_vial'
                ],
                'graficar': [
                    'Total_de_conductores_con_consumo_de_alcohol', 'Conductores_consumidores_de_alcohol',
                    'Conductores_que_dejan_de_consumir_alcohol'
                ]
            },

            'Extorsiones_a_transportistas': {
                'variables': [
                    'Extorsiones_a_transportistas', 'Extorsiones_ocurridas', 'Casos_resueltos', 'Tasa_de_extorsiones_a_transportistas',
                    'Tasa_de_seguridad_en_transportes', 'Estres_a_transportistas'
                ],
                'graficar': [
                    'Extorsiones_a_transportistas', 'Extorsiones_ocurridas',
                    'Casos_resueltos'
                ]
            },

            'Nivel_de_satisfaccion_de_usuarios': {
                'variables': [
                    'Nivel_de_satisfaccion_de_usuarios', 'Satisfaccion_de_usuarios', 'Insatisfaccion_de_usuarios',
                    'Tasa_de_satisfaccion_de_usuarios', 'Tasa_de_seguridad_en_transportes', 'Fluidez_del_trafico',
                    'Congestion_vehicular'
                ],
                'graficar': [
                    'Nivel_de_satisfaccion_de_usuarios', 'Satisfaccion_de_usuarios',
                    'Insatisfaccion_de_usuarios'
                ]
            },

            'Total_de_accidentes_de_transporte': {
                'variables': [
                    'Total_de_accidentes_de_transporte', 'Nuevos_accidentes', 'Accidentes_antiguos', 
                    'Tasa_de_accidentes_de_transporte'
                ],
                'graficar': [
                    'Total_de_accidentes_de_transporte', 'Nuevos_accidentes',
                    'Accidentes_antiguos'
                ]
            }
        }
    },
    'Seguridad_vial': {
        'submodelos': {
            'Infraestructura_seguridad_vial': {
                'variables': [
                    'Infraestructura_seguridad_vial', 'Infraestructura_seguridad_vial_en_ejecucion',
                    'Infraestructura_seguridad_vial_obsoleta', 'Gastos_Totales_Infraestructura_seguridad_vial',
                    'Equipamiento_vial_adquirida', 'Servicios_tecnicos_para_seguridad_vial', 'Tasa_Ejecucion_Seguridad_Vial',
                    'Tasa_Infrastructure_Seguridad_Vial_Obsoletas'
                ],
                'graficar': [
                    'Infraestructura_seguridad_vial', 'Infraestructura_seguridad_vial_en_ejecucion',
                    'Infraestructura_seguridad_vial_obsoleta'
                ]
            },
            'Dispositivos_viales_operativos': {
                'variables': [
                    'Dispositivos_viales_operativos', 'Dispositivos_seguridad_vial_instalados_nuevos',
                    'Dispositivos_seguridad_vial_retirados_por_falla', 'Tasa_de_instalacion_de_nuevos_dispositivos',
                    'Tasa_de_retiro_de_dispositivos_por_falla'
                ],
                'graficar': [
                    'Dispositivos_viales_operativos', 'Dispositivos_seguridad_vial_instalados_nuevos',
                    'Dispositivos_seguridad_vial_retirados_por_falla'
                ]
            },
            'Infraestructura_en_mantenimiento': {
                'variables': [
                    'Infraestructura_en_mantenimiento', 'Secciones_retiradas_para_mantenimiento', 
                    'Secciones_reparadas', 'Tasa_de_reparacion_de_infraestructura_seguridad', 
                    'Tasa_de_mantenimiento_correctivo_seguridad'
                ],
                'graficar': [
                    'Infraestructura_en_mantenimiento', 'Secciones_retiradas_para_mantenimiento',
                    'Secciones_reparadas'
                ]
            },
            'Presupuesto_mantenimiento_de_infraestructura': {
                'variables': [
                    'Presupuesto_mantenimiento_de_infraestructura', 'Fondos_asignados_para_mantenimiento',
                    'Gastos_en_mantenimiento', 'Costo_promedio_mantenimiento_infraestructura', 
                    'Tasa_de_mantenimiento_infraestructura'
                ],
                'graficar': [
                    'Presupuesto_mantenimiento_de_infraestructura', 'Fondos_asignados_para_mantenimiento',
                    'Gastos_en_mantenimiento'
                ]
            }
        }
    },
    'Eficiencia_de_movilidad': {
        'submodelos': {
            'Poblacion_que_utiliza_aplicaciones_de_transporte': {
                'variables': [
                    'Poblacion_que_utiliza_aplicaciones_de_transporte', 'Usuarios_de_aplicaciones',
                    'Usuarios_que_dejan_de_usar_aplicaciones', 'Tasa_de_personas_que_usan_aplicaciones_de_transporte',
                    'Uso_del_transporte_publico', 'Seguridad'
                ],
                'graficar': [
                    'Poblacion_que_utiliza_aplicaciones_de_transporte', 'Usuarios_de_aplicaciones',
                    'Usuarios_que_dejan_de_usar_aplicaciones'
                ]
            },
            'Total_de_vehiculos_en_circulacion': {
                'variables': [
                    'Total_de_vehiculos_en_circulacion', 'Vehiculos_circulantes', 'Vehiculos_que_ya_no_circulan',
                    'Tasa_de_vehiculos_en_circulacion', 'Uso_del_transporte_publico'
                ],
                'graficar': [
                    'Total_de_vehiculos_en_circulacion', 'Vehiculos_circulantes',
                    'Vehiculos_que_ya_no_circulan'
                ]
            },
            'Extorsiones_a_transportistas': {
                'variables': [
                    'Extorsiones_a_transportistas', 'Transportistas_extorsionados', 'Casos_que_han_sido_solucionados',
                    'Seguridad', 'Estres_a_transportistas', 'Tasa_de_extorsiones_a_transportistas', 
                    'Tasa_de_presion_de_pasajeros'
                ],
                'graficar': [
                    'Extorsiones_a_transportistas', 'Transportistas_extorsionados',
                    'Casos_que_han_sido_solucionados'
                ]
            },
            'Total_de_infracciones': {
                'variables': [
                    'Total_de_infracciones', 'Infracciones_nuevas', 'Infracciones_antiguas', 
                    'Tasa_de_infracciones', 'Nivel_de_educacion_vial', 'Congestion_vehicular'
                ],
                'graficar': [
                    'Total_de_infracciones', 'Infracciones_nuevas',
                    'Infracciones_antiguas'
                ]
            },
            'Eficiencia_de_movilidades': {
                'variables': [
                    'Eficiencia_de_movilidades', 'Facilidad_de_movilidades', 'Dificultad_de_movilidades',
                    'Fluidez_del_trafico', 'Congestion_vehicular'
                ],
                'graficar': [
                    'Eficiencia_de_movilidades', 'Facilidad_de_movilidades',
                    'Dificultad_de_movilidades'
                ]
            }
        }
    }
}

# ------------------- Funciones de SQLite + PySD -------------------

def crear_tablas_y_poblar_si_vacio(db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cur.fetchall()

    if not tablas:
        print("Base de datos vacía. Creando tablas y poblando datos...")
        for modelo, info in modelos_info_simulacion.items():
            columnas_sql = ", ".join([f"{col} REAL" for col in info['columns_sqlite']])
            cur.execute(f"CREATE TABLE IF NOT EXISTS {info['table']} ({columnas_sql});")
            conn.commit()

            modelo_vensim = pysd.read_vensim(info['mdl_file'])
            df = modelo_vensim.run(return_columns=info['columns_vensim'])
            rename_dict = dict(zip(info['columns_vensim'], info['columns_sqlite']))
            df_renombrado = df.rename(columns=rename_dict)
            df_renombrado = df_renombrado.fillna(0)
            data = df_renombrado.to_records(index=False).tolist()

            if len(info['columns_sqlite']) != len(data[0]):
                print(f"Error de columnas en {modelo}")
                continue

            placeholders = ", ".join(["?"] * len(info['columns_sqlite']))
            sql_insert = f"INSERT INTO {info['table']} ({', '.join(info['columns_sqlite'])}) VALUES ({placeholders});"
            cur.executemany(sql_insert, data)
            conn.commit()
            print(f"Datos insertados en {info['table']}")
    else:
        print("Base de datos ya contiene tablas. Se omite la simulación.")

    cur.close()
    conn.close()

# ------------------- Interfaz Gráfica -------------------

class DataViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualización de Modelos")
        self.resize(1400, 750)

        layout_principal = QVBoxLayout()

        self.modelo_selector = QComboBox()
        self.modelo_selector.addItems(modelos_info.keys())
        self.modelo_selector.currentTextChanged.connect(self.actualizar_submodelos)
        layout_principal.addWidget(QLabel("Seleccionar Modelo"))
        layout_principal.addWidget(self.modelo_selector)

        self.submodelo_selector = QComboBox()
        layout_principal.addWidget(QLabel("Seleccionar Submodelo"))
        layout_principal.addWidget(self.submodelo_selector)

        self.btn_mostrar = QPushButton("Mostrar Datos y Gráfica")
        self.btn_mostrar.clicked.connect(self.mostrar_datos_y_grafico)
        layout_principal.addWidget(self.btn_mostrar)

        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.close)
        layout_principal.addWidget(self.btn_salir)

        layout_datos = QHBoxLayout()

        self.tabla = QTableWidget()
        scroll_tabla = QScrollArea()
        scroll_tabla.setWidgetResizable(True)
        scroll_tabla.setWidget(self.tabla)
        scroll_tabla.setMinimumWidth(600)
        layout_datos.addWidget(scroll_tabla)

        self.figura = Figure()
        self.canvas = FigureCanvas(self.figura)
        layout_datos.addWidget(self.canvas, stretch=2)

        layout_principal.addLayout(layout_datos)
        self.setLayout(layout_principal)

        self.actualizar_submodelos(self.modelo_selector.currentText())

    def actualizar_submodelos(self, modelo):
        self.submodelo_selector.clear()
        self.submodelo_selector.addItems(modelos_info[modelo]['submodelos'].keys())

    def mostrar_datos_y_grafico(self):
        modelo = self.modelo_selector.currentText()
        submodelo = self.submodelo_selector.currentText()
        columnas = modelos_info[modelo]['submodelos'][submodelo]['variables']
        columnas_grafico = modelos_info[modelo]['submodelos'][submodelo]['graficar']

        conexion = sqlite3.connect("BD_OG-TRANSPORTE-MUNICIPAL.db")
        df = pd.read_sql_query(f"SELECT {', '.join(columnas)} FROM {modelo}", conexion)
        conexion.close()

        df.insert(0, 'Año', list(range(2025, 2025 + len(df))))

        self.tabla.setColumnCount(len(df.columns))
        self.tabla.setRowCount(len(df))
        self.tabla.setHorizontalHeaderLabels(df.columns)

        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.tabla.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

        self.figura.clear()
        ax = self.figura.add_subplot(111)
        for col in columnas_grafico:
            ax.plot(df['Año'], df[col], label=col)
        ax.set_title(f"{submodelo} - {modelo}")
        ax.set_xlabel("Año")
        ax.set_ylabel("Valor")
        ax.legend()
        self.canvas.draw()

# ------------------- Main -------------------

if __name__ == '__main__':
    db_file = 'BD_OG-TRANSPORTE-MUNICIPAL.db'
    crear_tablas_y_poblar_si_vacio(db_file)
    app = QApplication(sys.argv)
    visor = DataViewer()
    visor.show()
    sys.exit(app.exec_())
