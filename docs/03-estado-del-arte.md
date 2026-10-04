# Ejercicio 3: Estado del Arte

## Artículo 1: Gribkoff, E. (2013)
> Gribkoff, E. (2013). Applications of deterministic finite automata [Documento de curso, ECS 120]. University of California, Davis. https://www.cs.ucdavis.edu/~rogaway/classes/120/spring13/eric-dfa.pdf

### Ficha de análisis
* **Problema que aborda:** Presenta diversas aplicaciones prácticas de los Autómatas Finitos Deterministas (AFD) en escenarios reales de computación, alejándolos de ser solo un concepto teórico abstracto.
* **Método o propuesta:** Emplea un enfoque expositivo mediante ejemplos concretos (como máquinas expendedoras, el comando grep y Apache Lucene) para mostrar cómo modelar problemas con AFD.
* **Resultado principal:** Demuestra que los AFD son herramientas fundamentales y eficientes, principalmente en el procesamiento de texto y reactivos simples.
* **Relación con Unidad Temática I:** Se relaciona directamente con el tema de "Autómatas finitos y expresiones regulares”.
* **Aportación al curso:** Presenta el Desarrollo de un software aplicando las bases teóricas de la teoría de la computación para su posterior implementación práctica.

### Respuestas
* **Diferencia entre AFD y Máquina de Mealy / Apache Lucene:** Un AFD acepta o rechaza cadenas basándose únicamente en llegar a un estado final o de aceptación. Una máquina de Mealy, en cambio, produce una salida específica asociada a cada transición. El autocompletado de Apache Lucene requiere la máquina de Mealy porque necesita emitir sugerencias de texto para el usuario de manera interactiva a medida que se ingresan los caracteres.
* **Consecuencia de un conjunto de estados de aceptación vacío:** En el modelo de la máquina expendedora, carecer de estados de aceptación implica que ninguna cadena de entrada será formalmente "aceptada" (el lenguaje reconocido es vacío). Esto significa que la máquina está diseñada como un sistema perpetuo que únicamente vuelve al estado inicial teniendo $1.25 o más, para seguir realizando operaciones relativas a las latas de refresco sin finalizar.
* **Afirmación a verificar:** El autor señala usos amplios de expresiones regulares, sin embargo, en implementaciones reales (como ciertas funciones avanzadas de validación de texto), se utilizan "backreferences" que exceden la capacidad de un AFD tradicional y lo vuelven un problema complejo.

---

## Artículo 2: Luna-Benoso et al. (2022)
> Luna-Benoso, B., Martínez-Perales, J. C., Cortés-Galicia, J., Flores-Carapia, R., & Silva-García, V. M. (2022). Melanoma detection in dermoscopic images using a cellular automata classifier. Computers, 11(1), 8. https://doi.org/10.3390/computers11010008

### Ficha de análisis
* **Problema que aborda:** Aborda el desafío de diagnosticar y detectar el melanoma de manera automática a partir de imágenes dermatoscópicas, para asistir en la decisión médica.
* **Método o propuesta:** Propone una metodología que utiliza un clasificador basado en autómatas celulares asociativos que opera a través de morfología celular matemática (dilatación y erosión).
* **Resultado principal:** Reportan que el método propuesto basado en autómatas celulares supera en efectividad a otros métodos del estado del arte en la segmentación y análisis de los melanomas.
* **Relación con Unidad Temática I:** Presenta los autómatas como modelos fundamentales de cómputo adaptados a arquitecturas de cálculo en paralelo y espacial.
* **Aportación al curso:** Ilustra claramente cómo conceptos que se asemejan a la teoría clásica de autómatas se extienden para abordar problemas contemporáneos.

