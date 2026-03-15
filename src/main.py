import extract
import transform
import load

#confirguracion
Config_pg = {'user': 'postgres', 'pass': 'tu_pass', 'host':'localhost', 'port': '5432', 'db': 'Clientes_db'}
Config_my = {'user': 'root', 'pass': 'tu_pass', 'host':'localhost', 'port': '3306', 'db': 'ventas'}

def Ejecutar_etl():
    #extraccion
    clientes = extract.Extraer_Clientes_pg(Config_pg)
    ventas = extract.Extraer_Ventas_pg(Config_my)

    if clientes is not None and ventas is not None:
        #tranformacion
        df_final, df_gastado = transform.Transformar_Datos(clientes, ventas)

        #carga
        load.cargar_datos(df_final, "resultado_etl_final.csv")
        load.cargar_datos(df_gastado. "metricas_clientes.csv")
if __name__ == "__main__":
    ejecutar_etl()
