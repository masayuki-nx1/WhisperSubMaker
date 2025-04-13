import subprocess
from pathlib import Path

def extract_audio(video_path: Path, audio_path: Path):
    # ffmpegを使って動画ファイルから音声（モノラル・16kHz）を抽出
    command = [
        "ffmpeg",
        "-y",
        "-i", str(video_path),
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        str(audio_path)
    ]
    subprocess.run(command, check=True)
