import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import plotly.express as px
matplotlib.use("Agg")

# Load data
@st.cache
def load_data(data):
    df=pd.read_csv(data)
    return df

def run_eda_app():
    st.title("Exploratory Data Analysis")
    df=load_data("./data/diabetes_data_upload.csv")
    df_encoded=load_data("./data/diabetes_data_upload_clean.csv") 
    freq_df=load_data("./data/freqdist_of_age_data.csv")
    
    submenu=st.sidebar.selectbox("Submenu",["Descriptive","Plots"])
    if submenu=="Descriptive":
        st.subheader("Descriptive Data")
        st.dataframe(df)
        with st.expander("Data Types"):
            st.dataframe(df.dtypes.astype(str))
        with st.expander("Descriptive Summary"):
            st.dataframe(df_encoded.describe().astype(str))
        with st.expander("Class Distribution"):
            st.dataframe(df["class"].value_counts().astype(str))
        with st.expander("Gender Distribtion"):
            st.dataframe(df["Gender"].value_counts().astype(str))
        pass


    elif submenu=="Plots":
        st.subheader("Plots")
        # Layout
        col1,col2=st.columns([2,1])
        with col1:
            with st.expander("Dist Plot of Gender"):
                # fig=plt.figure()
                # sns.countplot(df["Gender"])
                # st.pyplot(fig)
                #pass
                gen_df=df["Gender"].value_counts().to_frame()
                
                gen_df=gen_df.reset_index()
                gen_df.columns=["Gender Type","Counts"]
                #st.dataframe(gen_df)

                p1=px.pie(gen_df,names="Gender Type",values="Counts")
                st.plotly_chart(p1,use_container_width=True)
                
            with st.expander("Dist Plot for Class"):
                fig=plt.figure()
                sns.countplot(df["class"])
                st.pyplot(fig)
                pass
            # with st.expander(""):
                
            #     pass
            
        with col2:
            with st.expander("Gender Distribution"):
                st.write(df["Gender"].value_counts().to_frame())
            with st.expander("Class Distribution"):
                st.write(df["class"].value_counts().to_frame())
                pass
        with st.expander("Frequency Distribtion of Age"):
                #st.dataframe(freq_df)
                p2=px.bar(freq_df,x="Age",y="count")
                st.plotly_chart(p2,use_container_width=True)
                pass    
        
        # Outlier Detection
        with st.expander("Outlier Detection Plot"):
            # fig=plt.figure(figsize=(15,10))
            # sns.boxplot(df["Age"])
            # st.pyplot(fig)
            p3=px.box(df,x="Age",color="Gender")
            st.plotly_chart(p3,use_container_width=True)

        with st.expander("Correlation Plot"):
            corr_matrix=df_encoded.corr()
            
            p4=px.imshow(corr_matrix)
            st.plotly_chart(p4,use_container_width=True)
        pass    
        pass


