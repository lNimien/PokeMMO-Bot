import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Archivo renombrado de '{old_name}' a '{new_name}'")
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Error al renombrar el archivo: {e}")

def main():
    rename_file('PokemonMMO.exe', 'PokemonMMO_bot.exe')


if __name__ == "__main__":
    main()
