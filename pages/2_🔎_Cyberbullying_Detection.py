import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report
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
st.set_page_config(page_title="Datasets", page_icon=image)
st.markdown(hide_menu, unsafe_allow_html=True)
st.sidebar.image(image, use_column_width=True, output_format='auto')
st.sidebar.markdown("---")
st.sidebar.markdown(" <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2024 | Hate Speech Detection</h1>", unsafe_allow_html=True)

# Set page title
st.title("Cyber-Bullying Detection🔍")

# Load data
st.header("Data Loading")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    # Replace NaN values with an empty string
    df['text_clean'] = df['text_clean'].fillna('')

    # Preprocess data
    st.header("Data Preprocessing")
    X = df['text_clean']
    y = df['sentiment']

    # Select Vectorizer
    st.header("Select Vectorizer")
    vectorizer_choice = st.selectbox("Select Vectorizer", ["Select a Vectorizer", "TF-IDF", "CountVectorizer"])
    

    if vectorizer_choice == "TF-IDF":
        vectorizer = TfidfVectorizer()
    else:
        vectorizer = CountVectorizer()

    X_train_vec = vectorizer.fit_transform(X)

    # Train Naive Bayes or SVM
    st.header("Train The Model")
    model_choice = st.selectbox("Select Model", ["Select a Model", "Naive Bayes", "Support Vector Machine", "BERT"])

    if model_choice == "Naive Bayes":
        model = MultinomialNB()
        model.fit(X_train_vec, y)
    else:
        model = SVC(kernel='linear')
        model.fit(X_train_vec, y)

    # Prediction
    st.header("Prediction")
    test_text = st.text_area("Enter text for prediction")
    if test_text:
        test_text_vec = vectorizer.transform([test_text])
        prediction = model.predict(test_text_vec)
        st.write(f"Predicted sentiment: {prediction[0]}")

    # Evaluate model
    st.header("Model Evaluation")
    y_pred = model.predict(X_train_vec)
    report = classification_report(y, y_pred, output_dict=True)
    st.write(pd.DataFrame(report).transpose())
else:
    st.warning("Please upload a CSV file to continue.")
