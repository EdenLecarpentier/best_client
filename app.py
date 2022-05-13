# Librairies
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import os
import os.path
import pickle 

# Header
#Load image
img = Image.open("image.png") 
st.image(img, width=120) 
#Titre
st.write("""
# Home Credit Default Risk 📈
""")

st.markdown("V1")

# Import Dataset test
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.drop('Unnamed: 0', inplace=True, axis=1)
    st.write(df.head())
    #Select ID
    st.selectbox('Choose ID', df)
    #Graphique
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['EXT_SOURCE_1', 'EXT_SOURCE_2','EXT_SOURCE_3'])
    st.line_chart(df)

######################################################################

# Prediction
# MODEL_DIR = os.path.join(os.path.dirname('file'), 'model.pickle')
# with open(MODEL_DIR , 'rb') as handle:
#     model = pickle.load(handle)
    # #Select gender
    # display = ("...", "Male", "Female")
    # options = list(range(len(display)))
    # value = st.selectbox("Choose gender ", options, format_func=lambda x: display[x])
    # #Select family status
    # display = ("...", "Married", "Separated", "Single", "Widow", "Civil Marriage")
    # options = list(range(len(display)))
    # value = st.selectbox("Choose family status ", options, format_func=lambda x: display[x])
    # #Select income
    # display = ("...", "AMT_CREDIT", "AMT_ANNUITY", "AMT_INCOME_TOTAL")
    # options = list(range(len(display)))
    # value = st.selectbox("Choose Income ", options, format_func=lambda x: display[x])


#Load Model
MODEL_DIR = os.path.join(os.path.dirname('file'), 'model.pickle')
with open(MODEL_DIR , 'rb') as handle:
    model = pickle.load(handle)

#Nouvelles colonnes

def prediction(CODE_GENDER, NAME_INCOME_TYPE, AMT, EXT):   
#Predictions   
    AMT = ["AMT_CREDIT", "AMT_ANNUITY", "AMT_INCOME_TOTAL"]
    EXT = ['EXT_SOURCE_1', 'EXT_SOURCE_2','EXT_SOURCE_3']
    prediction = model.predict( 
        [[CODE_GENDER, NAME_INCOME_TYPE, AMT, EXT]]) 
    print(prediction) 
    return prediction 
  
def main():       
    st.title("Prediction ❗") 
    st.markdown("V2")
    #Select choose     
    CODE_GENDER = st.selectbox("Choose genre", ["Male", "Female"]) 
    NAME_INCOME_TYPE = st.selectbox("Choose Income", ["Married", "Separated", "Single", "Widow", "Civil Marriage"]) 
    AMT = st.selectbox("Choose AMT", ["AMT_CREDIT", "AMT_ANNUITY", "AMT_INCOME_TOTAL"]) 
    EXT = st.selectbox("Choose EXT", ['EXT_SOURCE_1', 'EXT_SOURCE_2','EXT_SOURCE_3']) 
    result ='' 
    #Bouton predict
    if st.button("Predict"): 
        result = prediction(CODE_GENDER, NAME_INCOME_TYPE, AMT, EXT) 
    st.success('Rembourser son prêt ? {}'.format(result)) 
     
if __name__=='__main__': 
    main() 



# if uploaded_file:
#     MODEL_DIR = os.path.join(os.path.dirname('file'), 'model.pickle')
#     with open(MODEL_DIR , 'rb') as handle:
#         model = pickle.load(uploaded_file)

#     st.markdown("### Data preview")
#     st.dataframe(df.head())

#     st.markdown("### Select columns for analysis")
#     with st.form(key="my_form"):
#         ab = st.multiselect(
#             "Gender",
#             options=df.columns,
#             help="Select which column refers to your A/B testing labels.",
#         )
#     submit_button = st.form_submit_button(label="Submit")