### Respuestas a los cuestionamientos
* **Autómata celular vs. Autómata finito:** Mientras un autómata finito tiene un solo estado global a la vez que cambia secuencialmente, el autómata celular es una matriz completa de celdas. En él, el estado aplica a cada celda individual (por ejemplo 1 o 0). El vecindario es el subconjunto de celdas cercanas que afectan a una celda dada en el siguiente paso. La regla de transición local es la función que dictamina cuál será el nuevo estado de esa celda basándose en los estados actuales de su vecindario específico.
* **Problema y elección del modelo:** Abordan la detección de células cancerígenas (melanoma) en imágenes. Eligen los autómatas celulares porque capturan excelentemente las dependencias espaciales de los píxeles de una imagen mediante el vecindario local para poder hacer morfología matemática (operaciones lógicas en dos dimensiones).
* **Resultado reportado:** Evalúan con métricas de clasificación, demostrando que al aplicar reglas de transición como la dilatación o la erosión sobre los componentes en las imágenes, se obtiene una detección muy precisa (clasificación de píxeles como lesión o fondo).

---

## Artículo 3: Turing, A. M. (1936)
> Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. Proceedings of the London Mathematical Society, s2-42(1), 230-265. https://doi.org/10.1112/plms/s2-42.1.230

### Ficha de análisis
* **Problema que aborda:** El problema de decisión (Entscheidungsproblem); esto es, si existe un método general y mecánico mediante el cual puedan evaluarse como verdaderas o falsas todas las sentencias matemáticas.
* **Método o propuesta:** Formaliza el concepto del cálculo mecánico introduciendo las "a-machines" proveyendo una rigurosa definición al concepto algorítmico.
* **Resultado principal:** Se demuestra que no es posible determinar mecánicamente (con un algoritmo general) si una máquina dada se detendrá alguna vez, lo que invalida el Entscheidungsproblem.
* **Relación con Unidad Temática I:** Está en la cima de la jerarquía de Chomsky (Lenguajes sin restricciones y la máquina que los reconoce).
* **Aportación al curso:** Comprender los límites definitivos e irreducibles del cómputo.

### Respuestas a los cuestionamientos
* **Resultado y modelo:** Introduce el modelo abstracto hoy denominado Máquina de Turing. A través de este, demuestra la indecidibilidad de ciertos problemas lógicos fundamentales (la inexistencia de un algoritmo que resuelva la parada).
* **Tesis de Church-Turing:** Estipula que todo procedimiento efectivamente calculable puede ser llevado a cabo por una Máquina de Turing. Se denomina "tesis" y no "teorema" porque es un concepto intuitivo e informal (el "cálculo efectivo" o algoritmo natural), el cual no es demostrable mediante el puro rigor lógico.
* **Dificultad de lectura:** La nomenclatura y convenciones tipográficas de 1936 son densas. Turing habla de "m-configurations" y emplea convenciones lógicas arcaicas para representar lo que hoy modelamos con grafos dirigidos o tuplas explícitas de estados.
* **Nota de pie de página (sobre 1936 vs 1937):** El DOI registra el volumen en 1937 porque la encuadernación oficial en tomos de los proceedings ocurrió ese año; no obstante, el material circuló en fascículos y fue presentado originalmente en 1936, adoptando la comunidad científica esa fecha para fines de referencia histórica.

---

## Artículos 4 y 5: Artículos seleccionados recientes

### Artículo 4: Procesamiento de Lenguaje Natural en Medicina
> Wang, L., & Smith, J. (2024). Comparative performance analysis of regular expressions and a large language model for data extraction from radiological reports. JAMIA Open, 8(6), ooaf128. https://doi.org/10.1093/jamiaopen/ooaf128

* **Problema que aborda:** Extraer información estructurada compleja (puntuaciones biomédicas BI-RADS) directamente de reportes radiológicos clínicos en formato texto libre.
* **Método o propuesta:** Realiza una comparación analítica de precisión temporal y de exactitud entre las Expresiones Regulares tradicionales (equivalentes a autómatas finitos) contra las tecnologías emergentes de Modelos de Lenguaje Grandes (LLMs).
* **Resultado principal:** El sistema tradicional basado en expresiones regulares alcanzó una altísima precisión (89.20%), superando ligeramente al LLM moderno y demandando una fracción del poder de cómputo.
* **Relación con Unidad Temática I:** Aborda la aplicación directa en la industria actual del tema "Expresiones regulares" para problemas de coincidencia de patrones.
* **Aportación al curso:** Nos enseña que para tareas precisas y rigurosas, un modelo clásico basado en autómatas es, hoy en día, igual o más potente y robusto que la Inteligencia Artificial generativa.

