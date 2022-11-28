import streamlit  as st
from PIL import Image
st.title('\U0001f3b6 ONTOLIFY')
st.subheader('', anchor=None)


st.markdown('Te presentamos esta página en la cual es un sistema de recomendación de canciones. Para poder darte una recomendación satisfactoria te solicitaremos que nos indiques cuántas veces has escuchado las siguientes canciones. En caso dado de que no la hayas escuchado digita 0.')
image = Image.open('musica.png')
imag1 = Image.open('calidad.png')

col1, col2 = st.columns(2)

with col1:
    st.markdown('## Sobre la página')
    st.markdown('Te presentamos esta página en la cual es un sistema de recomendación de canciones. Para poder darte una recomendación satisfactoria te solicitaremos que nos indiques cuántas veces has escuchado las siguientes canciones. En caso dado de que no la hayas escuchado digita 0. ')

with col2:
   st.image(image)



st.markdown('## \u2705 Calificación de canciones')
cancion1 = st.number_input('Escribe por favor tu puntaje SAT1')
cancion2 = st.number_input('Escribe por favor tu puntaje SAT2')
cancion3 = st.number_input('Escribe por favor tu puntaje SAT3')
cancion4 = st.number_input('Escribe por favor tu puntaje SAT4')
cancion5 = st.number_input('Escribe por favor tu puntaje SAT5')

if st.button('Visualizar'):
    st.write('## \U0001f4bd Canciones que deberías escuchar')
    st.write('Abajo se listan las canciones que deberias escuchar')