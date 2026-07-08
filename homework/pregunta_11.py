"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
def pregunta_11():
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    return df.groupby("c0")["c4"].apply(
        lambda x: ",".join(sorted(x))
    ).reset_index()