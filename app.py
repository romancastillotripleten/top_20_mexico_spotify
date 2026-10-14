import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# Configuración de la página
# ---------------------------------------------------------
st.set_page_config(
    page_title="Spotify México Dashboard",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado para adaptar colores tipo Spotify
st.markdown("""
    <style>
    .main {
        background-color: #121212;
    }
    .stMetric {
        background-color: #e6dcdc;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #1DB954;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 1. Cargar los datos
# ---------------------------------------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/datos.csv")
        df["fecha_pico"] = pd.to_datetime(df["fecha_pico"])
        return df
    except FileNotFoundError:
        st.error("⚠️ No se encontró el archivo 'data/datos.csv'. Verifica la ruta e inténtalo de nuevo.")
        st.stop()

df = load_data()

# ---------------------------------------------------------
# 2. Título y Subtítulo llamativos
# ---------------------------------------------------------
st.title("🇲🇽 🎵 Spotify México: Tendencias & Cantantes Populares (2015 - 2024)")
st.markdown("### 🚀 Explora el impacto, métricas musicales y popularidad de los artistas más escuchados")

st.divider()

# ---------------------------------------------------------
# 4. Filtros en la barra lateral (Sidebar)
# ---------------------------------------------------------
st.sidebar.header("🎛️ Filtros Interactivos")

# Filtro Dropdown: Género
generos_disponibles = ["Todos"] + sorted(list(df["genero"].unique()))
genero_seleccionado = st.sidebar.selectbox("🎸 Selecciona un Género musical:", generos_disponibles)

# Filtro Dropdown: País de Origen
paises_disponibles = ["Todos"] + sorted(list(df["pais_origen"].unique()))
pais_seleccionado = st.sidebar.selectbox("🌍 Selecciona País de Origen:", paises_disponibles)

# Filtro Slider: Rango de Años
anio_min, anio_max = int(df["anio_chart"].min()), int(df["anio_chart"].max())
rango_anios = st.sidebar.slider(
    "📅 Rango de Años en Charts:",
    min_value=anio_min,
    max_value=anio_max,
    value=(anio_min, anio_max)
)

# Filtros Checkbox
st.sidebar.markdown("---")
st.sidebar.subheader("📌 Filtros Adicionales")
solo_mexicanos = st.sidebar.checkbox("🇲🇽 Solo Artistas Mexicanos", value=False)
solo_top_10 = st.sidebar.checkbox("🏆 Solo Tracks en Top 10", value=False)
solo_grammy = st.sidebar.checkbox("🏅 Solo Nominados al Grammy", value=False)

# ---------------------------------------------------------
# Aplicar Filtros al DataFrame
# ---------------------------------------------------------
df_filtrado = df.copy()

# Aplicar rangos de años
df_filtrado = df_filtrado[
    (df_filtrado["anio_chart"] >= rango_anios[0]) & 
    (df_filtrado["anio_chart"] <= rango_anios[1])
]

# Aplicar dropdowns
if genero_seleccionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["genero"] == genero_seleccionado]

if pais_seleccionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["pais_origen"] == pais_seleccionado]

# Aplicar checkboxes
if solo_mexicanos:
    df_filtrado = df_filtrado[df_filtrado["es_artista_mexicano"] == True]

if solo_top_10:
    df_filtrado = df_filtrado[df_filtrado["es_top_10"] == True]

if solo_grammy:
    df_filtrado = df_filtrado[df_filtrado["nominado_grammy"] == True]

# ---------------------------------------------------------
# Tarjetas de Resumen (KPIs)
# ---------------------------------------------------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric("Total de Registros", len(df_filtrado))
with kpi2:
    st.metric("Prom. Oyentes Mensuales", f"{df_filtrado['oyentes_mensuales_m'].mean():.2f} M" if not df_filtrado.empty else "N/A")
with kpi3:
    st.metric("Reproducciones Totales", f"{df_filtrado['reproducciones_mexico_m'].sum():.1f} M" if not df_filtrado.empty else "N/A")
with kpi4:
    st.metric("Índice Bailable Promedio", f"{df_filtrado['indice_bailable'].mean():.1f} pts" if not df_filtrado.empty else "N/A")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. Checkbox para vista previa del DataFrame
# ---------------------------------------------------------
ver_datos = st.checkbox("🔍 Mostrar vista previa de los datos filtrados (primeras 10 filas)")

if ver_datos:
    st.markdown("#### 📋 Vista Previa de los Datos")
    st.dataframe(df_filtrado.head(10), use_container_width=True)

st.divider()

# ---------------------------------------------------------
# 5. Gráficos Interactivos con Plotly Express
# ---------------------------------------------------------
st.markdown("### 📊 Análisis Gráfico Interactivo")

if df_filtrado.empty:
    st.warning("⚠️ No hay datos disponibles para los filtros seleccionados. Intenta ajustar la búsqueda.")
else:
    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # Gráfico 1: Gráfico de Barras (Top Artistas por Reproducciones)
    # -----------------------------------------------------
    with col1:
        st.markdown("##### 🎤 Top 10 Artistas por Reproducciones en México (Millones)")
        
        top_artistas = (
            df_filtrado.groupby("artista")["reproducciones_mexico_m"]
            .sum()
            .reset_index()
            .sort_values(by="reproducciones_mexico_m", ascending=True)
            .tail(10)
        )

        fig_barras = px.bar(
            top_artistas,
            x="reproducciones_mexico_m",
            y="artista",
            orientation="h",
            color="reproducciones_mexico_m",
            color_continuous_scale="Viridis",
            labels={"reproducciones_mexico_m": "Reproducciones (M)", "artista": "Artista"},
            template="plotly_dark"
        )
        
        fig_barras.update_layout(
            margin=dict(l=20, r=20, t=30, b=20),
            coloraxis_showscale=False,
            height=400
        )
        
        st.plotly_chart(fig_barras, use_container_width=True)

    # -----------------------------------------------------
    # Gráfico 2: Donut Chart (Distribución de Géneros)
    # -----------------------------------------------------
    with col2:
        st.markdown("##### 🎧 Distribución por Género Musical")
        
        fig_pie = px.pie(
            df_filtrado,
            names="genero",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel,
            template="plotly_dark"
        )
        
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        fig_pie.update_layout(
            margin=dict(l=20, r=20, t=30, b=20),
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # -----------------------------------------------------
    # Gráfico 3: Histograma (Distribución del Índice Bailable)
    # -----------------------------------------------------
    st.markdown("##### 💃 Distribución del Índice Bailable (Danceability Index)")
    
    fig_hist = px.histogram(
        df_filtrado,
        x="indice_bailable",
        nbins=20,
        color="es_artista_mexicano",
        color_discrete_map={True: "#1DB954", False: "#FF5733"},
        labels={
            "indice_bailable": "Índice Bailable (0 - 100)",
            "count": "Frecuencia",
            "es_artista_mexicano": "Artista Mexicano"
        },
        barmode="overlay",
        opacity=0.75,
        template="plotly_dark"
    )
    
    fig_hist.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_title="Índice Bailable",
        yaxis_title="Cantidad de Registros",
        height=400
    )
    
    st.plotly_chart(fig_hist, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("💡 *Dashboard interactivo desarrollado con Streamlit y Plotly Express.*")