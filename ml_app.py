import streamlit as st 

import joblib
import os
import pickle

import numpy as np
attrib_info=""" 
#### Attribute Information:    
    - Age 1.20-65
    - Sex 1. Male, 2.Female
    - Polyuria 1.Yes, 2.No.
    - Polydipsia 1.Yes, 2.No.
    - sudden weight loss 1.Yes, 2.No.
    - weakness 1.Yes, 2.No.
    - Polyphagia 1.Yes, 2.No.
    - Genital thrush 1.Yes, 2.No.
    - visual blurring 1.Yes, 2.No.
    - Itching 1.Yes, 2.No.
    - Irritability 1.Yes, 2.No.
    - delayed healing 1.Yes, 2.No.
    - partial paresis 1.Yes, 2.No.
    - muscle stifness 1.Yes, 2.No.
    - Alopecia 1.Yes, 2.No.
    - Obesity 1.Yes, 2.No.
    - Class 1.Positive, 2.Negative.

"""


label_dict={"Yes":1,"No":0}
gender_map={"Male":1,"Female":0}
target_label_map={"Negative":0,"Positive":1}

def get_fvalue(val):
    for key, value in label_dict.items():
        if val==key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val==key:
            return value


def load_model(filename):
    with open(filename,"rb") as f:
        model=pickle.load(f)
    
    return model


def run_ml_app():
    st.title("Predicting Your Risk of Diabetes ")
    
    #with 
    
    with st.expander("Attribute Info"):
        st.markdown(attrib_info)

    col1,col2=st.columns(2)

    with col1:
        age=st.number_input("Age",10,100)
        gender=st.radio("Gender",["Female","Male"])
        polyuria=st.radio("Polyuria",["No","Yes"])
        polydipsia=st.radio("Polydipsia",["No","Yes"])
        sudden_weight_loss=st.selectbox("Sudden Weight Loss",["No","Yes"])
        weakness=st.radio("weakness",["No","Yes"])
        Polyphagia=st.radio("Polyphagia",["No","Yes"])
        genital_thrust=st.selectbox("Genital Thrust",["No","Yes"])

    with col2:
        visual_blurring=st.radio("Visual Blurring",["No","Yes"])
        itching=st.radio("itching",["No","Yes"])
        irritability=st.radio("irritability",["No","Yes"])
        delayed_healing=st.radio("Delayed Healing",["No","Yes"])
        partial_paresis=st.selectbox("Partial Paresis",["No","Yes"])
        muscle_stiffness=st.radio("Muscle Stiffness",["No","Yes"])
        alopecia=st.radio("Alopecia",["No","Yes"])
        obesity=st.select_slider("obesity",["No","Yes"])
        pass
    
    with st.expander("Your Selected Options are "):
        results={
            "Age":age,
            "Sex" :gender,
            "Polyuria":polyuria ,
            "Polydipsia": polydipsia,
            "sudden weight loss": sudden_weight_loss,
            "weakness": weakness,
            "Polyphagia": Polyphagia,
            "Genital thrush": genital_thrust,
            "visual blurring ":visual_blurring,
            "Itching": itching,
            "Irritability": irritability,
            "delayed healing":delayed_healing ,
            "partial paresis": partial_paresis,
            "muscle stifness":muscle_stiffness,
            "Alopecia":alopecia,
            "Obesity":obesity}
        st.write(results)

        encoded_result=[]
        for i in results.values():
            if type(i)==int:
                encoded_result.append(i)
            elif i in ["Female","Male"]:
                encoded_result.append(get_value(i, gender_map))
            else:
                encoded_result.append(get_fvalue(i))


    with st.expander("Predicting your Risk of Diabetes "):
        model=load_model("./model/RandomForest_diabetes.pkl")
        single_samlpe=np.array(encoded_result).reshape(1,-1)
        #st.write()
        prediction=model.predict(single_samlpe)
        pred_prob=model.predict_proba(single_samlpe)
        #st.write(prediction)
        #st.write(pred_prob)

        if prediction==1:
            st.warning(f"High Risk of Diabetes 💀")
            predict_probability_score={"Negative DM Risk":pred_prob[0][0]*100,
            "Postive DM Risk":pred_prob[0][1]*100}
            st.write(predict_probability_score)
        else:
            st.success(f"You are Healthy 💘")
            predict_probability_score={"Negative DM Risk":pred_prob[0][0]*100,
            "Postive DM Risk":pred_prob[0][1]*100}
            st.write(predict_probability_score)


            