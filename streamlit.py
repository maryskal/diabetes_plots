import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic


def histogram():
    plt.rcParams.update({'font.size': 10})
    bmi, hb, gluc= False, False, False
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button('BMI'):
            bmi = True
            hb = False
            gluc: False
    with col2:
        if st.button("HbA1c level"):
            bmi = False
            hb = True
            gluc = False
    with col3:
        if st.button('Glucose levels'):
            bmi = False
            hb = False
            gluc = True

    
    if bmi:
        df_ = df[(df.bmi > 15) & (df.bmi < 51)]
        fig, ax = plt.subplots(1, 2, figsize=(15,10))
        sns.histplot(data=df_[df_.diabetes == 1], x="bmi",bins=14, stat='probability', color="red", ax=ax[0])  # distplot is deprecate and replaced by histplot
        ax[0].set_xlim(15,50)
        ax[0].set_xticks([18,25,30,35,40,45])
        ax[0].set_ylim(0,0.4)
        ax[0].set_title("BMI probability in patients with Diabetes (N = 8500)")
        sns.histplot(data=df_[df_.diabetes == 0], x="bmi", color="skyblue", bins=14, stat='probability', ax=ax[1])  # distplot is deprecate and replaced by histplot
        ax[1].set_ylim(0,0.4)
        ax[1].set_xlim(15,50)
        ax[1].set_xticks([18,25,30,35,40,45])
        ax[1].set_title("BMI probability in patients without Diabetes (N = 89552)")
        st.pyplot(fig)
    if hb: 
        fig, ax = plt.subplots(1, 2, figsize=(15,10))
        df_ = df
        sns.histplot(data=df_[df_.diabetes == 1], x="HbA1c_level",binwidth = 1,binrange= [3,9], stat='probability', color="red", ax=ax[0])  # distplot is deprecate and replaced by histplot
        ax[0].set_ylim(0,0.5)
        ax[0].set_xlim(3,9)
        ax[0].set_xticks(range(3,9))
        ax[0].set_title("HbA1c level probability in patients with Diabetes (N = 8500)")
        sns.histplot(data=df_[df_.diabetes == 0], x="HbA1c_level", color="skyblue", binwidth = 1,binrange= [3,9], stat='probability', ax=ax[1])  # distplot is deprecate and replaced by histplot
        ax[1].set_ylim(0,0.5)
        ax[1].set_xlim(3,9)
        ax[1].set_xticks(range(3,9))
        ax[1].set_title("HbA1c level probability in patients without Diabetes (N = 89552)")
        st.pyplot(fig)
    if gluc: 
        fig, ax = plt.subplots(1, 2, figsize=(15,10))
        df_ = df
        sns.histplot(data=df_[df_.diabetes == 1], x="blood_glucose_level", binwidth = 40, binrange= [80,300], stat='probability', color="red", ax=ax[0])  # distplot is deprecate and replaced by histplot
        ax[0].set_ylim(0,0.6)
        ax[0].set_xlim(80,300)
        ax[0].set_xticks(range(80,300,20))
        ax[0].set_title("Blood glucose level probability in patients with Diabetes (N = 8500)")
        sns.histplot(data=df_[df_.diabetes == 0], x="blood_glucose_level", color="skyblue", binwidth = 40,binrange= [80,300], stat='probability', ax=ax[1])  # distplot is deprecate and replaced by histplot
        ax[1].set_ylim(0,0.6)
        ax[1].set_xlim(80,300)
        ax[1].set_xticks(range(80,300,20))
        ax[1].set_title("Blood glucose level probability in patients without Diabetes (N = 89552)")
        st.pyplot(fig)
    

def mosaic_plot():
    plt.rcParams.update({'font.size': 25})
    df_ = df
    df_.diabetes[df_.diabetes == 1] = "DM"
    df_.diabetes[df_.diabetes == 0] = "No DM"
    smoking, gender = False, False
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button('Smoking habits'):
            smoking = True
            gender = False
    with col2:
        if st.button("Gender"):
            smoking = False
            gender = True

    if smoking:
        fig, ax = plt.subplots(figsize=(30,30))
        props = lambda key: {'color': 'r' if 'DM' in key else 'skyblue'}
        mosaic(df_[df.smoking_history != "No Info"],['smoking_history','diabetes'],  gap=0.01, title='Diabetes proportion among smoking habits',
            properties=props, ax = ax)
        st.pyplot(fig)
    if gender:
        fig, ax = plt.subplots(figsize=(30,30))
        props = lambda key: {'color': 'r' if 'DM' in key else 'skyblue'}
        mosaic(df_[df_.gender != "Other"],['gender','diabetes'],  gap=0.01, title='Diabetes proportion among smoking habits',
            properties=props, ax = ax)
        st.pyplot(fig)       

if __name__ == "__main__":
    df = pd.read_csv("diabetes_prediction_dataset.csv")
    st.title("DIFERENCES BETWEEN DIABETIC AND NON-DIABETIC PATIENTS")
    if st.sidebar.checkbox("Histogram"):
        histogram()
    if st.sidebar.checkbox("Mosaic plot"):
        mosaic_plot()
    

