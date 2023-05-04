import streamlit 
import joblib
import numpy as np

model = joblib.load('heart_log.pkl')

app = streamlit.title("Heart Disease Prediction")   

age = streamlit.selectbox("Enter Your Age : ",[num for num in range(28,78)])
sex = streamlit.selectbox("Choose your Gender : ",['Male','Female'])
if sex == "Female":
    sex = 0
else:
    sex = 1

cp = streamlit.select_slider("Chest Pain Scale : ",[num for num in range(0,5)])
restbp = streamlit.select_slider("Resting Blood Pressure : ",[num for num in range(90,201)])
chol = streamlit.select_slider("Cholestrol (mg/dl) : ",[num for num in range(126,564)])
fbs = streamlit.selectbox("Fasting Blood Sugar <= (120 mg/dl) : ",['True','False'])
if fbs == "False":
    fbs = 0
else:
    fbs = 1

fbs = streamlit.selectbox("Resting ECG Result  : ",['Normal','Caution','Alarming'])
if fbs == "Normal":
    fbs = 0
elif fbs == "Caution":
    fbs = 1
else:
    fbs = 2

thalach = streamlit.select_slider("Max. Heart Rate Acheived :",[num for num in range(71,203)])
angina  = streamlit.selectbox("Exercise induced Angina  :",["Yes","No"])
if angina == "Yes":
    angina = 1
else :
    angina = 0

oldpeak  = streamlit.select_slider("ST depression induced by exercise relative to rest  :",[num for num in range(0,7)])

paramlist = [[age,sex,cp,restbp,chol,fbs,thalach,angina,oldpeak,1.39,0.729,2.3135,0]]

pred = model.predict(paramlist)
confidence = model.predict_proba(paramlist)


if streamlit.button("Predict") == True:
    if pred == 1:
        confid = confidence[0][0]
        streamlit.markdown(f"Prone to Heart Disease , Confidence of model : {confid * 100}")
    else:
        confid = confidence[0][1]
        streamlit.markdown(f"Less likely Prone to Heart Disease , Confidence of model : {confid * 100}")
