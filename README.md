# Cuadrature-Tarea-2

Este es un trabajo para el curso FS-0432 Fisica Computacional de la Universidad de Costa Rica a cargo del profesor Marlon Brenes. El trabajo corresponde a la Tarea 2: Cuadratura Gaussiana, documentación de código y Git con un valor de 6%. 

## Cuadratura Gaussiana para Integración Numérica

[![Documentación](https://img.shields.io/badge/Documentación-Publicada-blue.svg)](https://gcontreras-hub.github.io/Cuadrature-Tarea-2/) Una biblioteca Python para calcular integrales definidas con alta precisión utilizando el método de Cuadratura Gaussiana (Gauss-Legendre).

## Problema

Muchas integrales definidas, como la que se presenta en este proyecto:
$$ \int_{1}^{3} (x^6 - x^2 \sin(2x)) dx $$
no tienen solución analítica simple. Este proyecto ofrece una implementación robusta del método numérico de Cuadratura Gaussiana para obtener aproximaciones precisas de forma eficiente.

## Uso Rápido

Para integrar una función $f(x)$ en el intervalo $[a, b]$ usando $N$ puntos de Gauss:

```python
import numpy as np
from cuadrature import integrar_gauss # Importa tu función

def mi_funcion(x):
    return np.cos(x) / (1 + x**2)

# Intervalo [0, pi/2] y 5 puntos (N=5)
a = 0
b = np.pi / 2
N = 5

resultado = integrar_gauss(mi_funcion, a, b, N)

print(f"La integral aproximada es: {resultado:.8f}")
