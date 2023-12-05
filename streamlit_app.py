import streamlit as st
import nltk

"""
Write a streamlit app that either translates the English text in an input box
or tokenizes the text in an input box using nltk 
The user selects the mode from a dropdown menu
"""


st.header("Hello World!")
# Add an image to the app
from PIL import Image
image = Image.open('logo.png')
st.image(image, caption='Streamlit logo', use_column_width=True)

"I am learning how to write an app in Streamlit!"

# Add a text box for user to type in a long piece of text
user_input = st.text_area("Please enter a long text here", "Type here")

# Add a dropdown menu to select between 'Translate to Thai' and 'Tokenize'
option = st.selectbox("Please select an option", ("Translate to Thai", "Tokenize"))

# submit button
submit_button = st.button("Submit")

# if push submit button then show tokenized text separated by |
if submit_button:
    # if user select 'Translate to Thai'
    if option == "Translate to Thai":
        # Put the response in a nice box for display
        st.success("Translated to Thai!")
        #st.write("This is the Thai translation")
    # if user select 'Tokenize'
    elif option == "Tokenize":
        tokenized_text = nltk.word_tokenize(user_input)
        st.write("|".join(tokenized_text))
