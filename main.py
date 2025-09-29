import os
from diffusers import StableDiffusionPipeline
import torch
from gtts import gTTS
from pydub import AudioSegment
from pydub import AudioSegment
from pydub.utils import which

# Tell pydub exactly where ffmpeg.exe is
AudioSegment.converter = r"C:\Users\DELL\Downloads\ffmpeg-n8.0-latest-win64-gpl-8.0\ffmpeg-n8.0-latest-win64-gpl-8.0\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\Users\DELL\Downloads\ffmpeg-n8.0-latest-win64-gpl-8.0\ffmpeg-n8.0-latest-win64-gpl-8.0\bin\ffprobe.exe"


# MoviePy imports
from moviepy.editor import ImageClip, AudioFileClip

# ---------------------------
# 0. Setup output folder
# ---------------------------
output_dir = "poc_outputs"
os.makedirs(output_dir, exist_ok=True)

# ---------------------------
# 1. TEXT → IMAGE (Stable Diffusion)
# ---------------------------
prompt = "A futuristic city skyline at sunset, cyberpunk style"
print("🔹 Generating image...")
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32
)
image = pipe(prompt).images[0]

image_path = os.path.join(output_dir, "generated_image.png")
image.save(image_path)

# ---------------------------
# 2. TEXT → AUDIO (gTTS)
# ---------------------------
print("🔹 Generating narration...")
narration_text = (
    "This is a demo of multimodal AI. "
    "The image you see was generated from text, and this narration was generated using AI."
)
tts = gTTS(narration_text)
tts_path = os.path.join(output_dir, "narration.mp3")
tts.save(tts_path)

# Convert MP3 → WAV (pydub)
sound = AudioSegment.from_mp3(tts_path)
audio_path = os.path.join(output_dir, "narration.wav")
sound.export(audio_path, format="wav")

# ---------------------------
# 3. COMBINE IMAGE + AUDIO → VIDEO
# ---------------------------
print("🔹 Creating video...")
clip = ImageClip(image_path, duration=10)
audio = AudioFileClip(audio_path)

final_clip = clip.set_audio(audio)
final_video_path = os.path.join(output_dir, "final_demo.mp4")
final_clip.write_videofile(final_video_path, fps=24)

print(f"✅ Demo complete! Video saved at {final_video_path}")
