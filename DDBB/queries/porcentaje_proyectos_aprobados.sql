SELECT  ROUND(((t1.proyectos_aprobados::FLOAT / t2.proyectos_totales::FLOAT) * 100)::NUMERIC, 2) AS "porcentaje_aprobados",
t1.proyectos_aprobados, t2.proyectos_totales, 
t1.vertical, t1.localizacion, t1.promocion, t2.profesor, t1.id_bootcamp 
FROM (SELECT COUNT(t1.id_proyecto) AS "proyectos_aprobados", t4.promocion, t6.nombre AS "localizacion",t8.nombre AS "profesor" ,t5.nombre AS "vertical", t4.id_bootcamp
FROM calificaciones t1
INNER JOIN alumnos t2 ON t2.id_alumno=t1.id_alumno
INNER JOIN a_clase t3 on t2.id_alumno=t3.id_alumno
INNER JOIN bootcamp t4 ON t3.id_bootcamp=t4.id_bootcamp
INNER JOIN verticales t5 ON t4.id_vertical=t5.id_vertical
INNER JOIN campus t6 ON t4.id_campus=t6.id_campus
INNER JOIN p_clase t7 ON t7.id_bootcamp=t4.id_bootcamp
INNER JOIN claustro t8 ON t8.id_profesor=t7.id_profesor
WHERE t1.nota= True
GROUP BY t8.nombre, t5.nombre, t6.nombre, t4.promocion, t4.id_bootcamp) t1
LEFT JOIN
(SELECT COUNT(t1.id_proyecto) AS "proyectos_totales", t4.id_bootcamp, t8.nombre AS "profesor"
FROM calificaciones t1
INNER JOIN alumnos t2 ON t2.id_alumno=t1.id_alumno
INNER JOIN a_clase t3 on t2.id_alumno=t3.id_alumno
INNER JOIN bootcamp t4 ON t3.id_bootcamp=t4.id_bootcamp
INNER JOIN verticales t5 ON t4.id_vertical=t5.id_vertical
INNER JOIN campus t6 ON t4.id_campus=t6.id_campus
INNER JOIN p_clase t7 ON t7.id_bootcamp=t4.id_bootcamp
INNER JOIN claustro t8 ON t8.id_profesor=t7.id_profesor
GROUP BY t4.id_bootcamp, profesor) t2
ON t1.id_bootcamp=t2.id_bootcamp
GROUP BY t2.profesor, t1.id_bootcamp, t1.proyectos_aprobados,t2.proyectos_totales,t1.vertical, t1.localizacion, t1.promocion;