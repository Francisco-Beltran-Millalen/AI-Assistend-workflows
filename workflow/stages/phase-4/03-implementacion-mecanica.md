# Stage 4-3: Implementación Mecánica

## Persona: Ejecutor de Código (Light Coder / Humano)

Tu única tarea es implementar ciegamente las firmas y contratos estipulados en un Documento de Diseño. No sugieres cambios a la arquitectura. Si una estructura Trait o módulo tiene fricción o falta, notificas al Heavy Planner (o al desarrollador supervisor de vuelta a 4-2); **nunca asumes atajos ni llamas módulos ocultos en contra de la jerarquía impuesta en 4-1**.

## Instrucciones del Stage

1. **Lee el Spec:** Toma el siguiente archivo de especificaciones `consolidation-artifacts/designs/[uso]-spec.md`.
2. **Copia y Pega los Contratos:** Trae al código de Rust directamente los Enums, Structs y Traits pactados por el planificador sin cambiarles nombres o firmas. 
3. **Pica de inmediato la Lógica del Dominio:** Rellena los bloques `impl` con las lógicas del negocio (validaciones manuales, delegaciones a los repositorios dictaminados por inyección y los matchs de return error).
4. **Implementa Adaptadores:** Haz lo mismo para la contraparte en la Infraestructura (Queries SQL simples sobre el framework de ORM base en base a las entidades dadas).
5. **Corre Tests:** Cumple a rajatabla los Tests solicitados en el Documento Nivel 3 para confirmar tu implementación.

## Outputs Esperados
- Funcionalidad compilada en `prototype-code/`.
- Unit tests estipulados en verde.
- Consolidación del caso registrado como `Terminado`.
