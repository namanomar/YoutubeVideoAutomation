# 🚀 YouTube Video Finder 

This project automates the process of finding the most relevant YouTube video based on a voice or text query in Hindi or English. It filters videos by duration and freshness, and uses an LLM (Gemini 2.0 Flash ) to score and select the best match.

---

## 🎯 Features

- Accepts **voice or text input** (Hindi/English)
- Searches **YouTube** for related videos using the YouTube Data API
- Filters:
  - **Video Duration**: 4–20 minutes
  - **Posted in the last 14 days**
- Uses **Gemini 2.0 Flash** to analyze and rank video titles
- Returns the **top-ranked video** with:
  - Title
  - Link

---

## 🛠 Tech Stack

- **Python**
- **YouTube Data API (v3)**
- **LLMs**: Google Gemini 
- **Voice & Audio**:
  - `torchaudio`, `pydub`, `ffmpeg-python`

---

## 📦 Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

## API intregration

Create a config.py file and add api:
```
YOUTUBE_API_KEY = 
GEMINI_API_KEY = 
```

## To run application

```
python main.py
```

## To test working of project 

Check the test.ipynb