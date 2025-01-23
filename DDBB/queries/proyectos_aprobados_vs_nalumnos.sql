SELECT t1.proyectos_aprobados, t2.num_alumnos, t1.vertical, t1.localizacion, t1.promocion FROM (SELECT COUNT(t1.id_proyecto) AS "proyectos_aprobados", t4.promocion, t6.nombre AS "localizacion", t5.nombre AS "vertical", t4.id_bootcamp
FROM calificaciones t1
INNER JOIN alumnos t2 ON t2.id_alumno=t1.id_alumno
INNER JOIN a_clase t3 on t2.id_alumno=t3.id_alumno
INNER JOIN bootcamp t4 ON t3.id_bootcamp=t4.id_bootcamp
INNER JOIN verticales t5 ON t4.id_vertical=t5.id_vertical
INNER JOIN campus t6 ON t4.id_campus=t6.id_campus
WHERE t1.nota= True
GROUP BY t5.nombre, t6.nombre, t4.promocion, t4.id_bootcamp) t1

INNER JOIN (SELECT COUNT(t1.id_alumno) AS "num_alumnos", t4.nombre AS "vertical", t5.nombre AS "localizacion",t3.promocion, t3.id_bootcamp
FROM alumnos t1
INNER JOIN a_clase t2 ON t1.id_alumno = t2.id_alumno
INNER JOIN bootcamp t3 ON t2.id_bootcamp = t3.id_bootcamp
INNER JOIN verticales t4 ON t3.id_vertical = t4.id_vertical
INNER JOIN campus t5 ON t3.id_campus = t5.id_campus
GROUP BY 2,3,4,5) t2 ON t1.id_bootcamp = t2.id_bootcamp
;