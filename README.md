# 📚 Proyecto: Creación de una Base de Datos Relacional

## 🧩 Descripción del Proyecto

En este proyecto se desarrollará una base de datos relacional a partir de un conjunto de datos sin normalizar.
Los datos hacen referencia a un grupo de estudiantes y al claustro de profesores de una escuela de bootcamps.

El objetivo principal es aplicar conceptos de modelado y normalización de bases de datos, así como la implementación práctica en PostgreSQL.
Este proyecto permitirá adquirir experiencia en el diseño, creación y despliegue de bases de datos escalables y normalizadas.

## 🧠 Objetivos del Proyecto

El propósito del proyecto es diseñar e implementar una base de datos relacional que represente de forma eficiente la información de estudiantes, profesores y proyectos.

Se trabajará siguiendo las buenas prácticas de diseño de bases de datos:

1.Normalización

2.Definición de relaciones entre entidades

3.Integridad referencial

4.Escalabilidad y flexibilidad del modelo

## ⚙️ Tareas Realizadas

### 🧱 Modelo Entidad-Relación (E/R)

Se diseña un modelo E/R que represente la estructura de la base de datos normalizada, definiendo:

1.Entidades principales (Estudiantes, Profesores, Campus, Promociones, Proyectos, etc.)

2.Atributos

3.Relaciones entre entidades

### 🧩 Modelo Lógico de la Base de Datos

A partir del modelo E/R, se crea el modelo lógico, definiendo:

1.Tablas y campos

2.Tipos de datos adecuados

3.Claves primarias y foráneas

4.Relaciones (1:N, N:M)

### 🧹 Normalización de Datos

Se aplican los principios de normalización (hasta 3FN) para eliminar redundancias y mejorar la integridad de los datos.

### 🛠️ Creación de la Base de Datos

1.Se crea la base de datos en PostgreSQL.

2.Se definen las queries SQL necesarias para crear las tablas.

3.Se insertan los datos normalizados.

4.Se asegura que la base de datos esté alojada en un servidor accesible desde aplicaciones externas (Render).

### 🚀 Requisitos de Escalabilidad

El modelo de base de datos es escalable, permitiendo la incorporación de nuevas dimensiones como:

1.Nuevos campus (Madrid, Valencia, etc.)

2.Nuevas verticales (Data Science, Full Stack, etc.)

3.Nuevas promociones (Septiembre, Febrero, etc.)

4.Nuevas modalidades (Online, Presencial, Híbrida)

5.Nuevas aulas o grupos

### 🧑‍💻 Tecnologías Utilizadas

PostgreSQL 🐘

pgAdmin

Render (para desplegar la base de datos)

GitHub (control de versiones y entrega final)

## ✨ Autora
Yanelis González





