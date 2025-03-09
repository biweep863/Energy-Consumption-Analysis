import pandas as pd
import matplotlib.pyplot as plt  

def porcentajes(df, año):
    # Filtrar los datos del año seleccionado
    datos_año = df[df["Año"] == año]
    
    if datos_año.empty:
        print(f"No se encontraron datos para el año {año}.")
        return
    
    # Extraer los valores de las fuentes de energía para ese año
    total_energia = datos_año[["Carbon", "Gas Natural", "Nuclear", "Hydro", "Eolica, solar, etc.", "Biocombustiles y desechos", "Petroleo"]].sum(axis=1).values[0]
    
    porcentajes = [
        (datos_año["Carbon"].values[0] / total_energia) * 100,
        (datos_año["Gas Natural"].values[0] / total_energia) * 100,
        (datos_año["Nuclear"].values[0] / total_energia) * 100,
        (datos_año["Hydro"].values[0] / total_energia) * 100,
        (datos_año["Eolica, solar, etc."].values[0] / total_energia) * 100,
        (datos_año["Biocombustiles y desechos"].values[0] / total_energia) * 100,
        (datos_año["Petroleo"].values[0] / total_energia) * 100
    ]
    
    etiquetas = ["Carbón", "Gas Natural", "Nuclear", "Hidro", "Eólica/Solar", "Biocombustibles", "Petróleo"]

    plt.figure(figsize=(8, 8)) 
    plt.pie(porcentajes, labels=etiquetas, autopct='%1.1f%%', startangle=140)
    plt.title(f"Distribución de Energía por Fuente en {año}")
    
    plt.show()

def graficasGeneralMain(df):
    años = df["Año"]
    carbon = df["Carbon"]
    gas_natural = df["Gas Natural"]
    nuclear = df["Nuclear"]
    hidro = df["Hydro"]
    eolica_solar = df["Eolica, solar, etc."]
    biocombustibles = df["Biocombustiles y desechos"]
    petroleo = df["Petroleo"]

    plt.figure(figsize=(10, 6)) 
    plt.plot(años, carbon, marker="o", linestyle="-", label="Carbón", color="brown")
    plt.plot(años, gas_natural, marker="s", linestyle="--", label="Gas Natural", color="green")
    plt.plot(años, nuclear, marker="^", linestyle=":", label="Nuclear", color="blue")
    plt.plot(años, hidro, marker="D", linestyle="-.", label="Hidro", color="cyan")
    plt.plot(años, eolica_solar, marker="*", linestyle="--", label="Eólica/Solar", color="orange")
    plt.plot(años, biocombustibles, marker="p", linestyle=":", label="Biocombustibles", color="purple")
    plt.plot(años, petroleo, marker="x", linestyle="-", label="Petróleo", color="black")

    plt.xlabel("Años")
    plt.ylabel("Terajulios (TJ)")
    plt.title("Consumo de Energía por Fuente a lo largo de los años")
    plt.grid(True) 
    plt.legend()  

    plt.show()

