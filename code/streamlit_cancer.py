import streamlit as st
import pandas as pd
import pickle as pk
import numpy as np
import PIL as image
#loading in the model to predict on the data
pickle_in=open("svm_linear.pkl","rb")
linear_model=pk.load(pickle_in)
def cancer_prediction(Clump_Thickness,Cell_Size,Cell_Shape,Marginal_Adhesion,Single_Epithelial_Cell_Size,Bare_Nuclei,Normal_Nucleoli,Bland_Chromatin,Mitoses):
    prediction=linear_model.predict([[Clump_Thickness,Cell_Size,Cell_Shape,Marginal_Adhesion,Single_Epithelial_Cell_Size,Bare_Nuclei,Normal_Nucleoli,Bland_Chromatin,Mitoses]])
    print(prediction)
    return prediction
def main():
    html_temp="""
    <div style="background-color:##B1DDF1;">
    <h1 style="color:white;text-align:center;font-size:50px;font-style:italic">Cancer Detection using SVM-linear</h1>
    </div>
    """
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    Clump_Thickness=st.number_input("Clump_Thickness")
    Cell_Size=st.number_input("Cell_Size")
    Cell_Shape=st.number_input("Cell_Shape")
    Marginal_Adhesion=st.number_input("Marginal_Adhesion")
    Single_Epithelial_Cell_Size=st.number_input("Single_Epithelial_Cell_Size")
    Bare_Nuclei=st.number_input("Bare_Nuclei")
    Normal_Nucleoli=st.number_input("Normal_Nucleoli")
    Bland_Chromatin=st.number_input("Bland_Chromatin")
    Mitoses=st.number_input("Mitoses")
    result=""
    if st.button("Predict"):
        result=cancer_prediction(Clump_Thickness,Cell_Size,Cell_Shape,Marginal_Adhesion,Single_Epithelial_Cell_Size,Bare_Nuclei,Normal_Nucleoli,Bland_Chromatin,Mitoses)
        if(result==2):
            result="Benign"
            st.text(result)
        else:
            result="Malignant"
            st.text(result)
if __name__=="__main__":
    main()



