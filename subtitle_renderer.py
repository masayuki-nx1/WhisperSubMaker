from moviepy.editor import VideoFileClip
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json

def generate_subtitle_images(video_path: Path, json_path: Path, output_dir: Path):
    # 日本語フォントの指定（Windows環境）
    font_path = "C:/Windows/Fonts/meiryo.ttc"
    font = ImageFont.truetype(font_path, 40)

    # JSONから字幕セグメントを読み込む
    with open(json_path, "r", encoding="utf-8") as f:
        segments = json.load(f)["segments"]

    # 動画ファイルを読み込む
    video = VideoFileClip(str(video_path))
    for i, seg in enumerate(segments):
        if seg["start"] >= video.duration:
            continue

        # 指定時間のフレームを取得
        frame = video.get_frame(seg["start"])
        img = Image.fromarray(frame)
        draw = ImageDraw.Draw(img)

        # テキストのサイズを計算
        bbox = draw.textbbox((0, 0), seg["text"], font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x, y = (img.width - w) // 2, img.height - h - 30

        # 背景を黒で描画（字幕の視認性向上）
        draw.rectangle([(x - 10, y - 10), (x + w + 10, y + h + 10)], fill=(0, 0, 0, 200))

        # 字幕テキストを描画（白文字）
        draw.text((x, y), seg["text"], font=font, fill="white")

        # 画像を保存
        img.save(output_dir / f"frame_{i:04}.jpg")