def graficaBarras(df, año):
    datos_año = df[df["Año"] == año]
    
    if datos_año.empty:
        print(f"No se encontraron datos para el año {año}.")
        return
    
    fuentes = ["Carbon", "Gas Natural", "Nuclear", "Hydro", "Eolica, solar, etc.", "Biocombustiles y desechos", "Petroleo"]
    valores = [datos_año[fuente].values[0] for fuente in fuentes]
    
    plt.figure(figsize=(10, 6))
    plt.bar(fuentes, valores, color=['brown', 'green', 'blue', 'cyan', 'orange', 'purple', 'black'])

    plt.xlabel("Fuente de Energía")
    plt.ylabel("Consumo de Energía (TJ)")
    plt.title(f"Consumo Energético por Tipo en {año}")
    
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def reporteAño(df, año):
    datos_año = df[df["Año"] == año]
    
    if datos_año.empty:
        print(f"No se encontraron datos para el año {año}.")
        return
    
    total_consumo = datos_año[["Carbon", "Gas Natural", "Nuclear", "Hydro", "Eolica, solar, etc.", "Biocombustiles y desechos", "Petroleo"]].sum(axis=1).values[0]
    
    maxima_fuente = datos_año[["Carbon", "Gas Natural", "Nuclear", "Hydro", "Eolica, solar, etc.", "Biocombustiles y desechos", "Petroleo"]].idxmax(axis=1).values[0]
    minima_fuente = datos_año[["Carbon", "Gas Natural", "Nuclear", "Hydro", "Eolica, solar, etc.", "Biocombustiles y desechos", "Petroleo"]].idxmin(axis=1).values[0]
    
    maxima_cantidad = datos_año[maxima_fuente].values[0]
    minima_cantidad = datos_año[minima_fuente].values[0]

    if año - 1 in df["Año"].values:
        datos_año_anterior = df[df["Año"] == año - 1]
        total_consumo_anterior = datos_año_anterior[["Carbon", "Gas Natural", "Nuclear", "Hydro", "Eolica, solar, etc.", "Biocombustiles y desechos", "Petroleo"]].sum(axis=1).values[0]
        incremento = ((total_consumo - total_consumo_anterior) / total_consumo_anterior) * 100
    else:
        incremento = None

    # Imprimir el reporte
    print(f"Reporte para el año {año}:")
    print(f"Consumo total de energía: {total_consumo:.2f} TJ")
    print(f"Fuente de energía más consumida: {maxima_fuente} con {maxima_cantidad:.2f} TJ")
    print(f"Fuente de energía menos consumida: {minima_fuente} con {minima_cantidad:.2f} TJ")
    
    if incremento is not None:
        print(f"Porcentaje de incremento respecto al año anterior: {incremento:.2f}%")
    else:
        print("No hay datos del año anterior para calcular el incremento.")

def main(): 
    df = pd.read_csv("./Total energy supply (TES) by source - World.csv")

    print("Para ver reporte de un año: 1, para ver porcentaje de un año: 2, para ver gráficas de un año: 3 y para ver gráfica(1990-2022): 4 :")
    decision = int(input())

    while decision != 1 and decision != 2 and decision != 3 and decision != 4:
        print ("Opción no valida, por favor ingrese alguna de las opciones que tenemos ")
        print("Para ver reporte de un año: 1, para ver porcentaje de un año: 2, para ver gráficas de un año: 3 y para ver gráfica(1990-2022): 4 :")
        decision = int(input())

    if decision == 1:
        print ("¿De qué año le gustaría ver el reporte? (A partir de 1990 a 2022) ")
        año = int(input())
        
        while (año == None) or (año <1990) or (año>2022):
            print ("Opción no valida, por favor ingrese alguna de las opciones que tenemos (1990 - 2022)")
            año = int(input())
        
        print ("Aqui va el reporte del año " + str(año))
        reporteAño(df, año)

    elif decision == 2:
        print ("¿De qué año le gustaría ver el porcentaje de uso? (A partir de 1990 a 2022) ")
        año = int(input())
        
        while (año == None) or (año <1990) or (año>2022):
            print ("Opción no valida, por favor ingrese alguna de las opciones que tenemos (1990 - 2022)")
            año = int(input())
        
        print ("Aqui va el porcentaje del año " + str(año))
        porcentajes(df, año)

    elif decision == 3:
        print ("¿De qué año le gustaría ver la gráfica? (A partir de 1990 a 2022) ")
        año = int(input())
        
        while (año == None) or (año <1990) or (año>2022):
            print ("Opción no valida, por favor ingrese alguna de las opciones que tenemos (1990 - 2022)")
            año = int(input())
        
        print ("Aqui va la gráfica del año " + str(año))
        graficaBarras(df, año)

    elif decision == 4:
        graficasGeneralMain(df)
        
#if para ejecutar la función main
if __name__ == "__main__":
    main()
