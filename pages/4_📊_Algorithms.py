import streamlit as st
from PIL import Image

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')

st.set_page_config(page_title = "Algorithms", page_icon = image)
st.markdown(hide_menu, unsafe_allow_html=True)
st.sidebar.image(image , use_column_width=True, output_format='auto')

st.sidebar.markdown("---")

st.sidebar.markdown(" <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2024 | Hate Speech Detection</h1>", unsafe_allow_html=True)

st.title("Algorithms📊")
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

all_Datasets = ["Select a Dataset","Cyber Bullying Tweets"]
data_choice = st.selectbox("Dataset", all_Datasets)
all_Vectorizers = ["Select a Vectorizer", "TF-IDF", "CountVectorizer"]
vect_choice = st.selectbox("Vectorizer", all_Vectorizers)
all_ML_models = ["Select a Machine Learning Algorithm", "Naive Bayes", "Support Vector Machine", "BERT"]
model_choice = st.selectbox("Machine Learning Algorithm", all_ML_models)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

if data_choice == "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Dataset_**]")
elif data_choice != "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Vectorizer_**]")
elif data_choice != "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Machine Learning Algorithm_**]")
elif data_choice == "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Dataset_** and **_Vectorizer_**]")
elif data_choice == "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Dataset_** and **_Machine Learning Algorithm_**]")
elif data_choice != "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Vectorizer_** and **_Machine Learning Algorithm_**]")
else:
    if data_choice == "Cyber Bullying Tweets":
    # if token_choice == "Tokenizing":
        if vect_choice == "TF-IDF":
            if model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_76.21%_**]")
            
        elif vect_choice == "CountVectorizer":
            if  model_choice == "Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_77.16%_**]")

        if vect_choice == "TF-IDF":
            if model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_87.35%_**]")
            
        elif vect_choice == "CountVectorizer":
            if  model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_90.28%_**]")

        if vect_choice == "TF-IDF":
            if  model_choice == "BERT":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_89.73%_**]")
                
        elif vect_choice == "CountVectorizer":
            if  model_choice == "BERT":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_88.35%_**]")
            
