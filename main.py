from transformers import pipeline
import gradio as gra

classifier = pipeline("text2text-generation", model="czearing/story-to-title")

def predict(text):
    processed_text = classifier(text)[0]
    return processed_text.get('generated_text')

input = gra.inputs.Textbox(label='Write to text')
output = gra.outputs.Textbox(label='Generated text')
app =  gra.Interface(fn = predict, inputs=input, outputs=output)
app.launch(server_port = 7861)
