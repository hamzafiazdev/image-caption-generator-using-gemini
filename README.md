# Image Caption Generator Using Gemini

A Streamlit app that generates image captions with the Gemini API.

## Run Locally

```powershell
$env:UV_SYSTEM_CERTS="true"; uv run streamlit run src/gemini_practice/app.py
```

Create a `.env` file with:

```env
GOOGLE_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
```

## Deploy

This app is ready to deploy on Streamlit Community Cloud. Set `GOOGLE_API_KEY`
as an app secret in the Streamlit Cloud dashboard.
