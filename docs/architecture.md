# Arquitectura del Proyecto

           Dataset
              |
              v
      Data Processing
              |
              v
    Feature Engineering
              |
              v
      Machine Learning
              |
    +---------+---------+
    |                   |
    v                   v
 SHAP              Predictions
    |                   |
    +---------+---------+
              |
              v
    GenAI Credit Assistant
              |
              v
      Business Dashboard


---

# 4. `data/README.md`

Crear:

```text
data/
└── README.md

# Data

## raw/

Contiene los datos originales sin modificaciones.

## processed/

Contiene datos transformados utilizados para entrenamiento.

## external/

Contiene fuentes externas utilizadas durante el proyecto.

---

Los datasets originales no deben modificarse.