import streamlit as st 
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from logic import page_load,page_concatenation,chat_answer_when_moderation_policy_is_uploaded,chat_answer_when_moderation_policy_is_not_uploaded
import tempfile
def main():
    st.title("Custom Moderation Policy Question Answering Chatbot")
   
    user_question = st.text_input("Ask any question..")
    uploaded_file = st.file_uploader("Upload PDF file for rule generation (optional)", type=["pdf"])
    if uploaded_file:
        st.success("File uploaded successfully!")
        

    
   
        if st.button("Use this file for rule generation"):
            if uploaded_file is not None:
             st.sidebar.write("Processing...")
             with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
            pages=page_load(temp_file.name)
            text=page_concatenation(pages)
            result=chat_answer_when_moderation_policy_is_uploaded(text,user_question)
             # Obtain response from conversation chain
            st.markdown("User's Question:")
            st.write(user_question) # Displays the user's question
            st.markdown("AI Assistant's Response:")
            
            st.write(result) # Displays the chatbot's response
    else:
        if st.button("Generate rule without file"):
            result=chat_answer_when_moderation_policy_is_not_uploaded(user_question)
            # response = use_chat_prompt_for_chatting(result, user_question, memory) # Obtain response from conversation chain
            st.markdown("User's Article:")
            st.write(user_question) # Displays the user's question
            st.markdown("AI Assistant's Response:")
            
            st.write(result) # Displays the chatbot's response

if __name__ == "__main__":
    main()

