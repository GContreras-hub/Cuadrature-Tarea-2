# Welcome to Cuadrature-Tarea-2
___

## Problema:
El propósito es aplicar el concepto de cuadratura Gaussiana para integración utilizando los polinomios de Legendre.
Mediante un script de python cuadrature.py que resuelve la siguiente integral utilizando el método de cuadratura Gaussiana:

\begin{equation}
I = \int_{1}^{3} dx [x^6 - x^2 sin(2x)]
\end{equation}

Cumpliendo los siguientes requisitos:
* Escribir un script de python que ejecuta el método numérico y devuelve el resultado correcto.
* Que el script contenga una funcion que devuelve los pesos y puntos de colocación.
* Que el script contenga una funcion que escala el intervalo de integración.
* Hacer pruebas con distintos valores de N hasta alcanzar el resultado correcto.

## Project layout

    mkdocs.yml    # The configuration file.
    cuadrature.py # Script de python con la solucion
    Tarea_02_Gabriel_Contreras_II_2025.ipynb # Documento final de Jupyter notebook 
    docs/
        index.md  # The documentation homepage.
        explanation.md # Describe el método numérico a utilizar.
        tutorials.md # Incluye un ejemplo de uso
        reference.md # Contiene la documentacion de las funciones.
        ...       # Other markdown pages, images and other files.
