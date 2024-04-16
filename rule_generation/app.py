import streamlit as st
from logic import page_load,page_concatenation,use_prompt_template,use_chat_prompt
import time
import tempfile


    


def main():
    st.title("PDF Moderation Point Finder")
    
   
    st.sidebar.header("About")
    st.sidebar.write(
        "This app takes a PDF file as input, processes it to find moderation points, "
        "and displays the results."
    )

 
    st.sidebar.header("Upload PDF File")
    uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.sidebar.write("Processing...")
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())

      
        with st.spinner("Processing..."):
            pages=page_load(temp_file.name)
            print(pages)
            texts=page_concatenation(pages)
            formatted_output=use_prompt_template(texts)
            moderation_points=use_chat_prompt(formatted_output)
            st.success("Processing done!")

       
        st.write("Moderation Points:")
        st.write(moderation_points)


if __name__ == "__main__":
    main()
