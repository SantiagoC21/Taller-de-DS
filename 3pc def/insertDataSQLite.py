import pysd
import pandas as pd
import sqlite3
import numpy as np

db_file = 'BD_OG-TRANSPORTE-MUNICIPAL.db'

conn = sqlite3.connect(db_file)
cur = conn.cursor()

modelos_info = {
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

def transferir_datos_modelo_a_sqlite(modelo_nombre, info):
    print(f"Procesando submodelo: {modelo_nombre}")
    modelo = pysd.read_vensim(info['mdl_file'])

    df = modelo.run(return_columns=info['columns_vensim'])

    rename_dict = dict(zip(info['columns_vensim'], info['columns_sqlite']))
    df_renombrado = df.rename(columns=rename_dict)

    for col in df_renombrado.columns:
        if df_renombrado[col].isnull().any():
            print(f"Advertencia: La columna '{col}' tiene valores vacíos.")
            df_renombrado[col] = df_renombrado[col].fillna(0)

    data = df_renombrado.to_records(index=False).tolist()

    print(f"Columnas esperadas: {len(info['columns_sqlite'])}")
    print(f"Datos generados: {len(data[0])}")
    
    if len(info['columns_sqlite']) != len(data[0]):
        print(f"Error: La cantidad de columnas ({len(info['columns_sqlite'])}) no coincide con la cantidad de datos ({len(data[0])})")
        print(f"Columnas: {info['columns_sqlite']}")
        print(f"Datos: {data[0]}")
        return

    columnas_sql = ", ".join(info['columns_sqlite'])
    placeholders = ", ".join(["?"] * len(info['columns_sqlite']))
    sql_insert = f"INSERT INTO {info['table']} ({columnas_sql}) VALUES ({placeholders});"

    # Ejecutar inserciones
    cur.executemany(sql_insert, data)
    conn.commit()
    print(f"Datos insertados en tabla {info['table']} correctamente.\n")

def crear_tablas():
    for modelo, info in modelos_info.items():
        columnas_sql = ", ".join([f"{columna} TEXT" for columna in info['columns_sqlite']])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {info['table']} ({columnas_sql});"
        cur.execute(create_table_sql)
        conn.commit()

crear_tablas()

for nombre, info in modelos_info.items():
    transferir_datos_modelo_a_sqlite(nombre, info)

cur.close()
conn.close()
