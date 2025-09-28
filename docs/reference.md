# 📚 Referencia de API: Módulo Cuadratura

Esta página contiene la documentación técnica completa del módulo `cuadrature`, generada automáticamente a partir de los docstrings. Aquí encontrarás detalles sobre cada función, sus argumentos, valores de retorno y ejemplos de uso.

---

## Módulo Principal: `cuadrature`

La siguiente inyección documenta el módulo completo y lista todos sus miembros.

::: src.cuadrature
    options:
      # Muestra la documentación del módulo (si tiene docstring) y de sus miembros
      members:
        - integrar_gauss
        - gaussxw
        - gaussxwab
        - func

---

## Función de Integración Principal

### `integrar_gauss`

Esta es la función que los usuarios deben llamar para realizar la integración numérica. Su documentación incluye un ejemplo de uso completo.

::: src.cuadrature.integrar_gauss

---

## Funciones Auxiliares

Estas funciones son la base de la Cuadratura Gaussiana.

### `gaussxw`

Función para obtener los nodos y pesos en el intervalo canónico $[-1, 1]$.

::: src.cuadrature.gaussxw

### `gaussxwab`

Función de escalado de los nodos y pesos al intervalo de integración deseado $[a, b]$.

::: src.cuadrature.gaussxwab
