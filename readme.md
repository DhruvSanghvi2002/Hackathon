# Custom Moderation Policy generation and configuring LLM with custom guidelines, using state of the art Prompt Engineering techniques.

Hello Everyone👋
This is the project made for automatic rule generation based on guidelines provided by user , Thus a user needs to upload a </br>file in the pdf format , and relax🏖️, the rules will be automatically generated, and could be provided to the Large Language models</br>.Powered by strong LLM's and libraries like langchain , it converts your PDF into text and does the preprocessing behind the scenes and generates rules for your LLM's📏.</br>

Rule Generation-User could generated custom rules ,based on the pdf provided by the user.</br>
Custom Configuration of LLM- User could provide his rules to the LLM, and LLM would first check the question based on the guideline provided by the user and then answer the question, If the user doesn't provide the guideline, The LLM would check the question based on preconfigured guidelines.</br>
Trained Model for detection of toxic question - This model is being trained on kaggle dataset which predicts and classifies question in 6 categories namely, toxic, severly toxic,obsence, threat, insult , identity hate. <br/>

## Instruction to run the project

~ For custom rule generation</br>
Go to the directory rule_generation , from there run</br>
`pip install -r requirements.txt`</br>
After getting all the dependencies installed go to app.py and run</br>
`streamlit run app.py`</br>
~For running LLM based on user's provided guideline </br>
Go to directory llm_moderated , from there run</br>
`pip install -r requirements.txt`</br>
After getting all the dependencies installed go to app.py and run</br>
`streamlit run app.py`</br>
~For seeing our trained model and training notebook you could visit</br>
`Toxicity.ipynb ` notebook
