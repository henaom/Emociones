from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

st.title('Análisis de Sentimiento')
image = Image.open('Colores-y-emociones-1.jpg')
st.image(image)
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
            st.write( 'Entras un gran día.')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
            st.write(' Tratar de superarlos con toda la paciencia del mundo.😀')
        else:
            st.write( 'Es un sentimiento Neutral 😐')
            st.write('Todo en la vida pasa 😋')
