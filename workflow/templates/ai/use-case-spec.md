# Plantilla: Spec de Caso de Uso

> Generado en la **Etapa 4-2: Planificación por Caso de Uso**.
> Este documento es ley arquitectónica. La Etapa 4-3 implementa exactamente lo que aquí se define, sin desviaciones.

**Estado:** En Progreso / Aprobado / Implementado
**Iniciado:** YYYY-MM-DD
**Aprobado:** —
**Implementado:** —

---

## Nivel 1: Lógico y Flujo

**Actor:** [Quién realiza esta acción — ej. "usuario autenticado"]
**Objetivo:** [Qué logra — en lenguaje de negocio, no técnico]
**Disparador:** [Qué inicia esto — ej. "el usuario hace clic en 'Guardar'"]
**Éxito:** [Qué recibe cuando funciona — ej. "una confirmación con el ID creado"]

**Escenario de ejemplo:** [Una oración concreta]

**Endpoint asociado:** `MÉTODO /ruta`

---

## Nivel 2: Mapeo de Transacción y Dominio

**Validación primitiva:**
| Campo | Regla | Error |
|-------|-------|-------|
| [campo] | [requerido / max 255 / > 0] | [CODIGO_ERROR] |

**Operaciones DB:**
- Lee: `[Entidad]` donde `[condición]` — para [propósito]
- Escribe: `[Entidad]` CREATE/UPDATE — campos: [lista]

**Alcance transaccional:** [Todas las escrituras son atómicas / Solo X e Y / Ninguno requerido]

**Invariantes de dominio (reglas que pueden rechazar una request válida y autorizada):**
- [Ej: "El pedido no puede cancelarse si ya está en estado 'enviado'"] → `409 { "error": "ALREADY_SHIPPED" }`

---

## Nivel 3: Contrato de Código Exacto en Rust

> El implementador (Etapa 4-3) debe usar estas firmas exactas. Prohibido renombrar o reestructurar.

### DTOs

```rust
// DTO de entrada — validado en la capa HTTP antes de llegar al dominio
pub struct [NombreRequest] {
    pub [campo]: [Tipo],
    pub [campo]: [Tipo],
}

// DTO de salida — lo que devuelve el endpoint al cliente
pub struct [NombreResponse] {
    pub [campo]: [Tipo],
}
```

### Enum de Errores

```rust
pub enum [NombreCasoDeUso]Error {
    [VarianteError],    // ej: NotFound
    [VarianteError],    // ej: DuplicateEmail
}
```

### Port (Trait del Repositorio)

```rust
pub trait [NombreRepository] {
    fn [metodo](&self, [param]: [Tipo]) -> Result<[TipoRetorno], [NombreCasoDeUso]Error>;
}
```

### Tests Requeridos

El implementador debe escribir los siguientes tests unitarios (mínimo):

- `test_[caso_exito]` — happy path completo
- `test_[falla_validacion]` — input inválido rechazado en capa HTTP
- `test_[falla_dominio]` — invariante de dominio aplicado correctamente
- `test_[falla_repositorio]` — puerto retorna error, se propaga correctamente

---

## Notas de Implementación

*(Completar durante la Etapa 4-3. Registra ajustes al contrato, descubrimientos y desviaciones.)*
