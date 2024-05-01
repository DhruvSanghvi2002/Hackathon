from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import os;
load_dotenv('.env')
groq_api_key=os.getenv("GROQ_API_KEY")
print( ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768"))

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

def chat_answer_when_moderation_policy_is_uploaded(text,question):
  
  question=question
  text=text

  chat = ChatGroq(temperature=1, model_name="mixtral-8x7b-32768",groq_api_key=groq_api_key)
  

  prompt_template = PromptTemplate.from_template(
    "I will be providing you an article check if it follows the moderation policies provided in the form of list, the article is {question} and list is {text}")
  formatted_output=prompt_template.format(question=question,text=text)
  output=chat.invoke(formatted_output)
  return(output.content)

# chat_answer_when_moderation_policy_is_uploaded()
def chat_answer_when_moderation_policy_is_not_uploaded(question):
  question=question
  chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768",groq_api_key=groq_api_key)
  prompt_template = PromptTemplate.from_template(
    "I will give you an article  , check if it follows your guidelines , the article is {question}" )
  formatted_output=prompt_template.format(question=question)
  output=chat.invoke(formatted_output)
  print(output.content)
  return(output.content)


chat_answer_when_moderation_policy_is_not_uploaded("How to top in an exam")


  