import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("tablero de dibujo")

with st.sidebar:
  st.subheader("propiedades del tablero")

  st.subheader("dimensiones del tablero")
  canvas_width = st.slider("ancho del tablero", 300, 700, 500, 50)
  canvas_height = st.slider("alto del tablero", 200, 600, 300, 50)

  drawing_mode = st.selectbox(
    "herramienta de dibujo",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
  )

  stroke_width = st.slider("selecciona el ancho de línea", 1, 30, 15)
  stroke_color = st.color_picker("color de trazo", "#FFFFFF")
  bg_color = st.color_picker("color de fondo", "#000000")

canvas_result = st_canvas(
  fill_color="rgba(255, 165, 0, 0.3)",
  stroke_width=stroke_width,
  stroke_color=stroke_color,
  background_color=bg_color,
  height=canvas_height,
  width=canvas_width,
  drawing_mode=drawing_mode,
  key=f"canvas_{canvas_width}_{canvas_height}",
)
