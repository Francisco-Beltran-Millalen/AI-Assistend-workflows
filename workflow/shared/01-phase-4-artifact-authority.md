# Fase 4: Autoridad de Actualización de Artefactos de Consolidación

Las personas de la Fase 4 tienen autoridad — y responsabilidad — de actualizar los artefactos de consolidación cuando la implementación revela que el diseño necesita cambiar.

## Por qué existe esto

Los artefactos de consolidación son la fuente de verdad. Los archivos en `docs/` de las fases anteriores son históricos. Cuando la implementación descubre una discrepancia o un cambio necesario, el artefacto de consolidación debe actualizarse para reflejar la realidad.

## Cuándo aplicarlo

Cuando cualquier etapa de la Fase 4 encuentre:
- Un contrato de API que no coincide con lo que la implementación requiere
- Un modelo de datos que necesita ajuste (nueva columna, tipo cambiado, tabla faltante)
- Una definición de caso de uso que necesita aclaración o cambio de alcance
- Una decisión de stack tecnológico que necesita revisión

## Protocolo

1. **Detente** — no hagas el cambio silenciosamente ni trabajes alrededor del problema
2. **Notifica** al usuario:
   > "El `[nombre-artefacto]` actual dice [X]. La implementación revela que necesitamos [Y] porque [razón]. Propongo actualizar el artefacto — ¿de acuerdo?"
3. **Obtén aprobación explícita** antes de modificar el artefacto
4. **Actualiza el artefacto de consolidación** con el cambio
5. **Registra en el spec del caso de uso** (`consolidation-artifacts/designs/[caso]-spec.md`) bajo `## Notas de Implementación`:

```
### YYYY-MM-DD — [resumen en una línea]
Artefacto: [nombre de archivo]
Cambio: [qué cambió precisamente]
Razón: [qué descubrió la implementación que requirió este cambio]
```

## Alcance de la Autoridad

| Tipo de cambio | Autoridad |
|----------------|-----------|
| Renombrar campo, corregir tipo, agregar campo faltante | Actualizar + registrar |
| Nuevo endpoint o reestructuración de endpoint | Actualizar + registrar |
| Nueva entidad o tabla | Actualizar + registrar |
| Eliminar un caso de uso del alcance | El usuario debe estar explícitamente de acuerdo — marcar claramente |
| Cambiar objetivos del proyecto o restricciones centrales | Fuera del alcance de la Fase 4 — requiere Etapa 0 |

## Qué NO hacer

- No actualices los archivos en `docs/` — son históricos; los artefactos de consolidación son los activos
- No hagas correcciones silenciosas — cada cambio debe ser registrado
- No inventes cambios para "mejorar" el diseño — solo cambia lo que la implementación genuinamente requiere
