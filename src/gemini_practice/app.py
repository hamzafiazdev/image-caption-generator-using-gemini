import streamlit as st
from google import genai
from google.genai import errors
import PIL.Image
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

client = genai.Client(api_key=GOOGLE_API_KEY)


def build_caption_prompt(style_prompt):
    style_instruction = style_prompt.strip() if style_prompt else "friendly and engaging"

    return f"""
You are a social media caption writer.
Look at the uploaded image and write one polished caption for it.

Style guidance from the user:
{style_instruction}

Rules:
- Return only the final caption text.
- Do not return JSON, bounding boxes, object labels, coordinates, markdown, or analysis.
- Keep it natural, concise, and ready to post.
""".strip()


def response_from_model(style_prompt, image):
    response = client.models.generate_content(
        model=GEMINI_MODEL, contents=[build_caption_prompt(style_prompt), image]
    )
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]

        return image_parts
    else:
        raise FileNotFoundError("File is not found!")


st.set_page_config(page_title="Image caption generator")

st.title("Image Caption Generator")
st.caption("Upload an image and generate a short, engaging caption with Gemini.")
caption_style = st.text_input("Caption style or instruction:", key="caption_style")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("Generate a caption")

if submit:
    # image_data = input_image_setup(uploaded_file)

    if not uploaded_file:
        st.warning("Please upload an image first.")
    else:
        try:
            response = response_from_model(caption_style, image)
        except errors.ClientError as exc:
            if exc.status_code == 429:
                st.error(
                    "Gemini API quota is exhausted for this project/model. "
                    "Wait for the retry/reset time, check AI Studio rate limits, "
                    "or set GEMINI_MODEL in .env to another available free-tier model."
                )
            else:
                st.error(f"Gemini API error: {exc}")
        else:
            st.subheader("The Response is")
            st.write(response)
