import streamlit as st
from PIL import Image
import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer, pipeline
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv('.env')

groq_api_key = os.getenv("GROQ_API_KEY")

# Load image captioning model
image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

# Initialize ChatGroq for moderation check
chat = ChatGroq(temperature=1, model_name="mixtral-8x7b-32768", groq_api_key=groq_api_key)

# Load VQA model
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Load VQA processor and model
from transformers import ViltProcessor, ViltForQuestionAnswering
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
vqa_model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# Function to check moderation
def check_moderation(image_description):
    
        # Construct prompt for moderation check
        prompt = f"Is the image description '{image_description}' appropriate according to moderation guidelines?, return 1 if yes else return 0, just return 1 or 0 as an integer and nothing else"
        response = chat.invoke(prompt)
        print(response.content)
        # Return 1 if the image description follows moderation guidelines, else 0
        if response.content=="1":
            return 1
        else:
            return 0
         

   

# Function to get image description
def get_image_description(image):
   
        # Get image description
        description = image_to_text(image)[0]["generated_text"]
        print(description)
        return description

   
# Function to get VQA answer
def get_answer(image, question):
    try:
        # Prepare inputs
        encoding = processor(image, question, return_tensors="pt")

        # Forward pass
        outputs = vqa_model(**encoding)
        logits = outputs.logits
        idx = logits.argmax(-1).item()
        answer = vqa_model.config.id2label[idx]

        return answer

    except Exception as e:
        st.error("Error in VQA:", e)
        return "Error"

# Set up the Streamlit app
st.title("Visual Question Answering")
st.write("Upload an image and enter a question to get an answer.")

# Create columns for image upload and input fields
col1, col2 = st.columns(2)

# Image upload
with col1:
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, use_column_width=True)

# Question input
with col2:
    question = st.text_input("Question")

# Process the image and question when both are provided
if uploaded_file and question:
    # Get image description
    image = Image.open(uploaded_file).convert("RGB")
    image_description = get_image_description(image)

    # Check moderation
    moderation_result = check_moderation(image_description)
    print(moderation_result)

    if moderation_result:
        # Get answer
        answer = get_answer(image, question)

        # Display the answer
        st.success("Answer: " + answer)
    else:
        st.error("The image description does not follow moderation guidelines. Unable to answer the question.")
