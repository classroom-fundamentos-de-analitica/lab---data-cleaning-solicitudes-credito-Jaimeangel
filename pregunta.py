"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    df=df.dropna()

    df['sexo'] = df['sexo'].str.lower();
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower();
    df['idea_negocio']=df['idea_negocio'].apply(lambda x: x.lower().replace("_", " ").replace("-", " "))
    df['barrio']=df['barrio'].apply(lambda x: x.lower().replace("_"," ").replace("-"," "))
    df['línea_credito']=df['línea_credito'].apply(lambda x: x.lower().replace("-"," ").replace("_"," "))
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)

    return df
print(clean_data())
