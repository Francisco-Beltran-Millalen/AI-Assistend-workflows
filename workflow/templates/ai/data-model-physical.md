# Modelo de Datos — Físico (PostgreSQL)

---

## Mapeo de Tipos

| Conceptual | PostgreSQL |
|------------|------------|
| identificador | SERIAL PRIMARY KEY o BIGSERIAL PRIMARY KEY |
| texto (corto) | VARCHAR(n) |
| texto (largo) | TEXT |
| número (entero) | INTEGER |
| número (decimal) | NUMERIC(p, s) |
| booleano | BOOLEAN |
| fecha/datetime | TIMESTAMPTZ |
| enum | TEXT con restricción CHECK o tipo ENUM personalizado |

---

## Schema

### Tabla [entidad]

| Columna | Tipo | Restricciones |
|---------|------|---------------|
| id | SERIAL | PRIMARY KEY |
| [col] | TEXT | NOT NULL |
| [col] | INTEGER | NOT NULL DEFAULT 0 |
| [col] | VARCHAR(255) | UNIQUE NOT NULL |
| created_at | TIMESTAMPTZ | NOT NULL DEFAULT NOW() |
| updated_at | TIMESTAMPTZ | NOT NULL DEFAULT NOW() |

**Claves foráneas:**
- `[col]` → `[otra_tabla].id` (ON DELETE CASCADE)

**Índices:**
- `idx_[entidad]_[col]` en `[col]` — [razón]

---

### Tabla [entidad]

| Columna | Tipo | Restricciones |
|---------|------|---------------|
| id | SERIAL | PRIMARY KEY |
| [col] | TEXT | NOT NULL |
| [fk_col] | INTEGER | NOT NULL REFERENCES [otra_tabla](id) ON DELETE RESTRICT |
| created_at | TIMESTAMPTZ | NOT NULL DEFAULT NOW() |
| updated_at | TIMESTAMPTZ | NOT NULL DEFAULT NOW() |

**Índices:**
- `idx_[entidad]_[fk_col]` en `[fk_col]` — búsqueda por clave foránea

---

## Datos de Prueba (Mock Data)

Mínimo 4 filas por tabla. Ver `docs/assets/schema.sql` para los INSERT completos.

---

*Generado: [Fecha]*
*Etapa: 2-2 - Modelado de Dominio y Datos*
