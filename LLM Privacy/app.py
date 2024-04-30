import re
import streamlit as st
from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer

# Function to apply color to anonymized tags
def apply_color(text):
    colored_text = re.sub(r"(<span style='color:red'>.*?</span>)", r"<span style='color:red'>\1</span>", text)
    return colored_text

# Function to anonymize data
def anonymize_data(document_content, fake_data=False):
    anonymizer = PresidioReversibleAnonymizer(add_default_faker_operators=fake_data)
    anonymized_content = anonymizer.anonymize(document_content)
    return anonymized_content

# Streamlit app
def main():
    st.title("Text Anonymizer")
    st.sidebar.title("About")
    st.sidebar.info(
        "This app anonymizes sensitive information in text documents.\n"
        "It uses Presidio for anonymization and Faker for generating fake data."
    )

    # Image
    st.image("llm_privacy.png", use_column_width=True)  # Add your image path here

    # Text input
    st.subheader("Enter Text")
    document_content = st.text_area("Paste your text here")

    if st.button("Anonymize"):
        # Display original text content
        st.subheader("Original Text")
        st.code(document_content, language="html")

        # Anonymize data
        st.subheader("Anonymized Data")
        anonymized_content = anonymize_data(document_content)
        colored_anonymized_content = apply_color(anonymized_content)
        st.code(colored_anonymized_content, language="html")

        # Anonymize data with fake data
        st.subheader("Anonymized Data with Fake Data")
        fake_anonymized_content = anonymize_data(document_content, fake_data=True)
        colored_fake_anonymized_content = apply_color(fake_anonymized_content)
        st.code(colored_fake_anonymized_content, language="html")

if __name__ == "__main__":
    main()
