# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:43:11 2021

@author: Klase
"""
import pandas as pd
import numpy as np

##Generamos un csv para cada pestaña

pd.options.display.max_columns = None

df = pd.read_excel('EDERJAKIN_LA_Datos_2021.xlsm', sheet_name=None)

for sheet_name in list(df.keys()):
   df[sheet_name].to_csv(sheet_name + 'Sheet.csv')

##Importamos los csvs
   
Usuarios = pd.read_csv('UsuariosSheet.csv')
Tutores_perfil = pd.read_csv('Tutores perfilSheet.csv')
Conocimientos = pd.read_csv('ConocimientosSheet.csv')
Cursos = pd.read_csv('CursosSheet.csv')
Programas = pd.read_csv('ProgramasSheet.csv')
Cursos_en_Programas = pd.read_csv('Cursos en ProgramasSheet.csv')
Itinearios = pd.read_csv('ItineariosSheet.csv')
Notas_Cursos = pd.read_csv('Notas_CursosSheet.csv')
Roles = pd.read_csv('RolesSheet.csv')
Plantas = pd.read_csv('PlantasSheet.csv')
Accesos = pd.read_csv('AccesosSheet.csv')
Acceso_1ero_ultimo = pd.read_csv('Acceso_1ero_ultimoSheet.csv')
Actividades = pd.read_csv('ActividadesSheet.csv')

Actividades.info()
Actividades.shape

##Quitamos la primera columna  de que se ha generado automaticamente 'Unnamed: 0'

Conocimientos = Conocimientos.drop(['Unnamed: 0'], axis=1)

Cursos_en_Programas = Cursos_en_Programas.drop(['Unnamed: 0'], axis=1)

Usuarios = Usuarios.drop(['Unnamed: 0'], axis=1)

Tutores_perfil = Tutores_perfil.drop(['Unnamed: 0'], axis=1)

Cursos = Cursos.drop(['Unnamed: 0'], axis=1)

Programas = Programas.drop(['Unnamed: 0'], axis=1)

Itinearios = Itinearios.drop(['Unnamed: 0'], axis=1)

Notas_Cursos = Notas_Cursos.drop(['Unnamed: 0'], axis=1)

Roles = Roles.drop(['Unnamed: 0'], axis=1)

Plantas = Plantas.drop(['Unnamed: 0'], axis=1)

Accesos = Accesos.drop(['Unnamed: 0'], axis=1)

Acceso_1ero_ultimo = Acceso_1ero_ultimo.drop(['Unnamed: 0'], axis=1)

Actividades = Actividades.drop(['Unnamed: 0'], axis=1)

##Vamos a unir dataframes
#%%
Conocimientos.head()

Cursos_en_Programas.head()

Usuarios.head()

Tutores_perfil.head()

Cursos.head()

Programas.head()

Itinearios.head()

Notas_Cursos.head()

Roles.head()

Plantas.head()

Accesos.head()

Acceso_1ero_ultimo.head()

Actividades


Df_final=pd.merge(Usuarios,Accesos,on="user_id")



#%%







