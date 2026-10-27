# 🔬 Laboratorio SQA - TechBank SAC: Análisis Estadístico y Aseguramiento de Calidad

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/milith0kun/laboratorio-sqa-UNSAAC/blob/main/Pareto_ACS.ipynb)
[![GitHub Issues](https://img.shields.io/github/issues/milith0kun/laboratorio-sqa-UNSAAC)](https://github.com/milith0kun/laboratorio-sqa-UNSAAC/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Quality Standard: ISO/IEC 25010](https://img.shields.io/badge/Standard-ISO%2FIEC%2025010-emerald.svg)](#)

Repositorio oficial del equipo **ACS-UNSAAC (Team 04)** para el desarrollo de la **Guía de Práctica 03: Aseguramiento de la Calidad de Software (SQA)**.  
**Caso de Estudio:** Diagnóstico de calidad, confiabilidad, disponibilidad y plan DMAMC (Seis Sigma) para la versión Beta de la plataforma bancaria transaccional de **TechBank SAC**.

---

## 🏛️ Información Institucional y Equipo de Trabajo

- **Universidad:** Universidad Nacional de San Antonio Abad del Cusco (UNSAAC)
- **Facultad:** Facultad de Ingeniería Eléctrica, Electrónica, Informática y Mecánica
- **Escuela Profesional:** Ingeniería Informática y de Sistemas
- **Curso:** Ingeniería de Software II (Semestre 2026-II)
- **Docente:** Msc. Ronald Melgarejo Ramos
- **Equipo:** Grupo 04 - SQA / ACS

### 👥 Integrantes
1. **Condori Quispe, Daniel** (215383) — *QA Lead & Modelado Estadístico*
2. **Kuroda Cabrera, Victor Alejandro** (200336) — *Ingeniero de Automatización & Scripts*
3. **Mendoza Ccolqque, Rony Rolando** (211363) — *Especialista SQA & Métricas ISO 25010*
4. **Nahuamel Huayhua, Cristian** (215389) — *Arquitecto de Confiabilidad & DevOps*
5. **Palomino Cahuana, Gabriel** (211367) — *Auditor de Calidad & Plan DMAMC*

---

## 🎯 Objetivos del Proyecto

1. **Clasificación ISO/IEC 25010 & Taxonomía de Defectos:** Mapeo formal de 200 incidencias en categorías de error de software (EEI, MCC, ERD, VEP, EDL, ICI, PLT).
2. **Análisis de Pareto (Regla 80/20):** Construcción automatizada de diagrama de Pareto con Pandas y Matplotlib para aislar las causas vitales generadoras de fallas.
3. **Métricas de Confiabilidad y Disponibilidad Operacional:**
   - **TMPF (MTBF):** Tiempo Medio Entre Fallas
   - **TMPR (MTTR):** Tiempo Medio Para Reparación
   - **TMEF (MTTF):** Tiempo Medio Hasta la Falla
   - **Disponibilidad ($A$):** $A = \frac{\text{TMPF}}{\text{TMPF} + \text{TMPR}} \times 100\%$ frente al SLA Financiero ($99.95\%$).
4. **Programa de Mejora Continua Seis Sigma (DMAMC):** Matriz operativa de 5 fases (Definir, Medir, Analizar, Mejorar, Controlar) con metas DPMO y nivel Sigma meta ($4.5\sigma$).

---

## 📊 Resumen Ejecutivo de Métricas

| Métrica | Valor Calculado | Estándar / SLA Financiero | Diagnóstico Operativo |
| :--- | :---: | :---: | :--- |
| **Horas Operación Total ($T$)** | $9,000\text{ h}$ | Periodo de observación | 20 fallas críticas en producción |
| **TMPF (MTBF)** | **$450.00\text{ h}$** | $\ge 2,000\text{ h}$ | Frecuencia de falla inaceptable |
| **TMPR (MTTR)** | **$6.00\text{ h}$** | $\le 0.50\text{ h}$ (30 min) | Resolución 12x más lenta que SLA |
| **TMEF (MTTF)** | **$450.00\text{ h}$** | $\ge 2,000\text{ h}$ | Confiabilidad operativa degradada |
| **Disponibilidad Operativa ($A$)** | **$98.6750\%$** | **$99.9500\%$** (3 Nueves y medio) | ⚠️ **INCUMPLE SLA** ($\Delta = -1.2750\%$) |
| **Downtime Mensual Proyectado** | **$9.84\text{ h/mes}$** | Max. $0.365\text{ h/mes}$ (22 min) | **26.5 veces superior** al límite |
| **Causas Vitales Pareto** | **EEI + Otros + MCC + ERD** | Regla 80/20 | Representan el **$72.7\%$** acumulado |

---

## 📂 Estructura del Repositorio

```text
laboratorio-sqa-UNSAAC/
├── data/
│   └── incidencias_software.csv   # Dataset de 10 incidencias base de prueba
├── notebooks/
│   └── Pareto_ACS.ipynb           # Notebook interactivo para Google Colab
├── scripts/
│   └── generate_pareto.py         # Script Python standalone para generación de gráficos
├── incidencias_software.csv       # Dataset en raíz para carga directa en Colab
├── Pareto_ACS.ipynb               # Notebook interactivo en raíz (Open In Colab)
└── README.md                      # Documentación ejecutiva del proyecto
```

---

## 🚀 Cómo Ejecutar en Google Colab

Puedes ejecutar el análisis completo de manera inmediata haciendo clic en la siguiente insignia:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/milith0kun/laboratorio-sqa-UNSAAC/blob/main/Pareto_ACS.ipynb)

O bien descargar y ejecutar localmente con Jupyter Lab / Notebook:
```bash
git clone https://github.com/milith0kun/laboratorio-sqa-UNSAAC.git
cd laboratorio-sqa-UNSAAC
pip install pandas matplotlib tabulate
jupyter notebook Pareto_ACS.ipynb
```

---

## 🎫 Gestión de Incidencias en GitHub Issues

El repositorio cuenta con la configuración de etiquetas y registro de incidencias formal:
- **Issue #1:** `EEI - Especificación Errónea en Módulo de Transferencias`
- **Etiquetas:** `bug`, `severity:high`
- **Trazabilidad:** [Ver Incidencias en GitHub Issues](https://github.com/milith0kun/laboratorio-sqa-UNSAAC/issues)

---
*UNSAAC - Escuela Profesional de Ingeniería Informática y de Sistemas - 2026*
