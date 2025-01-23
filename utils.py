import pandas as pd

#Esta funcion pivota los datos de origen de los csv de clase poder pasar los proyectos de columna a filas y así facilitar el concatenado de tablas e ingesta en BBDD
def class_melt(clase):
    return pd.melt(
    clase,
    id_vars=["Nombre", "Email", "Promoción", "Fecha_comienzo", "Campus"], 
    value_vars=[i for i in pd.DataFrame(clase.columns).loc[pd.DataFrame(clase.columns)[0].str.contains("Proyecto"), 0]], 
    var_name="Proyecto",  
    value_name="Calificación")


#Definimos primero un diccionario de Verticales (vertical_rules), que se deberá actualizar en caso de de ampliar oferta Formativa:
vertical_rules = {
    "FS": ['Proyecto_WebDev', 'Proyecto_FrontEnd', 'Proyecto_Backend', 
           'Proyecto_React', 'Proyecto_FullSatck'],
    "DS": ['Proyecto_HLF', 'Proyecto_EDA', 'Proyecto_BBDD', 'Proyecto_ML',
       'Proyecto_Deployment']
}
#Esta funcion el proyecto del alumno y lo checkea dentro del vertical_rules para identificar la vertical a la que pertenece
def asignar_vertical(proyecto):
    for vertical, proyectos in vertical_rules.items():
        if proyecto in proyectos:
            return vertical
    return 'Desconocido'


#Función para pasar los DataFrame a pgAdmin con un diccionario donde tenemos todos los DF relacionados con las tablas

from sqlalchemy import create_engine
engine = create_engine('postgresql://school_db_hkla_user:S8tvOM5YVinPoWddRVHG8Q4qMr3TFSek@dpg-cu8fnnl6l47c738hj8v0-a.frankfurt-postgres.render.com:5432/school_db_hkla')
def upload_tables(dict, engine):
    for table_name, dataframe in dict.items():
        dataframe.to_sql(
            name=table_name,  # Use the key as the table name
            con=engine,       # Database engine
            if_exists="append",  # If the table exists, append
            index=False        # Do not write the index
        )