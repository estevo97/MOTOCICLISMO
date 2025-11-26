import pandas as pd



tabla1 = pd.read_csv('tablas/tabla1.csv')
tabla1 = tabla1.rename(columns={tabla1.columns[0]: "Parámetro"})

tabla2 = pd.read_csv('tablas/cuantiles.csv')
tabla2 = tabla2.drop(tabla2.columns[0], axis=1)

tabla3 = pd.read_csv('tablas/top3.csv')
tabla3 = tabla3.drop(tabla3.columns[0], axis=1)

tabla4 = pd.read_csv('tablas/last3.csv')
tabla4 = tabla4.drop(tabla4.columns[0], axis=1)



tabla5 = pd.read_csv('tablas/paises_all.csv')
tabla5 = tabla5.drop(tabla5.columns[0], axis=1)

tabla6 = pd.read_csv('tablas/paises_500GP.csv')
tabla6 = tabla6.drop(tabla6.columns[0], axis=1)

tabla7 = pd.read_csv('tablas/paises_antes.csv')
tabla7 = tabla7.drop(tabla7.columns[0], axis=1)

tabla8 = pd.read_csv('tablas/paises_antes_500.csv')
tabla8 = tabla8.drop(tabla8.columns[0], axis=1)