### Artículo 5: Ciberseguridad y Redes
> Chen, Y., et al. (2025). Hyperflex: A SIMD-based DFA Model for Deep Packet Inspection. IEEE Transactions on Networking / arXiv. https://arxiv.org/abs/2512.07123

* **Problema que aborda:** La necesidad de analizar las cargas útiles (payloads) en millones de paquetes de internet a hiper-velocidad para evitar intrusiones en la red o bloquear virus.
* **Método o propuesta:** Introduce Hyperflex, un modelo de Autómata Finito Determinista (DFA) que utiliza registros SIMD (vectoriales) de microprocesadores para saltar estados de transición en la RAM a nivel físico y paralelo.
* **Resultado principal:** Mejora sustancialmente el rendimiento, reduciendo cuellos de botella de memoria en comparación con los esquemas algorítmicos tradicionales que escanean carácter por carácter el paquete.
* **Relación con Unidad Temática I:** Relacionado profundamente con el tema "definición formal del AFD", explorando cómo las transiciones pueden implementarse a nivel hardware.
* **Aportación al curso:** Subraya cómo las bases y tablas de estado de los DFA se mapean directamente en hardware contemporáneo (registros AVX512), dándonos una perspectiva ingenieril real de un tema teórico.

---

## Tabla Comparativa de Textos

| Texto | Arbitrado | Año | Modelo que usa | Campo de aplicación |
| :--- | :--- | :--- | :--- | :--- |
| 1. Gribkoff | No | 2013 | AFD / Mealy | Diseño e implementaciones de software (Búsquedas, reactividad) |
| 2. Luna-Benoso et al. | Sí | 2022 | Autómatas celulares | Detección de patologías médicas en imágenes (Salud) |
| 3. Turing, A.M. | Sí | 1936 | Máquina de Turing | Fundamentos de la Computabilidad |
| 4. Wang & Smith | Sí | 2024 | Expresiones regulares | Procesamiento de Lenguaje Natural en Reportes Médicos |
| 5. Chen et al. | Sí | 2025 | Autómatas Finitos Vectoriales | Inspección Profunda de Paquetes (Ciberseguridad) |

---

## Análisis Comparativo 

En la revisión y comparación de los cinco artículos presentados, resulta evidente la convención de todos en el uso de estos autómatas simples para la definición de problemas que podrían caber dentro de la definición de “lenguaje”, en todos se presenta un lenguaje que precede de un “alfabeto” siendo el mismo un conjunto específico de imágenes o tipos semejantes de elementos. Todos los trabajos (con distintos niveles de rigor) fundamentan la solución de problemas en la abstracción a través de estados, eventos de transición y lenguajes aceptados. Sin embargo, divergen notoriamente en la meta final. Mientras Turing y su aproximación de la década de 1930 sentaron la base fundacional de una disciplina completamente nueva operando sobre matemáticas puras y límites inamovibles de decidibilidad, los artículos modernos como el de Luna-Benoso o Chen adaptan las definiciones clásicas para que las infraestructuras contemporáneas resuelvan problemáticas pragmáticas de vida o muerte (como la identificación clínica de cáncer o el rechazo de anomalías y hackeos de red). El documento de Gribkoff, por el contrario, actúa primariamente como un mecanismo didáctico. 

Al confrontar los casos expuestos en el texto de Wang con las implementaciones contemporáneas de inteligencia artificial (LLMs), detectamos un problema abierto de particular interés de cara al futuro: Las expresiones regulares y los autómatas son rígidos y altamente determinísticos, ideales para encontrar exactitud matemática a velocidades vertiginosas. Los modelos generativos basados en conexionismo neuronal carecen de estas garantías operativas de exactitud estructural, pero resuelven las ambigüedades idiomáticas. El gran reto a nivel de investigación, y que resulta claro al leer estos enfoques opuestos, es encontrar arquitecturas que integren la inflexibilidad formal del autómata finito para las búsquedas críticas, con la flexibilidad difusa de las redes modernas y los modelos de lenguaje naturales, manteniendo la eficiencia de las problemáticas computacionales.