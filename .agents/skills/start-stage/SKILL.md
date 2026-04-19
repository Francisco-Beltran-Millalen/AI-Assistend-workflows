# Habilidad: Iniciar Etapa (start-stage)

Inicia la etapa especificada del workflow.

## Argumentos

- Identificador de etapa:
  - `0` para meta-workflow
  - `teacher` para el modo profesor
  - `<fase>-<etapa>` para etapas regulares (ej. `2-1` para Fase 2 Etapa 1)

## Instrucciones

1. Parsear el identificador de etapa y construir la ruta del archivo usando la base `workflow/stages/`:
   - Si es `0`: Leer `workflow/stages/phase-0/00-meta-workflow.md`
   - Si es `teacher`: Leer `workflow/stages/phase-0/04-teacher.md`
   - Si es `<fase>-<etapa>`: Leer `workflow/stages/phase-<fase>/0<etapa>-*.md`
2. Adoptar la persona definida en el archivo de etapa
3. Solo para etapas de las Fases 1–5 (no 0 ni teacher): verificar si los artefactos de salida de la etapa (listados en `## Outputs Esperados`) ya existen. Si alguno existe, leer `workflow/shared/00-existing-artifact-protocol.md` y seguirlo antes de proceder al paso 4.
4. Seguir el proceso de la etapa

## Mapeo de Etapas

### Etapas Bajo Demanda
- 0: meta-workflow (correcciones al workflow, operaciones git, importación de artefactos)
- teacher: profesor (enseñanza, pato de goma, prueba de conocimiento, diagramas)

### Fase 1: Descubrimiento + Selección de Stack
- 1-1: project-brief-y-casos-de-uso
- 1-2: stack-tecnico-y-arquitectura
- 1-3: consolidacion

### Fase 2: Sketching y Modelado de Datos
- 2-1: sketching-de-interfaz
- 2-2: modelado-de-dominio-y-datos
- 2-3: diseno-de-api-y-rutas
- 2-4: consolidacion

### Fase 3: Pulido UI y Arquitectura Frontend
- 3-1: arquitectura-frontend-y-css
- 3-2: componentes-e-interactividad
- 3-3: ensamblaje-de-vistas
- 3-4: consolidacion

### Fase 4: Implementación del Prototipo
- 4-1: setup-y-arquitectura-base
- 4-2: planificacion-por-caso-de-uso (una vez por caso de uso o en lote)
- 4-3: implementacion-mecanica (ejecutar por cada spec aprobada en 4-2)
- 4-4: auditoria-y-refactor (una vez, después de todos los casos de uso)

### Fase 5: Despliegue
- 5-1: build-optimizado-y-contenedor
- 5-2: entorno-de-produccion
- 5-3: pipeline-cicd

## Ejemplos de Uso

```
/start-stage 0
```
Inicia la Etapa 0 (Ingeniero de Workflow) — correcciones al workflow, operaciones git, importación de artefactos.

```
/start-stage teacher
```
Inicia la Etapa teacher (Profesor Paciente) — enseñanza, modo pato de goma, prueba de conocimiento, diagramas.

```
/start-stage 2-1
```
Inicia Fase 2, Etapa 1 (Sketching de Interfaz) con la persona de Diseñador Visual de Sistemas.

```
/start-stage 4-2
```
Inicia Fase 4, Etapa 2 (Planificación por Caso de Uso) con la persona de Diseñador Técnico.
