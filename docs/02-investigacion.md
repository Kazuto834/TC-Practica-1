# Fundamentos de la Teoría de la Computación

**Autores:** García Castillo Mario, Navarro Domínguez Antonio
**Fecha:** 3 de octubre de 2026

## 1. Introducción

La Teoría de la Computación puede considerarse el pilar matemático de las ciencias de la computación. Su objetivo central es modelar el proceso de cálculo para comprender qué problemas pueden ser resueltos mediante algoritmos y cuántos recursos (tiempo y memoria) son necesarios para lograrlo, además de cómo representar formalmente dichos procesos.

Al conceptualizar esta disciplina, distintos académicos la abordan desde perspectivas complementarias:

* **Michael Sipser** enfoca la teoría hacia los límites de la resolución de problemas. Para él, la disciplina busca responder fundamentalmente qué hace que un problema sea resoluble o intratable, clasificándolos según la cantidad de recursos que demanda su solución.
* **John Hopcroft y Jeffrey Ullman** presentan una definición más estructural y mecanicista, orientada al modelado de hardware y software a través de abstracciones matemáticas. Definen la disciplina mediante el estudio de los autómatas (máquinas abstractas) y los lenguajes formales que estas máquinas son capaces de reconocer y procesar.

Mientras Sipser adopta un enfoque ontológico sobre la naturaleza de los problemas (qué se puede resolver), Hopcroft y Ullman se centran en el constructo matemático subyacente de la máquina (cómo se procesa la información mediante estados).

## 2. Contexto Histórico

Los cimientos de estas interrogantes surgieron mucho antes de la invención de las computadoras y en general, de la electrónica moderna, arraigados en una crisis matemática a principios del siglo XX. En la década de 1920, el matemático David Hilbert propuso el **programa de Hilbert**, un intento monumental de asentar todas las matemáticas sobre un conjunto finito, sólido e incuestionable de axiomas. Su objetivo era demostrar que las matemáticas eran consistentes (no contenían contradicciones lógicas) y completas (toda afirmación verdadera podía ser probada matemáticamente).

Como parte de este programa, Hilbert planteó el *Entscheidungsproblem* o problema de decisión en 1928: pedía encontrar un procedimiento mecánico general que, dado cualquier enunciado lógico de las matemáticas, pudiera determinar infaliblemente en un número finito de pasos si dicho enunciado era verdadero o falso.

Este sueño formalista comenzó a fracturarse con el surgimiento de paradojas en la lógica matemática, siendo la más notable la Paradoja de Russell, que demostró contradicciones fundamentales en la teoría de conjuntos ingenua al plantear el problema del "conjunto de todos los conjuntos que no se contienen a sí mismos".

El colapso definitivo del programa de Hilbert ocurrió en 1931, cuando Kurt Gödel publicó sus **Teoremas de Incompletitud**. Gödel demostró que cualquier sistema matemático lo suficientemente complejo para describir la aritmética básica es inherentemente incompleto; siempre existirán verdades matemáticas que no pueden ser probadas dentro de ese mismo sistema. En 1936, Alan Turing dio la estocada final al *Entscheidungsproblem* al crear un modelo matemático abstracto (la Máquina de Turing) y demostrar, mediante el **Problema de la Parada** (*Halting Problem*), que no existe ningún algoritmo capaz de predecir si un programa arbitrario se detendrá o se ejecutará para siempre.

## 3. Ramas Principales y la Tesis de Church-Turing

Para abordar el estudio de los algoritmos y las máquinas, la Teoría de la Computación se divide en tres ramas fundamentales:

1. **Teoría de Autómatas y Lenguajes Formales:** Estudia las máquinas matemáticas abstractas y las reglas sintácticas que generan conjuntos de cadenas. Responde a la pregunta: ¿Cuáles son los modelos matemáticos de la computación y qué clases de estructuras lógicas (lenguajes) pueden procesar?
2. **Teoría de la Computabilidad:** Clasifica los problemas en resolubles e irresolubles. Abstrae por completo las limitaciones de tiempo o memoria de los ordenadores físicos para responder a la pregunta fundamental: ¿Qué problemas pueden ser computados matemáticamente por un algoritmo y cuáles son lógicamente imposibles de resolver por cualquier máquina?
3. **Teoría de la Complejidad:** Toma los problemas que ya se sabe que son computables y los clasifica según su viabilidad práctica. Responde a la pregunta: ¿Qué problemas pueden ser resueltos de manera eficiente (en tiempo polinómico) y cuáles son computacionalmente intratables porque requerirían un tiempo exponencial infactible en la práctica?

En el núcleo de todas estas ramas reside la **Tesis de Church-Turing**. Esta tesis afirma que cualquier concepto intuitivo que los seres humanos tenemos sobre un "algoritmo" o un "procedimiento efectivamente calculable" puede ser emulado y resuelto por una Máquina de Turing.

A mediados de la década de 1930, Alonzo Church y Alan Turing trabajaron de manera independiente en la formalización del concepto de computación. Church desarrolló un sistema basado en la abstracción de funciones llamado *Cálculo Lambda*, mientras que Turing propuso la *Máquina de Turing*, basada en la manipulación mecánica de símbolos en una cinta infinita. Al mismo tiempo, Kurt Gödel y Stephen Kleene desarrollaron las *Funciones Recursivas*. Posteriormente se demostró matemáticamente que estos tres modelos son equivalentes.

