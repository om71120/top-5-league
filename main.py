###import library
from ulits import process_new
import streamlit as st 
import joblib


##load the model
model = joblib.load("model_xgboost")


def top_leagues():

    st.title("Top Football Leagues Scores")
    st.markdown('<hr>',unsafe_allow_html=True)

    ###input

    Country =st.selectbox('Country', options=['Spain','Italy','Germany','England','Brazil','France','USA','Portugal','Netherlands'])
    Club = st.text_input('club')
    Player_Names= st.text_input('player name')
    Matches_Played=st.number_input('Matches_Played',value=1,step=1)
    Substitution = st.number_input('Substitution',value=1,step=1)
    Mins = st.select_slider( 'Mins' , min=264 , max=4177 , step=1)
    Goals = st.select_slider('Goals', min=2, max=37 , step=1 )
    # xG_Per_Avg_Match = 
    #Shots = 
    #OnTarget = 
    ##On_Target_Per_Avg_Match= 
    #Year =

    return None
if __name__ =='_main_':
    ##call function 
    top_leagues()
