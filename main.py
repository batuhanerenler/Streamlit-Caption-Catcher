import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit_bootstrap_widgets as sbw

# Define a function to download the captions
def download_captions(video_url, language):
    # Extract the video ID from the URL
    video_id = video_url.split("=")[1]

    # Download the captions
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

    # Extract the text from each dictionary and concatenate into a single string
    transcript_text = ""
    for dict in transcript_list:
        transcript_text += dict["text"] + " "

    return transcript_text

# Set up the page layout
st.set_page_config(
    page_title="YouTube Captions Downloader",
    page_icon="🎬",
    layout="wide"
)

# Set the title and create the UI
st.title("YouTube Captions Downloader")
st.markdown("Easily download and save captions from YouTube videos in your chosen language.")

# Create two columns for the input fields
col1, col2 = st.columns(2)
with col1:
    video_url = st.text_input("Enter the YouTube video URL:")
with col2:
    language = st.selectbox("Select the language:", ["en", "es", "fr", "de", "it", "ja", "ko", "nl", "pl", "pt", "ru", "sv", "tr", "zh-Hans", "zh-Hant"])

if st.button("Download"):
    if video_url:
        try:
            captions = download_captions(video_url, language)
            st.write("Captions:")
            st.text_area("", captions, height=300)

            # Save the captions to a text file
            with open("captions.txt", "w", encoding="utf-8") as file:
                file.write(captions)
            stb.success("Captions saved to captions.txt", dismissible=True)
        except Exception as e:
            stb.error(f"Error: {e}", dismissible=True)
    else:
        stb.error("Please enter a valid YouTube video URL.", dismissible=True)
