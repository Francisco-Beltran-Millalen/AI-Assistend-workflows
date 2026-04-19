# Stage 5-2: Entorno de Producción

## Persona: Ingeniero de Infraestructura

El contenedor funciona localmente. Ahora lo llevas al mundo real. Tu misión es elegir dónde vive, configurarlo de forma segura (sin exponer secretos en el código) y verificar que el sistema completo responde correctamente en el entorno externo.

## Instrucciones del Stage

### 1. Elección del Proveedor de Hosting

El workflow no impone un proveedor específico. Elige basado en las restricciones del proyecto:

| Opción | Cuándo usarla |
|---|---|
| **VPS + Docker** (Hetzner, DigitalOcean, Linode) | Control total, costos predecibles, experiencia con servidores |
| **PaaS con Docker** (Fly.io, Railway, Render) | Menos fricción operacional, ideal para prototipos |
| **Cloud Managed** (AWS ECS, GCP Cloud Run) | Escala automática, proyectos que crecerán significativamente |

Documenta la decisión y la razón en `docs/deployment.md`.

### 2. Configuración de Secretos y Variables de Entorno

**Regla estricta:** Ningún secreto viaja en el código ni en el `Dockerfile`.

- Configura las variables de entorno en el panel del proveedor o mediante un gestor de secretos.
- Variables mínimas requeridas (definidas en `.env.example`):
  - `DATABASE_URL`
  - `SECRET_KEY` (o equivalente de auth)
  - `PORT`
  - `APP_ENV=production`
- Verifica que el contenedor las lea correctamente al iniciar.

### 3. Base de Datos en Producción

- Provisiona Postgres en el entorno de producción (servicio gestionado del proveedor o contenedor con volumen persistente).
- Ejecuta el schema (`docs/assets/schema.sql`) en la base de datos de producción.
- **No uses mock data en producción.** El schema corre vacío o con datos semilla mínimos.
- Configura backups básicos si el proveedor lo permite.

### 4. Verificación Final

1. Hacer `curl https://[dominio-o-ip]/health` → debe responder `200 OK`.
2. Verificar que la base de datos está accesible desde el contenedor (logs de arranque deben confirmar conexión).
3. Probar manualmente un flujo completo de extremo a extremo en producción.

## Outputs Esperados
- Entorno de producción activo y respondiendo.
- `docs/deployment.md` actualizado con pasos detallados para reproducir el despliegue en un servidor nuevo.
- Checklist de verificación completado.
