SELECT t1.nombre AS "alumno", t4.nombre AS "vertical", t5.nombre AS "localizacion",t3.promocion, t3.f_comienzo
FROM alumnos t1
INNER JOIN a_clase t2 ON t1.id_alumno = t2.id_alumno
INNER JOIN bootcamp t3 ON t2.id_bootcamp = t3.id_bootcamp
INNER JOIN verticales t4 ON t3.id_vertical = t4.id_vertical
INNER JOIN campus t5 ON t3.id_campus = t5.id_campus
WHERE t4.nombre = 'DS' AND t5.nombre = 'Madrid' AND t3.promocion = 'Septiembre';

