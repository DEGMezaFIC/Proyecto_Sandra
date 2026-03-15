import pandas as pd
from sqlalchemy import Create_Engine

def Extraer_Clientes_pg (Config_pg):
    try:
        Engine = Create_Engine(f"postgresql://{Config_pg['user']}:{Config_pg['pass']}@{Config_pg['host']}:{Config_pg['port']}/{Config_pg['db']}")
        Query = "SELECT id, nombre, ciudad FROM Clientes"
        df_Clientes = pd.read_sql (Query, Engine)
        return df_Clientes
        except Exception as e:
            print(f"Error al extraer de PostgreSQL: {e}")
            return None

def Extraer_Ventas_Mysql(Config_my):
    try:
        Engine = Create_engine(f"mysql+pymysql://{Config_my['user']}:{Config_my['pass']}@{Config_my['host']}:{Config_my['port']}/{Config_my['db']}")
        Query = "SELECT id_cliente, monto, fecha FROM Ventas"
        df_Ventas = pd.read_sql (Query, Engine)
        return df_Ventas
        except Exception as e:
        print(f"Error al extraer de MySQL: {e}")
        return None
