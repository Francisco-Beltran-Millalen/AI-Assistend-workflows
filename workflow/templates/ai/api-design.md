# Diseño de API

---

## Convenciones

- **URL Base:** `/api/v1`
- **Auth:** `Authorization: Bearer <token>`
- **Content-Type:** `application/json`
- **Errores:** `{ "error": { "code": "CODIGO_ERROR", "message": "Mensaje legible por humanos" } }`

---

## Códigos de Estado HTTP

| Estado | Cuándo |
|--------|--------|
| 200 OK | Éxito en GET, PATCH, PUT |
| 201 Created | Éxito en POST |
| 204 No Content | Éxito en DELETE |
| 400 Bad Request | Error de validación |
| 401 Unauthorized | Auth ausente o inválida |
| 403 Forbidden | Permisos insuficientes |
| 404 Not Found | Recurso no encontrado |
| 409 Conflict | Violación de regla de negocio |

---

## Endpoints

### [Recurso]

#### GET /[recurso]

**Caso de uso:** [nombre UC] | **Auth:** Requerida

**Parámetros de consulta:** `page` (default: 1), `per_page` (default: 20)

**Respuesta 200:**
```json
{
  "data": [
    { "id": 1, "[campo]": "[valor]" }
  ],
  "meta": { "page": 1, "per_page": 20, "total": 45 }
}
```

---

#### GET /[recurso]/:id

**Caso de uso:** [nombre UC] | **Auth:** Requerida

**Respuesta 200:**
```json
{ "id": 1, "[campo]": "[valor]" }
```

**Errores:** `NOT_FOUND` 404

---

#### POST /[recurso]

**Caso de uso:** [nombre UC] | **Auth:** Requerida

**Request:**
```json
{ "[campo]": "[valor]" }
```

**Respuesta 201:**
```json
{ "id": 1, "[campo]": "[valor]" }
```

**Errores:** `VALIDATION_ERROR` 400

---

#### PATCH /[recurso]/:id

**Caso de uso:** [nombre UC] | **Auth:** Requerida

**Request:**
```json
{ "[campo]": "[valor actualizado]" }
```

**Respuesta 200:**
```json
{ "id": 1, "[campo]": "[valor actualizado]" }
```

**Errores:** `NOT_FOUND` 404, `VALIDATION_ERROR` 400

---

#### DELETE /[recurso]/:id

**Caso de uso:** [nombre UC] | **Auth:** Requerida

**Respuesta:** 204 No Content

**Errores:** `NOT_FOUND` 404

---

### Autenticación

#### POST /auth/login

**Auth:** Ninguna

**Request:**
```json
{ "email": "usuario@ejemplo.com", "password": "secreto" }
```

**Respuesta 200:**
```json
{ "token": "jwt-token", "user": { "id": 1, "email": "usuario@ejemplo.com" } }
```

**Errores:** `INVALID_CREDENTIALS` 401

---

## Mapeo Vista-Endpoint

| Vista | Endpoint | Request | Forma de Respuesta |
|-------|----------|---------|-------------------|
| [vista.html] | GET /[recurso] | — | `{ data: [...], meta: {...} }` |
| [vista.html] | POST /[recurso] | `{ campo: val }` | `{ id, campo }` |
| [vista.html] | PATCH /[recurso]/:id | `{ campo: val }` | `{ id, campo }` |
| [vista.html] | DELETE /[recurso]/:id | — | 204 |

---

*Generado: [Fecha]*
*Etapa: 2-3 - Diseño de API y Rutas*
