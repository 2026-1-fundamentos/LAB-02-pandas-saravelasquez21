"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
def pregunta_12():
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    resultado = df.sort_values(["c0", "c5a"]).groupby("c0").apply(
        lambda x: ",".join(f"{r['c5a']}:{r['c5b']}" for _, r in x.iterrows())
    ).reset_index()
    resultado.columns = ["c0", "c5"]
    return resultado