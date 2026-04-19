# Modelo de Datos — Conceptual

Agnóstico de tecnología. Sin tipos SQL, sin claves primarias, sin timestamps.

---

## Entidades

### [Nombre de Entidad]

**Descripción:** [Qué representa en el dominio]

| Atributo | Tipo (Genérico) | Requerido | Descripción |
|----------|----------------|-----------|-------------|
| [attr] | texto | Sí | [desc] |
| [attr] | número | No | [desc] |
| [attr] | booleano | Sí | [desc] |
| [attr] | fecha | No | [desc] |
| [attr] | enum([A], [B]) | Sí | [desc] |

**Relaciones:**
- [campo] → [Entidad] (N:1) — [descripción]
- [campo] → [Entidad] (1:N) — [descripción]

---

### [Nombre de Entidad]

**Descripción:** [Qué representa]

| Atributo | Tipo (Genérico) | Requerido | Descripción |
|----------|----------------|-----------|-------------|
| [attr] | texto | Sí | [desc] |

**Relaciones:**
- [campo] → [Entidad] (N:M) — [descripción]

---

## Enums

### [NombreEnum]
| Valor | Descripción |
|-------|-------------|
| [VALOR] | [Descripción] |
| [VALOR] | [Descripción] |

---

## Diagrama de Relaciones entre Entidades

```mermaid
erDiagram
    [EntidadA] ||--o{ [EntidadB] : [relación]
    [EntidadB] }o--|| [EntidadC] : [relación]
```

---

*Generado: [Fecha]*
*Etapa: 2-2 - Modelado de Dominio y Datos*
