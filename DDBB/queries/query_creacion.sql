CREATE TABLE claustro (
    id_profesor      SMALLINT PRIMARY KEY,
    id_vertical   SMALLINT,
    nombre        VARCHAR(100),
    rol           VARCHAR(5),
    CONSTRAINT fk_vertical FOREIGN KEY (id_vertical) REFERENCES verticales (id_vertical)
)CREATE TABLE verticales (
    id_vertical      SMALLINT PRIMARY KEY,
    nombre        VARCHAR(100)
)CREATE TABLE proyectos (
    id_proyectos      SMALLINT PRIMARY KEY,
    id_vertical   SMALLINT,
    nombre        VARCHAR(100),
    CONSTRAINT fk_vertical FOREIGN KEY (id_vertical) REFERENCES verticales (id_vertical)
)CREATE TABLE calificaciones (
    id_calif     SMALLINT PRIMARY KEY,
    id_proyecto  SMALLINT,
    id_alumno  SMALLINT,
    nota         BOOLEAN,
    CONSTRAINT fk_vertical FOREIGN KEY (id_vertical) REFERENCES verticales (id_vertical)
)CREATE TABLE alumnos (
    id_alumnos     SMALLINT PRIMARY KEY,
    nombre        VARCHAR(100),
    email          VARCHAR(100))CREATE TABLE a_clase (
    id_aclase     SMALLINT PRIMARY KEY,
    id_bootcamp   SMALLINT,
    id_alumno     SMALLINT,
    CONSTRAINT fk_bootcamp FOREIGN KEY (id_bootcamp) REFERENCES bootcamp (id_bootcamp),
	CONSTRAINT fk_alumno FOREIGN KEY (id_alumno) REFERENCES alumnos (id_alumno)
)CREATE TABLE bootcamp (
    id_bootcamp    SMALLINT PRIMARY KEY,
    id_vertical  SMALLINT,
    id_campus    SMALLINT,
	id_modalidad SMALLINT,
	promocion    VARCHAR(50),
	f_comienzo   DATE NOT NULL,
	CONSTRAINT fk_bootcamp FOREIGN KEY (id_bootcamp) REFERENCES bootcamp (id_bootcamp),
	CONSTRAINT fk_vertical FOREIGN KEY (id_vertical) REFERENCES verticales (id_vertical)
    CONSTRAINT fk_campus FOREIGN KEY (id_campus) REFERENCES campus (id_campus),
	CONSTRAINT fk_modalidad FOREIGN KEY (id_modalidad) REFERENCES modalidad (id_modalidad)
)CREATE TABLE p_clase (
    id_pclase    SMALLINT PRIMARY KEY,
    id_bootcamp  SMALLINT,
    id_profesor    VARCHAR(50),
	CONSTRAINT fk_bootcamp FOREIGN KEY (id_bootcamp) REFERENCES bootcamp (id_bootcamp),
	CONSTRAINT fk_profe FOREIGN KEY (id_profe) REFERENCES claustro (id_profe)
)CREATE TABLE campus (
    id_campus    SMALLINT PRIMARY KEY,
    nombre       VARCHAR(50)
)CREATE TABLE modalidad (
    id_modalidad    SMALLINT PRIMARY KEY,
    presencial      BOOLEAN,
    fulltime        BOOLEAN
	);