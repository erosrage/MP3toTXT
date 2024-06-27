import moviepy.editor as mp

# Load the video file
video_path = "/mnt/data/Duration Analytics - Documentation-20230612_100644-Meeting Recording (1).mp4"
video = mp.VideoFileClip(video_path)

# Extract the audio
audio = video.audio

# Save the audio to a file
audio_path = "/mnt/data/meeting_audio.wav"
audio.write_audiofile(audio_path)

# Transcribe the audio (using a placeholder function as transcription is not possible here)
def transcribe_audio(audio_path):
    # Placeholder transcription function
    # In a real scenario, you would use an API or a library like SpeechRecognition or AssemblyAI
    transcription = "Transcription of the audio content goes here."
    return transcription

# Get the transcription of the audio
transcription = transcribe_audio(audio_path)
transcription[:500]  # Display the first 500 characters of the transcription for brevity
