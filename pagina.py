import streamlit  as st
from PIL import Image
import pandas as pd
import numpy as np
st.title('\U0001f3b6 ONTOLIFY')
st.subheader('', anchor=None)

st.markdown('Te presentamos esta página la cual es un sistema de recomendación de canciones. Para poder darte una recomendación satisfactoria te solicitaremos que nos indiques cuántas veces has escuchado las siguientes canciones. En caso dado de que no la hayas escuchado digita 0.')
image = Image.open('musica.png')
imag1 = Image.open('calidad.png')

df = pd.read_csv('df_calificaciones.csv',sep = ",", encoding='utf-8')
def diff_euclidiana(normalizado):
    score = []
    for i in range(0,100):
        fila_i = np.array(normalizado.iloc[i,:])
        diff = np.linalg.norm(np.array(normalizado.iloc[-1])-fila_i)
        score.append(diff)
    return score

def minmax_norm(df_input):
    return (df_input - df_input.min()) / ( df_input.max() - df_input.min())

#seleccion = df[['Let It Be','Sweet Home Alabama','Mas que nada','Hallelujah','Thriller','Gimme! Gimme! Gimme! (A Man After Midnight)','Electric City','Side by Side','Take Five','Over the Rainbow','Part II','What Up Gangsta']]

#st.dataframe(df[['Let It Be','Sweet Home Alabama','Mas que nada','Hallelujah','Thriller','Gimme! Gimme! Gimme! (A Man After Midnight)','Electric City','Side by Side','Take Five','Over the Rainbow','Part II','What Up Gangsta']])
col1, col2 = st.columns(2)

with col1:
    st.markdown('## Sobre la página')
    st.markdown('Te presentamos esta página en la cual es un sistema de recomendación de canciones. Para poder darte una recomendación satisfactoria te solicitaremos que nos indiques cuántas veces has escuchado las siguientes canciones. En caso dado de que no la hayas escuchado digita 0. ')

with col2:
   st.image(image)



st.markdown('## \u2705 Calificación de canciones')
st.markdown('En el siguiente formulario califique las siguientes canciones de cada género. Después ')
st.markdown('### Canciones de Rock')
cancion1 = st.number_input('¿Cuántas veces ha escuchado Let It Be?')
cancion2 = st.number_input('¿Cuántas veces ha escuchado Sweet Home Alabama?')
st.markdown('### Canciones de Pop')
cancion3 = st.number_input('¿Cuántas veces ha escuchado Mas que nada?')
cancion4 = st.number_input('¿Cuántas veces ha escuchado Hallelujah?')
st.markdown('### Canciones de Disco')
cancion5 = st.number_input('¿Cuántas veces ha escuchado Thriller?')
cancion6 = st.number_input('¿Cuántas veces ha escuchado Gimme! Gimme! Gimme! (A Man After Midnight)?')
st.markdown('### Canciones de Electro')
cancion7 = st.number_input('¿Cuántas veces ha escuchado Electric City?')
cancion8 = st.number_input('¿Cuántas veces ha escuchado Side by Side?')
st.markdown('### Canciones de Jazz')
cancion9 = st.number_input('¿Cuántas veces ha escuchado Take Five?')
cancion10 = st.number_input('¿Cuántas veces ha escuchado Over the Rainbow?')
st.markdown('### Canciones de Rap')
cancion11 = st.number_input('¿Cuántas veces ha escuchado Part II?')
cancion12 = st.number_input('¿Cuántas veces ha escuchado What Up Gangsta?')

#st.dataframe(df)
if st.button('Visualizar'):
    df = pd.read_csv('df_calificaciones.csv',sep = ",", encoding='utf-8')
    calificacion_usuario = [cancion1,cancion2,cancion3,cancion4,cancion5,cancion6,cancion7,cancion8,cancion9,cancion10,cancion11,cancion12]

    #Se realiza la normalización de los datos 
    
    df_normalizado = minmax_norm(df)
    #Se selecciona las columnas que calififca el usuario
    seleccion = df[['Let It Be','Sweet Home Alabama','Mas que nada','Hallelujah','Thriller','Gimme! Gimme! Gimme! (A Man After Midnight)','Electric City','Side by Side','Take Five','Over the Rainbow','Part II','What Up Gangsta']]
    seleccion.loc[100] = calificacion_usuario
    seleccion_normalizada = minmax_norm(seleccion) #Se normaliza el dataframe seleecionado
    df_normalizado['score'] = diff_euclidiana(seleccion_normalizada) # Se asigna los scores al dataframe normalizado
    new_df = df_normalizado.sort_values(by=['score']).reset_index(drop = True) #Se ordena el dataframe
    

    
    new_df = df_normalizado.sort_values(by=['score'])

    #print(new_df.iloc[:,1:1878].head(2).idxmax(axis=1).reset_index(drop=True)[1])
  
    st.markdown('## \U0001f4bd Canciones que deberías escuchar')
    
    recomendacion_1 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[0]
    recomendacion_2 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[1]
    recomendacion_3 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[2]
    recomendacion_4 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[3]
    recomendacion_5 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[4]
    recomendacion_6 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[5]
    recomendacion_7 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[6]
    recomendacion_8 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[7]
    recomendacion_9 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[8]
    recomendacion_10 = new_df.iloc[:,1:1878].idxmax(axis=1).reset_index(drop=True)[9]

    st.markdown('Si se te es recomendada una canción más de una vez, esto querrá decir que  tienes una afinidad con varias personas en esta canción, lo que podría significar que hay más posibilidad de que te guste.')
    st.markdown('- ' + recomendacion_1)
    st.markdown('- ' + recomendacion_2)
    st.markdown('- ' + recomendacion_3)
    st.markdown('- ' + recomendacion_4)
    st.markdown('- ' + recomendacion_5)
    st.markdown('- ' + recomendacion_6)
    st.markdown('- ' + recomendacion_7)
    st.markdown('- ' + recomendacion_8)
    st.markdown('- ' + recomendacion_9)
    st.markdown('- ' + recomendacion_10)
    st.markdown('# \U0001f480')