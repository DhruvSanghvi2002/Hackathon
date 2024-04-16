from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os;
load_dotenv('.env')
groq_api_key=os.getenv("GROQ_API_KEY")
pdf_file_path="C:/Users/Dhruv Sanghvi/Downloads/it-policy.pdf"
def page_load(pdf_file_path):
  loader = PyPDFLoader(pdf_file_path)
  pages = loader.load_and_split()
  return pages
text=[];
def page_concatenation(pages):
  text=[]
  if pages is not None:
    for i in range(0,min(len(pages),10)):
        if(len(text)<1000):
          text.append(pages[i].page_content)
        else:
          break
  return text



def use_prompt_template(text):
  prompt_template = PromptTemplate.from_template(
    "You are an IT moderator, who needs to process some IT moderation topics based on a list{text} and generate moderation policies."
  )
  formatted_output=prompt_template.format( text=text)
  return formatted_output

def use_chat_prompt(formatted_output):
  chat = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")
  prompt_result=chat.invoke(formatted_output)
  print(prompt_result.content)
  return prompt_result.content