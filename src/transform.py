import pandas as pd

def Transformar_Datos (df_Clientes, df_Ventas):
    #eliminacion de duplicado
    df_Clientes =df_Clientes.drop_duplicates()
    df_Ventas = df_Ventas.drop_duplicates()
    #imputamos valores para no perder registros de venta
    df_Clientes['nombre'] = df_Clientes['nombre'].fillna('Sin nombre')
    df_Clientes['ciudad'] = df_Clientes['ciudad'].fillna('Desconocida')
    #convercacion de tipos
    df_Ventas['fecha'] = pd.to_datetime(df_Ventas['fecha'])
    #union usando la id de clientes como llave
    df_Unificado = pd.merge(df_Ventas, df_Clientes, left_on='id_clientes', right_on='id', how='inner')
    #agregacion total_gastado por cliente y conteo por la ciudadd
    Total_Gastado = df_Unificado.groupbt(['id_cliente', 'nombre'])['monto'].sum().reset_index()
    Total_Gastado.rename(columns={'monto': 'Total_Gastado'}, inplace=True)
    
    Conteo_Ciudad =df_Unificado.groupby('ciudad')['id_clientes'].count().reset_index_()
    Conteo_Ciudad.rename(columns={'id_clientes': 'Conteo_Transaccion'}, inplace=True)

    return df_Unificado, Total_Gastado