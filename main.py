from dorks import generar_dork
from scraper import buscar_google, extraer_enlaces

def main():
    print("=== OSINT Dorks Tool ===")

    # Entrada de usuario
    dominio = input("Introduce el dominio (ej: example.com): ").strip().lower()
    tipo_archivo = input("Introduce el tipo de archivo (pdf, doc, etc): ").strip().lower()

    # Validación básica
    if not dominio:
        print("Dominio no válido. Usando 'example.com' por defecto.")
        dominio = "example.com"

    if not tipo_archivo:
        print("Tipo de archivo no válido. Usando 'pdf' por defecto.")
        tipo_archivo = "pdf"

    # Generar dork
    dork = generar_dork(dominio, tipo_archivo)
    print(f"\nDork generado: {dork}")

    try:
        resultado = buscar_google(dork)

        # Manejo de respuesta (puede ser tuple o html)
        if isinstance(resultado, tuple):
            html, estado = resultado

            if estado == "bloqueado":
                print("\nGoogle ha bloqueado la petición.")
                html = None
        else:
            html = resultado

        resultados = []

        if html:
            resultados = extraer_enlaces(html)

        print("\nResultados encontrados:")

        if resultados:
            for r in resultados[:10]:
                print(r)
        else:
            print("No se encontraron resultados reales. Mostrando resultados simulados:\n")

            resultados_simulados = [
                f"https://{dominio}/documento1.{tipo_archivo}",
                f"https://{dominio}/archivo2.{tipo_archivo}",
                f"https://{dominio}/reporte3.{tipo_archivo}"
            ]

            for r in resultados_simulados:
                print(r)

    except Exception as e:
        print(f"\nError durante la ejecución: {e}")

if __name__ == "__main__":
    main()