# Habilidad: Exportar Log (export-log)

Exporta la conversación actual a un archivo de log en `docs/logs/`.

## Argumentos

- Identificador de etapa:
  - `0` para meta-workflow
  - `teacher` para el modo profesor
  - `<fase>-<etapa>` para etapas regulares (ej. `2-1` para Fase 2 Etapa 1)

## Proceso

1. Encontrar el archivo de transcript de la sesión actual — la ubicación es específica por herramienta, definida en el adaptador CLI
2. Ejecutar el script conversor específico de la herramienta para convertirlo a texto legible
3. Guardar en `docs/logs/` usando la convención de nombres indicada abajo

**Formato de nombre:** `stage-<identificador>-<nombre>-<YYYYMMDD>-<HHMMSS>.txt`

Ejemplos:
- `stage-00-meta-workflow-20260203-091500.txt`
- `stage-2-1-sketching-de-interfaz-20260203-143022.txt`

## Nombres de Etapa

### Etapas Bajo Demanda
- 0 → `00-meta-workflow`
- teacher → `teacher`

### Fase 1: Descubrimiento + Selección de Stack
- 1-1 → `1-1-project-brief-y-casos-de-uso`
- 1-2 → `1-2-stack-tecnico-y-arquitectura`
- 1-3 → `1-3-consolidacion`

### Fase 2: Sketching y Modelado de Datos
- 2-1 → `2-1-sketching-de-interfaz`
- 2-2 → `2-2-modelado-de-dominio-y-datos`
- 2-3 → `2-3-diseno-de-api-y-rutas`
- 2-4 → `2-4-consolidacion`

### Fase 3: Pulido UI y Arquitectura Frontend
- 3-1 → `3-1-arquitectura-frontend-y-css`
- 3-2 → `3-2-componentes-e-interactividad`
- 3-3 → `3-3-ensamblaje-de-vistas`
- 3-4 → `3-4-consolidacion`

### Fase 4: Implementación del Prototipo
- 4-1 → `4-1-setup-y-arquitectura-base`
- 4-2 → `4-2-planificacion-por-caso-de-uso`
- 4-3 → `4-3-implementacion-mecanica`
- 4-4 → `4-4-auditoria-y-refactor`

### Fase 5: Despliegue
- 5-1 → `5-1-build-optimizado-y-contenedor`
- 5-2 → `5-2-entorno-de-produccion`
- 5-3 → `5-3-pipeline-cicd`
