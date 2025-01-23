from utils import *

claus = pd.read_csv("data/claustro.csv",sep = ";")
clase1=pd.read_csv("data/clase_1.csv", sep =";")
clase2=pd.read_csv("data/clase_2.csv", sep =";")
clase3=pd.read_csv("data/clase_3.csv", sep =";")
clase4=pd.read_csv("data/clase_4.csv", sep =";")
total_clases= pd.read_csv("data/total_clases.csv")
total_clases.drop(columns="Unnamed: 0",inplace=True)

alumnos = pd.DataFrame({"Nombre": total_clases["Nombre"].unique(),"Email":total_clases["Email"].unique()})
alumnos.insert(0, 'id_alumnos', range(1, len(alumnos) + 1))

verticales= pd.DataFrame({"Nombre":claus["Vertical"].unique()})
verticales.insert(0, 'id_verticales', range(1, len(verticales)
                                             + 1))
campus= pd.DataFrame({"Nombre":total_clases["Campus"].unique()})
campus.insert(0, 'id_campus', range(1, len(campus) + 1))

claustro1=pd.DataFrame({"nombre":claus["Nombre"],"vertical":claus["Vertical"],"Rol":claus["Rol"]})
claustro1.insert(0, 'id_profesor', range(1, len(claustro1) + 1))
claustro = pd.merge(claustro1, verticales, left_on='vertical', right_on='Nombre', how='left')
claustro= claustro.loc[:,["id_profesor","nombre","id_verticales","Rol"]]

claus['Modalidad'] = claus['Modalidad'].replace({'Presencial': True, 'Online': False})
modalidad=pd.DataFrame({"Presencial":claus['Modalidad'].unique()})
modalidad.insert(0, 'id_modalidad', range(1, len(modalidad) + 1))
modalidad['FullTime'] = [True,False]
modalidad.loc[2]=[3,True,False]
modalidad.loc[3]=[4,False,True]

total_clases["Vertical"] = total_clases["Proyecto"].apply(asignar_vertical)
proyectos1 = total_clases.groupby("Proyecto")["Vertical"].unique().reset_index()
proyectos1["Vertical"] = proyectos1["Vertical"].str[0]
proyectos1.insert(0, 'id_proyecto', range(1, len(proyectos1) + 1))
proyectos = pd.merge(proyectos1, verticales, left_on='Vertical', right_on='Nombre', how='left')
proyectos= proyectos.loc[:,["id_proyecto","Proyecto","id_verticales"]]

bootcamp1=pd.DataFrame({"Promocion":total_clases["Promoción"],"F_comienzo":total_clases["Fecha_comienzo"],
                        "campus":total_clases["Campus"],"vertical":total_clases["Vertical"]})
bootcamp= pd.merge(bootcamp1, verticales, left_on='vertical', right_on='Nombre', how='left')
bootcamp= pd.merge(bootcamp, campus, left_on='campus', right_on='Nombre', how='left')
bootcamp["id_modalidad"]=modalidad.iloc[0,0]
bootcamp=bootcamp.drop_duplicates(["Promocion","F_comienzo","id_campus","id_modalidad","id_verticales"]).reset_index()
bootcamp.insert(0, 'id_bootcamp', range(1, len(bootcamp) + 1))
bootcamp.drop(columns="index",inplace=True)
bootcamp_cruce = bootcamp
bootcamp=bootcamp.loc[:,['id_bootcamp',"Promocion","F_comienzo","id_campus","id_verticales","id_modalidad"]]

total_clases["Calificación"] = total_clases["Calificación"] .replace({'Apto': True, 'No Apto': False})
calificaciones1=pd.DataFrame({"nombre_alumnos":total_clases["Nombre"],"nombre_proyecto":total_clases["Proyecto"],"Nota":total_clases["Calificación"]})
calificaciones1.insert(0, 'id_calificaciones', range(1, len(calificaciones1) + 1))
calificaciones= pd.merge(calificaciones1, alumnos, left_on='nombre_alumnos', right_on='Nombre', how='left')
calificaciones= pd.merge(calificaciones, proyectos, left_on='nombre_proyecto', right_on='Proyecto', how='left')
calificaciones=calificaciones.loc[:,["id_calificaciones","id_alumnos","id_proyecto","Nota"]]

a_alumnos = pd.merge(total_clases, bootcamp_cruce, left_on=['Promoción','Fecha_comienzo','Campus', 'Vertical'], right_on=['Promocion','F_comienzo','campus','vertical'], how='left')
a_alumnos = a_alumnos.loc[:,['Nombre','id_bootcamp']]
a_alumnos = pd.merge(a_alumnos, alumnos, left_on=['Nombre'], right_on=['Nombre'], how='left')
a_alumnos.drop_duplicates(subset=["Nombre","id_bootcamp","id_alumnos","Email"],inplace=True,ignore_index=True)
a_alumnos = a_alumnos.loc[:,['id_bootcamp', 'id_alumnos']]
a_alumnos.insert(0, 'id_aclase', range(1, len(a_alumnos) + 1))

p_clase = pd.merge(claus, bootcamp_cruce, left_on=['Promocion','Campus', 'Vertical'], right_on=['Promocion','campus','vertical'], how='left')
p_clase = p_clase.loc[:,['Nombre','id_bootcamp']]
p_clase = pd.merge(p_clase, claustro, left_on=['Nombre'], right_on=['nombre'], how='left')
p_clase = p_clase.loc[:,['id_bootcamp', 'id_profesor']]
p_clase.insert(0, 'id_pclase', range(1, len(p_clase) + 1))
p_clase.dropna(inplace=True)
p_clase["id_bootcamp"] = p_clase["id_bootcamp"].astype("int")

a_clase=a_alumnos
a_clase.rename(columns={"id_alumnos":"id_alumno"},inplace=True)
alumnos.rename(columns={"id_alumnos":"id_alumno","Nombre":"nombre","Email":"email"},inplace=True)
bootcamp.rename(columns={"Promocion":"promocion","F_comienzo":"f_comienzo","id_verticales":"id_vertical"},inplace=True)
bootcamp["f_comienzo"]= pd.to_datetime(bootcamp["f_comienzo"], format='%d/%m/%Y')
calificaciones.rename(columns={"id_calificaciones":"id_calif","id_alumnos":"id_alumno","Nota":"nota"},inplace=True)
campus.rename(columns={"Nombre":"nombre"},inplace=True)
claustro.rename(columns={"id_verticales":"id_vertical","Rol":"rol"},inplace=True)
modalidad.rename(columns={"Presencial":"presencial","FullTime":"fulltime"},inplace=True)
proyectos.rename(columns={"Proyecto":"nombre","id_verticales":"id_vertical"},inplace=True)
verticales.rename(columns={"Nombre":"nombre","id_verticales":"id_vertical"},inplace=True)

dic_sql={"campus":campus,
         "verticales":verticales,
         "modalidad":modalidad,
         "claustro":claustro,
         "bootcamp":bootcamp,
         "proyectos":proyectos,
         "p_clase":p_clase,
         "alumnos":alumnos,
         "calificaciones":calificaciones,
         "a_clase":a_clase
      }

upload_tables(dic_sql,engine)




