# ==============================================================================
# Laboratorio 03 SQA: Análisis de Calidad y Diagrama de Pareto
# TechBank SAC - Equipo 04 SQA UNSAAC
# ==============================================================================
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # 1. Carga de incidencias de prueba
    try:
        df_base = pd.read_csv('incidencias_software.csv')
        print("=== DATASET BASE (10 INCIDENCIAS) ===")
        print(df_base)
    except FileNotFoundError:
        print("Archivo incidencias_software.csv no encontrado en directorio actual.")

    # 2. Dataset consolidado del caso TechBank SAC (n=942)
    categorias = ['EEI', 'Otros', 'MCC', 'ERD', 'EDL', 'ICI', 'PLT', 'VEP']
    frecuencias = [205, 193, 156, 130, 85, 68, 55, 50]
    nombres_dict = {
        'EEI': 'Especificaciones Erróneas (EEI)',
        'Otros': 'Otras Incidencias (Otros)',
        'MCC': 'Mala Comunicación (MCC)',
        'ERD': 'Error Repr. Datos (ERD)',
        'EDL': 'Error Diseño Lógico (EDL)',
        'ICI': 'Interfaz Inconsistente (ICI)',
        'PLT': 'Error Traducción Lenguaje (PLT)',
        'VEP': 'Violación Estándares (VEP)'
    }

    df = pd.DataFrame({'codigo': categorias, 'frecuencia': frecuencias})
    df['nombre'] = df['codigo'].map(nombres_dict)
    df = df.sort_values(by='frecuencia', ascending=False).reset_index(drop=True)
    df['porcentaje'] = (df['frecuencia'] / df['frecuencia'].sum()) * 100
    df['acumulado'] = df['porcentaje'].cumsum()

    print("\n=== TABLA DE FRECUENCIAS Y PORCENTAJE ACUMULADO ===")
    print(df[['codigo', 'frecuencia', 'porcentaje', 'acumulado']])

    # 3. Métricas de Confiabilidad y Disponibilidad
    horas_totales = 9000
    num_fallas = 20
    tiempo_reparacion_total = 120

    tmpr = tiempo_reparacion_total / num_fallas  # MTTR
    tmpf = (horas_totales - tiempo_reparacion_total) / num_fallas  # MTBF
    tmef = tmpf  # MTTF
    disponibilidad = (tmpf / (tmpf + tmpr)) * 100
    indisponibilidad = 100 - disponibilidad
    downtime_mes = (indisponibilidad / 100) * 744

    print("\n=== MÉTRICAS DE CONFIABILIDAD Y DISPONIBILIDAD ===")
    print(f"TMPF (MTBF): {tmpf:.2f} h")
    print(f"TMPR (MTTR): {tmpr:.2f} h")
    print(f"TMEF (MTTF): {tmef:.2f} h")
    print(f"Disponibilidad (A): {disponibilidad:.4f}%")
    print(f"Indisponibilidad (U): {indisponibilidad:.4f}% ({downtime_mes:.2f} h/mes)")
    print(f"SLA Bancario Meta: 99.9500% -> Brecha: {disponibilidad - 99.95:.4f}%")

    # 4. Generación Gráfico de Pareto
    fig, ax1 = plt.subplots(figsize=(11, 6), dpi=300)
    bars = ax1.bar(df['codigo'], df['frecuencia'], color='#1e3d59', edgecolor='#17b978', width=0.6, label='Frecuencia')
    ax1.set_xlabel('Categoría de Error (Taxonomía SQA)', fontsize=12, fontweight='bold', labelpad=10)
    ax1.set_ylabel('Frecuencia de Incidencias', color='#1e3d59', fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='#1e3d59')
    ax1.set_ylim(0, max(df['frecuencia']) * 1.18)

    for bar in bars:
        h = bar.get_height()
        ax1.annotate(f'{int(h)}', xy=(bar.get_x() + bar.get_width() / 2, h),
                     xytext=(0, 4), textcoords="offset points", ha='center', va='bottom',
                     fontweight='bold', fontsize=10, color='#1e3d59')

    ax2 = ax1.twinx()
    line = ax2.plot(df['codigo'], df['acumulado'], color='#ff6e40', marker='o', linewidth=2.5, markersize=7, label='% Acumulado')
    ax2.set_ylabel('Porcentaje Acumulado (%)', color='#ff6e40', fontsize=12, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor='#ff6e40')
    ax2.set_ylim(0, 105)

    for i, txt in enumerate(df['acumulado']):
        ax2.annotate(f'{txt:.1f}%', (df['codigo'][i], df['acumulado'][i]),
                     textcoords="offset points", xytext=(0, 9), ha='center',
                     fontweight='bold', fontsize=9, color='#ff6e40')

    ax2.axhline(80, color='#d32f2f', linestyle='--', linewidth=1.6, label='Umbral Pareto 80%')
    ax1.grid(axis='y', linestyle=':', alpha=0.6)
    plt.title('Diagrama de Pareto: Defectos e Incidencias en TechBank SAC (Regla 80/20)', fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig('pareto_techbank.png', dpi=300)
    print("\nGráfico 'pareto_techbank.png' guardado exitosamente.")

if __name__ == '__main__':
    main()
