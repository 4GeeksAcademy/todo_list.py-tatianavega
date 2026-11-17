import csv
import os

# Esta es nuestra pizarra en memoria (la lista vacía)
tareas = []
TODO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'todos.csv')

def add_one_task(title):
    tareas.append(title)
    print(f"✅ ¡Tarea '{title}' agregada con éxito!")
    save_todos()

def print_list():
    if len(tareas) == 0:
        print("📭 Tu lista está vacía. ¡Agrega algo!")
        return
    
    print("\n--- 📝 TUS TAREAS ---")
    for indice, tarea in enumerate(tareas, 1):
        print(f"{indice}. {tarea}")
    print("---------------------\n")

def delete_task(number_to_delete):
    try:
        numero = int(number_to_delete)
        indice_real = numero - 1
        
        if 0 <= indice_real < len(tareas):
            tarea_borrada = tareas.pop(indice_real)
            print(f"🗑️ Tarea '{tarea_borrada}' eliminada correctamente.")
            save_todos()
        else:
            print("❌ Ese número de tarea no existe.")
            
    except ValueError:
        print("❌ Por favor, ingresa un número válido.")

def save_todos():
    with open(TODO_FILE, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        for tarea in tareas:
            writer.writerow([tarea])
    print("💾 Tareas guardadas en 'todos.csv'.")

def load_todos():
    global tareas
    tareas.clear() 
    
    try:
        with open(TODO_FILE, mode='r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                if len(fila) > 0:
                    tareas.append(fila[0])
        print("📂 Tareas cargadas desde 'todos.csv'.")
    except FileNotFoundError:
        print("📂 No se encontró 'todos.csv'. Empezando lista nueva.")

def main():
    load_todos()
    
    while True:
        print("\n=== MENÚ DE TAREAS ===")
        print("1. Agregar nueva tarea")
        print("2. Mostrar todas las tareas")
        print("3. Eliminar una tarea")
        print("4. Guardar y salir")
        
        opcion = input("¿Qué quieres hacer? (1-4): ")
        
        if opcion == '1':
            titulo = input("Escribe la nueva tarea: ")
            add_one_task(titulo)
        elif opcion == '2':
            print_list()
        elif opcion == '3':
            print_list() 
            num = input("Escribe el número de la tarea a eliminar: ")
            delete_task(num)
        elif opcion == '4':
            save_todos()
            print("¡Adiós! Sigue siendo productiva. 👋")
            break 
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()