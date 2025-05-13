import sys
from youtube_search import fetch_youtube_videos
from gemini_ranking import rank_videos_gemini
from speech_to_text import transcribe_audio_hf

def main():
    print("🛠 Choose input type:")
    print("1. Text")
    print("2. Voice (.mp3 or .wav file)")
    choice = input("Enter 1 or 2: ").strip()

    if choice not in ["1", "2"]:
        print("❌ Invalid choice. Please enter 1 or 2.")
        sys.exit(1)

    if choice == "1":
        query = input("🎤 Enter your query (in Hindi or English): ")
        print("\n🔍 Searching YouTube...")

    elif choice == "2":
        print("🔊 Converting and transcribing audio...")
        file_path = input("📂 Enter the path to the audio file (.mp3 or .wav): ")
        
        query = transcribe_audio_hf(file_path)
        print(f"\n📝 Transcribed Query: {query}")
        print("\n🔍 Searching YouTube...")

    videos = fetch_youtube_videos(query)

    if not videos:
        print("❌ No suitable videos found.")
        return

    print(f"📦 Found {len(videos)} videos. Ranking now with Gemini...\n")
    best_video = rank_videos_gemini(query, videos)
    best_video_details =videos['title' == best_video]
    if best_video:
        print("🏆 Best Video:")
        print(f"Title       : {best_video_details['title']}")
        print(f"Link        : {best_video_details['url']}")
    else:
        print("❌ Gemini couldn't determine the best video.")

if __name__ == "__main__":
    main()
