# Async

Cuando hablamos de código **asíncrono**, lo que estamos diciendo al computador es que en esa parte del código tendrá que **esperar**, porque algo se está ejecutando y hay que esperar a que finalice.

Para indicar esto al computador utilizamos la palabra **async**, y en la línea del código donde tiene que esperar usamos la palabra **await**.

Por norma, debemos usar código **async** cuando estamos trabajando:

1. Con bibliotecas de terceros.
2. Cuando estamos haciendo llamadas a una API.
3. Cuando estamos trabajando con bases de datos.

Por lo general, cuando no sabemos si es necesario o no, lo que debemos hacer es declarar la **función de forma normal** (sin `async`).

---

## Esperando pero trabajando

Cuando usamos **async**, el computador **no se queda esperando** a que la función termine de ejecutarse sin hacer nada.

Lo que pasa es que, aunque esté esperando que termine una tarea que tiene **await**, puede seguir ejecutando otras partes del código.

Cuando la función con **await** termina, el programa vuelve a continuar la ejecución **a partir de ese punto**.

---

### Concurrency

Cuando hablamos de **concurrency** en :contentReference[oaicite:0]{index=0} estamos hablando de la capacidad del computador de **manejar varias tareas casi al mismo tiempo**.

No significa que se ejecuten exactamente al mismo tiempo, sino que el sistema va:

- ejecutando una tarea,
- pausándola,
- ejecutando otra,
- y cuando es posible vuelve a continuar la anterior.

Esto ocurre hasta que se terminan todas las tareas o peticiones que están en proceso.

---

### Parallelism

Cuando hablamos de **parallelism** (paralelismo), estamos hablando de la capacidad del computador de **ejecutar varios procesos realmente al mismo tiempo**, normalmente usando varios núcleos del CPU.

La diferencia es que cada proceso puede ejecutarse **desde el inicio hasta el final sin pausarse**.

La ventaja es que se pueden ejecutar muchos procesos al mismo tiempo.  
La desventaja es que cada proceso ocupa recursos del CPU mientras se ejecuta hasta terminar.