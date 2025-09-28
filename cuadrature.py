# Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Función que vamos a integrar
def func(x):
    """
    Función de prueba para la integración numérica.

    Esta es la función $f(x)$ que se desea integrar en el ejemplo
    de Cuadratura Gaussiana.

    Args:
        x (float, array): El punto o array de puntos donde evaluar la función.

    Returns:
        float, array: El valor de $x^6 - x^2 \sin(2x)$.
    """
    return x**6 - x**2 * np.sin(2*x)

# Obtener puntos y pesos en [-1, 1]
def gaussxw(N):
    """
    Obtiene los nodos y pesos para la Cuadratura de Gauss-Legendre en [-1, 1].

    Utiliza la implementación de NumPy para calcular los puntos y pesos
    necesarios para el método.

    Args:
        N (int): El número de puntos de Gauss a generar.

    Returns:
        tuple: Una tupla con dos arrays NumPy, (x, w), que son los nodos y pesos.
    
    Examples:
        >>> x, w = gaussxw(2)
        >>> len(x)
        2
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

# Escalar los puntos y pesos al intervalo [a, b]
def gaussxwab(a, b, x, w):
    """
    Escala los nodos y pesos de Gauss desde [-1, 1] al intervalo [a, b].

    Esto es esencial para aplicar la Cuadratura Gaussiana a cualquier intervalo $[a, b]$.

    Args:
        a (float): Límite inferior del nuevo intervalo.
        b (float): Límite superior del nuevo intervalo.
        x (np.ndarray): Nodos de Gauss obtenidos para el intervalo [-1, 1].
        w (np.ndarray): Pesos de Gauss obtenidos para el intervalo [-1, 1].

    Returns:
        tuple: Una tupla con los nodos escalados (xp) y los pesos escalados (wp).
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

# Integración usando cuadratura gaussiana
def integrar_gauss(f, a, b, N):
    """
    Calcula la integral definida de una función usando la Cuadratura Gaussiana.

    Aproxima la integral $\int_{a}^{b} f(x) dx$ sumando la función evaluada en los
    nodos de Gauss multiplicada por los pesos escalados.

    Args:
        f (function): La función a integrar, que debe aceptar un array NumPy
                      como entrada (ej: lambda x: x**2).
        a (float): Límite inferior de la integración.
        b (float): Límite superior de la integración.
        N (int): Número de puntos de Gauss (nodos) a utilizar. Determina la precisión.

    Returns:
        float: El valor aproximado de la integral.

    Examples:
        >>> # Definimos una función simple: f(x) = x^2
        >>> def f_test(x):
        ...     return x**2
        >>> # Integramos de 0 a 1 con N=3 (el valor exacto es 1/3 ≈ 0.333...)
        >>> integrar_gauss(f_test, 0, 1, 3)
        0.3333333333333333
        
        >>> # Ejemplo con límites diferentes: integrar x^2 de 1 a 2 (valor exacto: 7/3 ≈ 2.333...)
        >>> integrar_gauss(f_test, 1, 2, 4)
        2.3333333333333335
    """
    x, w = gaussxw(N)
    xp, wp = gaussxwab(a, b, x, w)
    return np.sum(wp * f(xp))

def ejecutar():
    # Limites de integración
    a = 1
    b = 3

    # Evaluar para diferentes valores de N
    # Para N=2
    x2, w2 =gaussxw(2)
    xp2, wp2 = gaussxwab(a, b, x2, w2)
    I2 = np.sum(wp2 * func(xp2))
    print(f"Para N=2 la integral es aproximadamente {I2:.12f}")

    # Para N=3
    x3, w3 =gaussxw(3)
    xp3, wp3 = gaussxwab(a, b, x3, w3)
    I3 = np.sum(wp3 * func(xp3))
    print(f"Para N=3 la integral es aproximadamente {I3:.12f}")

    # Para N=4
    x4, w4 =gaussxw(4)
    xp4, wp4 = gaussxwab(a, b, x4, w4)
    I4 = np.sum(wp4 * func(xp4))
    print(f"Para N=4 la integral es aproximadamente {I4:.12f}")

    # Para N=5
    x5, w5 =gaussxw(5)
    xp5, wp5 = gaussxwab(a, b, x5, w5)
    I5 = np.sum(wp5 * func(xp5))
    print(f"Para N=5 la integral es aproximadamente {I5:.12f}")

    # Para N=6
    x6, w6 =gaussxw(6)
    xp6, wp6 = gaussxwab(a, b, x6, w6)
    I6 = np.sum(wp6 * func(xp6))
    print(f"Para N=6 la integral es aproximadamente {I6:.12f}")

def grafica():
    # Limites de integración
    a = 1
    b = 3

    # Graficar la función
    x = np.linspace(1, 3, 128)
    plt.figure(dpi=100)
    for N in range(2,7):
        plt.plot(x, legendre(N)(x), label='N = {}'.format(N))
    plt.grid()
    plt.xlabel("$x$")
    plt.ylabel("$P_N(x)$")
    plt.legend()
    plt.show()

def graficas_convergencia():
    # Limites de integración
    a = 1
    b = 3
    # Graficar la convergencia
    Ns = np.arange(2, 21)
    Is = [integrar_gauss(func, a, b, N) for N in Ns]
    plt.figure(figsize=(10, 6))
    plt.plot(Ns, Is, marker='o')    
    plt.xlabel('Número de puntos (N)')
    plt.ylabel('Valor de la integral')
    plt.title('Convergencia del método de integración de Gauss')
    plt.grid()
    plt.show()

ejecutar()
grafica()
graficas_convergencia()

# src/cuadrature.py (Modificado)

# ... (otras funciones)

def integrar_gauss(f, a, b, N):
    """Calcula la integral definida de una función usando la Cuadratura Gaussiana.

    Aproxima la integral sumando la función evaluada en los nodos de Gauss
    multiplicada por los pesos escalados.

    Args:
        f (function): La función a integrar, que debe aceptar un array numpy
                      como entrada (ej: lambda x: x**2).
        a (float): Límite inferior de la integración.
        b (float): Límite superior de la integración.
        N (int): Número de puntos de Gauss (nodos) a utilizar.

    Returns:
        float: El valor aproximado de la integral.

    Examples:
        >>> # Definimos una función simple: f(x) = x^2
        >>> def f_test(x):
        ...     return x**2
        >>> # Integramos de 0 a 1 con N=3 (el valor exacto es 0.333...)
        >>> integrar_gauss(f_test, 0, 1, 3)
        0.3333333333333333
    """
    x, w = gaussxw(N)
    xp, wp = gaussxwab(a, b, x, w)
    return np.sum(wp * f(xp))