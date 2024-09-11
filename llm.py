import streamlit as st
from langchain_community.llms import CTransformers
import requests
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# Load the translation model
# tokenizer = AutoTokenizer.from_pretrained("opus2m-2020-08-01/opus2m.spm32k-spm32k.transformer.model1.npz.best-perplexity.npz")
# model = AutoModelForSeq2SeqLM.from_pretrained("opus2m-2020-08-01/opus2m.spm32k-spm32k.transformer.model1.npz.best-perplexity.npz")

# Load model and tokenizer for English to Sinhala translation
model_name = "facebook/m2m100_418M"
tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model1 = M2M100ForConditionalGeneration.from_pretrained(model_name)


# Function to get the LLM response
def get_llm_response(question):

    # Load the LLM model using CTransformers
        model = CTransformers(
        model='model/llama-2-7b-chat.ggmlv3.q2_K.bin', # Local path to the GGML model
        model_type='llama'
        )
        print("Question: ")
        print(question)
    # Generate a response from the model
        answer = model(question) # CTransformers handles tokenization internally

    # Fetch weather data if location is provided
        return answer
        

# Function to translate text to Sinhala
def translate_to_sinhala(text):
    # Tokenize the input text
    print("Text")
    print(text)
    tokenizer.src_lang = "en"
    encoded_text = tokenizer(text, return_tensors="pt")

    # Generate translation
    generated_tokens = model1.generate(**encoded_text, forced_bos_token_id=tokenizer.get_lang_id("si"))
    print("Tokens")
    print(generated_tokens)
    # Decode the translated text
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    return translated_text