Se denomina "tesis" y no "teorema" porque establece una equivalencia entre un concepto informal, subjetivo e intuitivo y una definición matemática rigurosa (la Máquina de Turing). Dado que no existe una definición matemática previa para la intuición humana del cálculo, la tesis no puede ser probada mediante una deducción lógica estricta. Sin embargo, al no haber encontrado ningún modelo que supere a la Máquina de Turing, la tesis es universalmente aceptada como una ley de las ciencias de la computación.

## 4. Lenguajes Formales y Operaciones Básicas

La información que procesan estas máquinas abstractas se formaliza mediante la teoría de lenguajes formales, la cual se construye sobre tres definiciones axiomáticas:

* **Alfabeto ($\Sigma$):** Un conjunto finito, indivisible y no vacío de símbolos elementales. Ejemplo: $\Sigma=\{0,1\}$.
* **Cadena ($w$):** Una secuencia finita de símbolos concatenados elegidos de un alfabeto específico. Ejemplo: $w_{1}=0110$.
* **Lenguaje ($L$):** Un conjunto matemático de cadenas formadas exclusivamente a partir de un alfabeto dado. Ejemplo: $L=\{1,10,11,100,101,\dots\}$

### 4.1. Operaciones Matemáticas sobre Cadenas y Lenguajes

* **Concatenación:** Une dos cadenas o elementos de dos lenguajes. Si $L_{1}=\{a,b\}$ y $L_{2}=\{0,1\}$, entonces $L_{1}L_{2}=\{a0,a1,b0,b1\}$.
* **Potencia ($w^{n}$ o $L^{n}$):** Concatenación de un elemento consigo mismo $n$ veces. Si $L=\{1,0\}$, $L^{2}=\{11,10,01,00\}$.
* **Reflexión (Reverso):** Inversión del orden de los símbolos $(w=abc \Rightarrow w^{R}=cba)$.
* **Unión ($L_{1} \cup L_{2}$):** Conjunto de cadenas que pertenecen al primer lenguaje, al segundo, o a ambos.
* **Intersección ($L_{1} \cap L_{2}$):** Conjunto de cadenas comunes a ambos lenguajes.
* **Diferencia ($L_{1} - L_{2}$):** Conjunto de cadenas que pertenecen a $L_{1}$ pero no a $L_{2}$.

Dos de las operaciones más críticas son la **Cerradura de Kleene ($L^{*}$)**, que genera el conjunto de todas las cadenas posibles incluyendo la cadena vacía ($\lambda$ o $\epsilon$), y la **Cerradura Positiva ($L^{+}$)**, que requiere que la concatenación ocurra al menos una vez. 

Matemáticamente:
$$L^{+} = L^{*} - \{\lambda\}$$

## 5. Jerarquía de Chomsky y Autómatas Finitos

Noam Chomsky propuso en 1956 una clasificación jerárquica de las gramáticas formales:

* **Tipo 0 (Recursivamente Enumerable):** Sin restricciones. Generados por gramáticas irrestrictas y reconocidos por una Máquina de Turing.
* **Tipo 1 (Sensible al Contexto):** Reconocidos por un Autómata Linealmente Acotado (LBA).
* **Tipo 2 (Libre de Contexto):** Reconocidos por el Autómata de Pila (memoria LIFO). Ejemplo: el lenguaje $a^n b^n$.
* **Tipo 3 (Regular):** El nivel más restrictivo. Generados por expresiones regulares y reconocidos por Autómatas Finitos.

### 5.1. Autómatas Finitos

Un Autómata Finito se representa mediante una tupla matemática de 5 elementos: 
$$M = (Q, \Sigma, \delta, q_{0}, F)$$

* **$Q$:** Conjunto finito de estados.
* **$\Sigma$:** Alfabeto.
* **$\delta$:** Función de transición.
* **$q_{0}$:** Estado inicial.
* **$F$:** Conjunto de estados finales o de aceptación.

En un Autómata Finito Determinista (AFD), las transiciones para cada símbolo son únicas. Para reconocer cadenas binarias que terminan en "01":

$$Q=\{q_{0},q_{1},q_{2}\}, \quad \Sigma=\{0,1\}, \quad F=\{q_{2}\}$$

Las transiciones se definen como:
* $\delta(q_{0},0) = q_{1}$
* $\delta(q_{1},0) = q_{1}$
* $\delta(q_{2},0) = q_{1}$
* $\delta(q_{0},1) = q_{0}$
* $\delta(q_{1},1) = q_{2}$
* $\delta(q_{2},1) = q_{0}$

Por el Teorema de Kleene, todo Autómata Finito No Determinista (AFN) puede transformarse en un AFD equivalente.

## 6. Aplicaciones Prácticas

* **Construcción de Compiladores e Intérpretes:** Análisis léxico mediante expresiones regulares y AFD para generar tokens.
* **Validación de Entradas en UI:** Verificación de correo electrónico, contraseñas e IPv4.
* **Auditoría y Monitoreo (Log Parsing):** Uso de herramientas como `grep` y `awk` basadas en autómatas finitos.

---

## Referencias
Consultar fuentes en: [bibliografias](docs/bibliografia.md)