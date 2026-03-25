# Data Model — Physical (PostgreSQL)

---

## Type Mapping

| Conceptual | PostgreSQL |
|------------|------------|
| identifier | SERIAL PRIMARY KEY or BIGSERIAL PRIMARY KEY |
| text (short) | VARCHAR(n) |
| text (long) | TEXT |
| number (int) | INTEGER |
| number (decimal) | NUMERIC(p, s) |
| boolean | BOOLEAN |
| date/datetime | TIMESTAMPTZ |
| enum | TEXT with CHECK constraint or custom ENUM type |

---

## Schema

### [entity] table

| Column | Type | Constraints |
|--------|------|-------------|
| id | SERIAL | PRIMARY KEY |
| [col] | TEXT | NOT NULL |
| [col] | INTEGER | NOT NULL DEFAULT 0 |
| [col] | VARCHAR(255) | UNIQUE NOT NULL |
| created_at | TIMESTAMPTZ | NOT NULL DEFAULT NOW() |
| updated_at | TIMESTAMPTZ | NOT NULL DEFAULT NOW() |

**Foreign keys:**
- `[col]` → `[other_table].id` (ON DELETE CASCADE)

**Indexes:**
- `idx_[entity]_[col]` on `[col]` — [reason]

---

### [entity] table

| Column | Type | Constraints |
|--------|------|-------------|
| id | SERIAL | PRIMARY KEY |
| [col] | TEXT | NOT NULL |
| [fk_col] | INTEGER | NOT NULL REFERENCES [other_table](id) ON DELETE RESTRICT |
| created_at | TIMESTAMPTZ | NOT NULL DEFAULT NOW() |
| updated_at | TIMESTAMPTZ | NOT NULL DEFAULT NOW() |

**Indexes:**
- `idx_[entity]_[fk_col]` on `[fk_col]` — foreign key lookup

---

## Mock Data

Minimum 4 rows per table. See `docs/assets/schema.sql` for full INSERT statements.

---

*Generated: [Date]*
*Stage: 2-2 - Data Modeling*
*Input: data-model-conceptual.md, tech-stack-consolidation.md*
