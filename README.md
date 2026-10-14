# 🇲🇽 🎧 Spotify México: Trends & Popular Artists Dashboard (2015 - 2024)

¡Bienvenido al repositorio oficial del **Spotify México Analytics Dashboard**! 🚀

Este proyecto es una herramienta de inteligencia de datos e interactiva diseñada para explorar, analizar y visualizar la evolución de la música más escuchada en México durante la última década. A través de métricas clave como el índice bailable (*danceability*), la energía de las pistas, reproducciones estimadas y el país de origen de los artistas, esta aplicación permite descubrir los patrones que definen el consumo musical en una de las regiones más influyentes de la industria global.

> *"Sin música, la vida sería un error, y sin datos sobre la música, nos perderíamos las historias detrás de los éxitos que mueven al mundo."*

---

## 🌟 Características Principales

* **📊 Visualización Interactiva:** Gráficos dinámicos e intuitivos desarrollados con **Plotly Express** (barras, gráficos de dona e histogramas).
* **🎛️ Filtros Avanzados:** Filtrado multidimensional por género, país, rango de años y características de los artistas (*tracks* en Top 10, nominaciones a Grammys o talento nacional).
* **📈 KPIs en Tiempo Real:** Métricas resumen que calculan promedios de oyentes, reproducciones acumuladas e índices musicales al instante.
* **🔍 Exploración Directa:** Módulo para inspeccionar el *dataset* en bruto filtrado para mayor transparencia analítica.

---

## 🛠️ Tecnologías Utilizadas

La solución está construida sobre un *stack* moderno, ligero y altamente escalable en Python:

* 🐍 **Python 3.9+** — Lenguaje principal de desarrollo.
* 🎈 **Streamlit** — *Framework* para la creación rápida de aplicaciones web interactivas de datos.
* 📊 **Plotly Express** — Librería para la generación de gráficos interactivos de alto impacto visual.
* 🐼 **Pandas** — Manipulación, limpieza y análisis estructurado del *dataset*.

---

## 📁 Estructura del Proyecto

```text
├── data/
│   └── datos.csv         # Conjunto de datos sobre cantantes populares en México
├── app.py                # Aplicación principal de Streamlit
├── requirements.txt      # Dependencias y librerías del proyecto
└── README.md             # Documentación del proyecto
```

---

## 🚀 Instrucciones de Instalación Local

Sigue estos sencillos pasos para clonar y ejecutar el panel de control en tu máquina local:

### 1. Clonar el Repositorio
Abre tu terminal y ejecuta el siguiente comando:

```bash
git clone https://github.com/tu-usuario/spotify-mexico-dashboard.git
cd spotify-mexico-dashboard
```

### 2. Crear y Activar un Entorno Virtual (Opcional pero recomendado)

* **En macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **En Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 3. Instalar Dependencias
Asegúrate de instalar todos los paquetes necesarios enumerados en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación
Lanza el servidor local de **Streamlit**:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador web predeterminado en la dirección `http://localhost:8501`. ¡Listo para explorar! 🎉

---

## 🤝 Contribuciones y Contacto

¡Las contribuciones, sugerencias y retroalimentaciones siempre son bienvenidas! Si tienes ideas para agregar nuevas variables, mejorar las visualizaciones o incluir más modelos analíticos:

1. Haz un **Fork** del proyecto.
2. Crea tu rama de características (`git checkout -b feature/NuevaFuncion`).
3. Envía tus cambios (`git commit -m 'Añadir nueva función'`).
4. Haz **Push** a la rama (`git push origin feature/NuevaFuncion`).
5. Abre un **Pull Request**.

---

⭐ **¿Te gustó este proyecto?** ¡No olvides darle una estrella (*Star*) al repositorio para apoyar el desarrollo de más proyectos de datos abiertos!


*URL disponible* : [Top 20 MX Live](https://top-20-mexico-spotify.onrender.com/)