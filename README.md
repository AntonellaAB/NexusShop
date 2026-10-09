# NexusShop — Buenas Prácticas y ayudamemoria

Bienvenido/a al repositorio oficial de **NexusShop**, nuestro proyecto de e-commerce desarrollado en **Python** y **Django**. 

Para evitar problemas de compatibilidad, inconsistencias de entorno o conflictos en el repositorio , **todo el equipo debe seguir este documento al pie de la letra**.

---

## Reglas del Repositorio (OBLIGATORIO)

1. **PROHIBIDO hacer `git push` directo a la rama `main`:** La rama `main` es sagrada y contiene código estable probado. Aqui se hace merge luego de cada sprint solamente.
2. **Uso estricto de ramas por Feature / Tarea:** Cada desarrollador trabaja en su propia rama dedicada (ejemplo: `feature/login`, `feature/carrito`, `fix/estilos`).
3. **Aprobación de Pull Requests (PR):** Únicamente **Antonella** (admin del repositorio) revisa, aprueba y resuelve conflictos antes de hacer Merge a `develop`.
4. **Entorno Virtual Aislado (`venv`) Obligatorio:** Todos debemos usar la versión unificada de Python 3.12+ para evitar incompatibilidades de dependencias.
5. **NUNCA subir el entorno virtual (`venv/`) ni la base de datos local (`db.sqlite3`):** Antes de cada commit, verifica con `git status` que no estés subiendo archivos no deseados.
6. Si se hace merge se hace en la rama de **develop**

---

## Setup Inicial

Sigue estos pasos la primera vez que descargues el proyecto en tu computadora.

#### 1. Clonar el Repositorio
Abre tu terminal (PowerShell, Git Bash o Terminal de VS Code) en la carpeta donde guardas tus proyectos y ejecuta:

```bash
git clone [https://github.com/AntonellaAB/NexusShop.git](https://github.com/AntonellaAB/NexusShop.git)
cd nexusShop 
```

#### 2. Iniciar el entorno virtual
En la terminal del VS code ingresar:
```bash
python-m venv venv
```
Activamos el espacio virtual con: 
```bash
venv\Scripts\activate
```
Y para asegurarnos que se activo deberíamos de ver esto <span style="color: #008000;">(venv)</span> al inicio de cada línea de comando:

<span style="color: #008000;">(venv)</span> PS: C:\> 

#### 3.Descargar Django y versiones necesarias 
```bash
pip install -r requirements.txt
```


## Rutina de trabajo
#### Se actualiza el repo principal
```bash
git checkout develop
```
#### Descarga los cambios mas recientes
```bash
git pull origin develop
```
#### Muevete a TU rama asignada
```bash
git checkout feature/lo_que_sea
```
#### Dentro de tu rama haz
```bash
git merge develop
```

#### Terminas de trabajar 
```bash
git add .
```
```bash
git commit -m "TU COMENTARIO"
```
```bash
git push origin feature/lo_que_sea
```


