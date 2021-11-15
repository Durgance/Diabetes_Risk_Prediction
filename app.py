import streamlit as st

from eda_app import run_eda_app
from ml_app import run_ml_app

st.set_page_config(page_title="Early Diabetes Risk Prediction",
                        page_icon="🦍")

st.image("./data/diabetes cover.jpg")


def main():
    menu=["Home","EDA","ML Model","About"]
    choice=st.sidebar.selectbox("Menu", menu)
    if choice=="Home":
        st.title("Early Diabetes Risk Prediction App")
        st.write("""
			
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			""")
        pass
    elif choice=="EDA":
        run_eda_app()

        pass
    elif choice=="ML Model":
        run_ml_app()
        pass
    else:
        st.title("About")
        st.subheader("Durgance Gaur")
        st.subheader("NIT Silchar")

        st.markdown("""
        * ### Description :

            * ##### The dataset was collected using direct questions from patients of Sylhet Diabetes Hospital in Sylhet, Bangladesh and approved by doctor

        * ### Metadata :

            * ##### The dataset is a multivariate datasets in CSV format.
            * ##### It has 520 Datapoints and 17 fields or attribtues
            """)

    
if __name__=="__main__":
    main()