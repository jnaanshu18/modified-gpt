import os
import openai
import gradio as gr
import requests

openai.api_key = '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'

API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
HEADERS = {"Authorization": "Bearer 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"}

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

import json

data = []
with open('visualcogs_prepared_valid.json', 'r',encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))
prompt = data

def openai_creat(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    ) 
    return response.choices[0].text


def conversation_history(input, history):
    history = history or []
    s = list(sum(history,()))
    s.append(input)
    inp =' '.join(s)
    output = openai_creat(inp)
    history. append((input, output))
    return history, history


blocks = gr.Blocks()
with blocks:
    chatbot= gr.Chatbot()
    message= gr.Textbox (placeholder= prompt)
    state= gr.State ()
    submit= gr.Button ("click")
    submit.click(conversation_history, inputs=[message, state], outputs= [ chatbot, state])
blocks. launch (debug= True)