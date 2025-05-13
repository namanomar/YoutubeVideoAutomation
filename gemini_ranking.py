import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def rank_videos_gemini(query, videos):
    model = genai.GenerativeModel("gemini-2.0-flash")

    video_data = "\n".join([
        f"{i+1}. Title: {v['title']}\n   Description: {v['description']}" 
        for i, v in enumerate(videos)
    ])

    prompt = f"""
        You are an assistant helping rank YouTube videos. The user asked:
        "{query}"

        Here are the video options:
        {video_data}

        Rank these videos by how relevant and useful the title is for the query.
        Respond with the top 1 video only with title.
        Only include the title of the video in your response.
        Do not include any other text or explanation.
        Note: The title should be the same as the one in the video data.
    """

    response = model.generate_content(prompt)
    return response.text
