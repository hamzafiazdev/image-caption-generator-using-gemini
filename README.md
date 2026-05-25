# Image Caption Generator Using Gemini

A clean Streamlit web app that uses Google's Gemini API to generate short,
engaging captions from uploaded images. It is designed for social media posts,
content ideas, product visuals, and quick creative caption drafting.

Live app: https://hamza-ig.streamlit.app

## Features

- Upload JPG, JPEG, or PNG images.
- Add an optional prompt to guide the caption style.
- Generate captions using Gemini's multimodal image understanding.
- Configure the Gemini model from environment variables.
- Friendly quota handling for free-tier Gemini API limits.

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- `google-genai`
- Pillow

## Run Locally

Clone the repository and install the dependencies:

```powershell
$env:UV_SYSTEM_CERTS="true"; uv sync
```

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
```

Start the app:

```powershell
$env:UV_SYSTEM_CERTS="true"; uv run streamlit run src/gemini_practice/app.py
```

If you prefer `pip`, install from `requirements.txt`:

```powershell
pip install -r requirements.txt
streamlit run src/gemini_practice/app.py
```

## Streamlit Cloud Deployment

This app is deployed on Streamlit Community Cloud.

Deployment settings:

```text
Repository: hamzafiazdev/image-caption-generator-using-gemini
Branch: main
Main file path: src/gemini_practice/app.py
```

Required Streamlit secrets:

```toml
GOOGLE_API_KEY="your_api_key_here"
GEMINI_MODEL="gemini-2.5-flash-lite"
```

## Notes

Gemini free-tier quotas can vary by model and project. If the app shows a quota
message, wait for the reset window or switch `GEMINI_MODEL` to another available
free-tier model in your environment settings.
