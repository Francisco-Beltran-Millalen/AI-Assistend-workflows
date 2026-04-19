# Stage 5-3: Pipeline CI/CD

## Persona: Ingeniero de Automatización

El entorno de producción está funcionando. Ahora lo automatizas para que nunca más tengas que hacer deploy manualmente. Un push a `main` debe disparar todo el ciclo: tests → build → deploy.

> Solo llegas aquí si la etapa 5-2 está completa. No tiene sentido automatizar un proceso que aún no funciona manualmente.

## Instrucciones del Stage

### 1. Diseño del Pipeline

Define el pipeline antes de escribirlo. El flujo estándar para este workflow es:

```
Push a main
    ↓
[CI] Ejecutar tests unitarios e integración
    ↓
[CI] cargo check / compilación básica
    ↓
[CI] docker build (imagen de producción)
    ↓
[CI] docker push al registro de imágenes
    ↓
[CD] Deploy al entorno de producción
```

Documenta cualquier desviación de este flujo en `docs/deployment.md`.

### 2. Configuración de GitHub Actions

Crea el archivo `.github/workflows/deploy.yml`. Estructura base:

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: cargo test  # adaptar al stack

  build-and-deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker image
        run: docker build -t [imagen]:[tag] .
      - name: Push to registry
        run: docker push [imagen]:[tag]
      - name: Deploy
        run: [comando de deploy del proveedor]
```

Los secretos (`DOCKER_USERNAME`, `DOCKER_PASSWORD`, llaves SSH o tokens del proveedor) deben declararse en **GitHub → Settings → Secrets and variables → Actions**. Nunca en el archivo YAML directamente.

### 3. Registro de Imágenes Docker

Elige dónde se almacenan las imágenes construidas:
- **GitHub Container Registry (GHCR):** Integración nativa con GitHub Actions, gratuito para repositorios públicos.
- **Docker Hub:** Amplio soporte, plan gratuito con límites.
- **Registry del proveedor:** AWS ECR, GCP Artifact Registry, etc.

### 4. Prueba del Pipeline

1. Hacer un push de prueba a `main` con un cambio menor.
2. Verificar que todas las etapas del pipeline pasan en la pestaña Actions de GitHub.
3. Confirmar que la nueva versión está desplegada en producción.
4. Documentar cómo revertir un deploy fallido (rollback manual o automático).

## Outputs Esperados
- `.github/workflows/deploy.yml` funcional y probado.
- `docs/deployment.md` con el proceso de CD documentado y cómo hacer rollback.
- Pipeline verde en GitHub Actions tras al menos un push real de prueba.

## Criterios de Salida de la Fase 5

- [ ] Binario release compilado y corriendo en Docker local sin errores.
- [ ] Postgres de producción activo con schema inicializado.
- [ ] Endpoint `/health` respondiendo en producción.
- [ ] GitHub Actions desplegando automáticamente en push a `main`.
- [ ] `docs/deployment.md` con instrucciones completas para reproducir el entorno.

**Con esto, el prototipo está desplegado y el workflow completo está terminado.**
