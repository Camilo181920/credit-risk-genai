# Credit Risk Analytics & GenAI Assistant

## Informe Ejecutivo

## 1. Contexto

Este proyecto simula una solución analítica para una entidad financiera orientada a mejorar el proceso de evaluación de riesgo crediticio.

---

# 2. Problema de negocio

La entidad financiera requiere identificar clientes con mayor probabilidad de incumplimiento para apoyar decisiones de aprobación de crédito.

---

# 3. Objetivo analítico

Construir un modelo predictivo que:

- estime la probabilidad de default;
- identifique factores de riesgo;
- genere explicaciones interpretables;
- permita recomendaciones mediante IA Generativa.

---

# 4. Datos utilizados

Dataset:

German Credit Data

Características:

- Información demográfica.
- Características del crédito.
- Historial financiero.
- Variable objetivo de incumplimiento.

---

# 5. Análisis exploratorio

## Calidad de datos

Pendiente.

## Principales hallazgos

Pendiente.

---

# 6. Modelamiento

Modelos evaluados:

- Regresión logística.
- Random Forest.
- XGBoost.

Métricas:

- ROC-AUC.
- Precision.
- Recall.
- F1-score.

---

# 7. Explainable AI

Se utilizará SHAP para identificar las variables que más influyen en las predicciones.

---

# 8. IA Generativa

Se desarrollará un asistente capaz de transformar resultados del modelo en recomendaciones entendibles para analistas de crédito.

---

# 9. Impacto esperado

La solución busca reducir el riesgo crediticio y facilitar decisiones basadas en datos.

# Evaluación de negocio

Además de evaluar métricas tradicionales de clasificación, se estimó el impacto de las decisiones del modelo utilizando una matriz de costos simplificada.

Se asignó un mayor costo a los falsos negativos, ya que representan clientes de alto riesgo aprobados incorrectamente.

Posteriormente se optimizó el umbral de decisión para reducir el costo esperado sin depender únicamente del valor por defecto de 0.5.