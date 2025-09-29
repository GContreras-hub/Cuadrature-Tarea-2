# Tutorial
## Integración Numérica con Cuadratura Gaussiana

Este tutorial te guía sobre cómo usar el módulo `cuadrature` para calcular la integral definida de una función utilizando el método de Cuadratura Gaussiana.

## El Problema a Resolver: Integración Numérica

Calcular la integral definida $\int_{a}^{b} f(x) dx$ de una función compleja a menudo requiere métodos numéricos. El módulo `cuadrature` implementa la **Cuadratura Gaussiana**, un método altamente eficiente que aproxima la integral al evaluar la función en un número pequeño de puntos óptimos (*nodos de Gauss*) dentro del intervalo, logrando una alta precisión.

## La Solución: `integrar_gauss`

La función clave es `integrar_gauss`. Está diseñada para ser simple y flexible, requiriendo solo la función, los límites del intervalo y el número de puntos de Gauss (N).

### Referencia de la Función

Utilizamos `mkdocstrings` para inyectar la documentación extraída directamente del código fuente:

::: cuadrature.integrar_gauss

## Ejemplo de Uso

A continuación, se muestra cómo usar el módulo para integrar la función $f(x) = x^6 - x^2 \sin(2x)$ en el intervalo $[1, 3]$, tal como se realiza en el *script* original.

**Nota:** El método de Cuadratura Gaussiana con $N$ puntos es exacto para polinomios de grado hasta $2N-1$. Nuestra función $f(x)$ no es un polinomio, por lo que la precisión aumenta a medida que incrementamos $N$.

### Código de Ejemplo

```python
import numpy as np
from cuadrature import func, integrar_gauss # Asume que tu código es un módulo importable

# 1. Definir los límites y la función
a = 1
b = 3

## 2. Elegir el número de puntos (N) para la precisión
N_puntos = 5

## 3. Calcular la integral
I_aprox = integrar_gauss(func, a, b, N_puntos)

## Imprimir el resultado
print(f"La integral de f(x) en [{a}, {b}] con N={N_puntos} es: {I_aprox:.12f}")
### Output (ejemplo, el valor real dependerá de la implementación de numpy):
### La integral de f(x) en [1, 3] con N=5 es: 317.344226721970
