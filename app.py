# Librairies
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import os
import os.path
import pickle 

#Titre
st.title("""
# Home Credit Default Risk 📈
""")

# Import Dataset test
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    #Select ID
    liste_id = df['SK_ID_CURR']  
    id = st.select_slider(
      'Choose client ID',
     options=liste_id,  value=liste_id[0])

    st.write('You chose the client ', id)

    #Indexing
    abc = df[df['SK_ID_CURR'] == id].index
    indice = abc[0]

######################################################################

# Prediction
#MODEL_DIR = os.path.join(os.path.dirname('file'), 'model.pickle')
with open('C:/Users/Simplon/Desktop/Travaux python/Scoring client/model.pickle' , 'rb') as handle:
    model = pickle.load(handle)
    #Select gender
    display = ("...", "Male", "Female")
    options = list(range(len(display)))
    value = st.selectbox("Choose gender 👩🏻‍🤝‍🧑🏻", options, format_func=lambda x: display[x])

#AMT_INCOME_TOTAL
if uploaded_file is None:
  total_income = st.number_input('Total income of the client', value=0)
else:
  total_income = st.number_input('Total income of the client', value=(df['AMT_INCOME_TOTAL'].loc[indice]))

st.write('The total income of the client is', total_income)

# When deploying:
#     MODEL_DIR = os.path.join(os.path.dirname('file'), 'model.pickle')
#     with open(MODEL_DIR , 'rb') as handle:
#         model = pickle.load(handle)