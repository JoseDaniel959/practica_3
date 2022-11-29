import streamlit  as st
from PIL import Image
import pandas as pd
import numpy as np
st.title('\U0001f3b6 ONTOLIFY')
st.subheader('', anchor=None)

df = pd.read_csv('df_normalizado.csv',sep = ",", encoding='utf-8')
st.markdown('Te presentamos esta página la cual es un sistema de recomendación de canciones. Para poder darte una recomendación satisfactoria te solicitaremos que nos indiques cuántas veces has escuchado las siguientes canciones. En caso dado de que no la hayas escuchado digita 0.')
image = Image.open('musica.png')
imag1 = Image.open('calidad.png')

def diff_euclidiana(l):
    score = []
    for i in range(0,100):
        fila_i = np.array(seleccion.iloc[i,:])
        diff = np.linalg.norm(np.array(l)-fila_i)
        score.append(diff)
    return score

seleccion = df[['Let It Be','Sweet Home Alabama','Mas que nada','Hallelujah','Thriller','Gimme! Gimme! Gimme! (A Man After Midnight)','Electric City','Side by Side','Take Five','Over the Rainbow','Part II','What Up Gangsta']]

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

if st.button('Visualizar'):
    calificacion_usuario = [cancion1,cancion2,cancion3,cancion4,cancion5,cancion6,cancion7,cancion8,cancion9,cancion10,cancion11,cancion12]

    df['score'] = diff_euclidiana(calificacion_usuario)
 
    new_df = df.sort_values(by=['score'])

    print(new_df.iloc[:,1:1878].head(2).idxmax(axis=1).reset_index(drop=True)[1])
  
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