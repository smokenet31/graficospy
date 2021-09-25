import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


aplicaciondb = pd.read_csv('Aplicaciones.csv')
##aplicacionfiltro = aplicaciondb.loc[(aplicaciondb['Nombre y apellido'] == 'Flavio Rodriguez'),["Nombre y apellido", "Bebida"]]
##print(aplicacionfiltro)
##aplicacionfiltro.to_csv('agustinjugo.csv')

fig = px.bar(aplicaciondb, x="Aplicacion", y="Tiempo", color="Nombre", barmode="group")
fig.show()