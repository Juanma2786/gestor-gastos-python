import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Archivo donde se guardan los gastos
ARCHIVO = "gastos.csv"

# Inicializar CSV si no existe
def inicializar_archivo():
    try:
        pd.read_csv(ARCHIVO)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Fecha", "Categoría", "Descripción", "Monto"])
        df.to_csv(ARCHIVO, index=False)

# Agregar un gasto
def agregar_gasto(fecha, categoria, descripcion, monto):
    df = pd.read_csv(ARCHIVO)
    nuevo = {"Fecha": fecha, "Categoría": categoria, "Descripción": descripcion, "Monto": monto}
    df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    df.to_csv(ARCHIVO, index=False)
    print("✅ Gasto agregado con éxito.")

# Mostrar resumen
def resumen():
    df = pd.read_csv(ARCHIVO)
    print("\n📊 Resumen de gastos:")
    print(df.groupby("Categoría")["Monto"].sum())
    print(f"\n💰 Gasto total: {df['Monto'].sum()}")

# Graficar gastos por categoría
def graficar():
    df = pd.read_csv(ARCHIVO)
    df.groupby("Categoría")["Monto"].sum().plot(kind="bar")
    plt.title("Gastos por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Monto")
    plt.show()

# Menú principal
def menu():
    inicializar_archivo()
    while True:
        print("\n--- Gestor de Gastos ---")
        print("1. Agregar gasto")
        print("2. Ver resumen")
        print("3. Graficar gastos")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            fecha = datetime.today().strftime("%Y-%m-%d")
            categoria = input("Categoría: ")
            descripcion = input("Descripción: ")
            monto = float(input("Monto: "))
            agregar_gasto(fecha, categoria, descripcion, monto)
        elif opcion == "2":
            resumen()
        elif opcion == "3":
            graficar()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Ejecutar programa
if __name__ == "__main__":
    menu()