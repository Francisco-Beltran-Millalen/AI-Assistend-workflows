# Protocolo de Artefactos Existentes

Cuando se inicia una etapa de las Fases 1 a 5, la habilidad `start-stage` verifica si los artefactos de salida de esa etapa ya existen. Este protocolo define qué hacer cuando existen.

**No aplica a las etapas bajo demanda (0, teacher).**

---

## Paso 1: Identificar qué artefactos existen

Revisa la sección `## Outputs Esperados` del archivo de la etapa. Comprueba si alguno de los archivos (o carpetas) listados ya existe.

**Verifica primero los casos especiales:** Algunas etapas tienen comportamiento especial cuando sus artefactos ya existen — revisa la sección `## Casos Especiales` del archivo de etapa antes de continuar. Si la etapa define un manejo especial, síguelo. Puede instruirte a omitir este protocolo por completo, usar un artefacto disparador diferente, o manejar la finalización parcial de otro modo.

---

## Paso 2: Leer y resumir

Por cada artefacto existente:

1. **Léelo**
2. **Muestra un breve resumen** — 2 a 5 puntos cubriendo el contenido clave y las decisiones tomadas

---

## Paso 3: Preguntar por qué lo estamos revisando

Pregunta al usuario por qué se está ejecutando esta etapa nuevamente y presenta estas opciones:

> "Los artefactos de salida de esta etapa ya existen (resumen arriba). ¿Por qué los estamos revisando?"

- **Iteración** — Refinar, expandir o mejorar el trabajo existente
- **Cambio de dirección del proyecto** — Los objetivos o el alcance han cambiado; parte o todo esto puede ya no aplicar
- **Cambio de stack tecnológico** — Se tomaron decisiones tecnológicas distintas; el contenido específico de tecnología necesita actualización
- **Corrección de errores** — Algo en el artefacto es factualmente incorrecto y necesita corrección
- **Otro** — El usuario describe otra razón

---

## Paso 4: Proceder según la razón

| Razón | Cómo proceder |
|-------|---------------|
| **Iteración** | Cargar como estado actual. Construir sobre él. No reiniciar desde cero. |
| **Cambio de dirección** | Empezar de cero. Conservar el artefacto existente solo como referencia histórica — no estar vinculado por decisiones previas. |
| **Cambio de stack** | Actualizar en su lugar. Enfocar los cambios en las secciones específicas de tecnología. Las decisiones estructurales y de dominio permanecen salvo que el usuario las cambie. |
| **Corrección de errores** | Cargar el artefacto, identificar el error específico, corregirlo. Actualizar en su lugar. |
| **Otro** | Pedir más contexto, luego decidir juntos cómo proceder. |

---

Después de completar este protocolo, continúa con el proceso de la etapa (Paso 5 de `start-stage`).
