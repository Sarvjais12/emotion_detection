import gradio as gr
from deepface import DeepFace
import cv2

# Core logic from your notebook
def detect_emotion(image_path):
    try:
        # analyze the image for emotions
        analysis = DeepFace.analyze(image_path, actions=['emotion'])
        return analysis[0]['dominant_emotion']
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface setup
with gr.Blocks() as demo:
    gr.Markdown("# Customer Support Emotion Detector")
    gr.Markdown("Upload an image of a customer to instantly analyze and classify their dominant facial expression.")
    
    with gr.Row():
        with gr.Column():
            # type="filepath" ensures Gradio passes a string path to your function
            image_input = gr.Image(type="filepath", label="Upload Customer Image")
            analyze_btn = gr.Button("Detect Emotion", variant="primary")
            
        with gr.Column():
            emotion_output = gr.Textbox(label="Detected Emotion")

    # Connect the button to the function
    analyze_btn.click(fn=detect_emotion, inputs=image_input, outputs=emotion_output)

if __name__ == "__main__":
    demo.launch()