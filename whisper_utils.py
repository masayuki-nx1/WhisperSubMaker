import whisper
import json
from pathlib import Path

def transcribe_audio(audio_path: Path, json_output_path: Path, model_size: str = "medium"):
    # 指定されたサイズのWhisperモデルを読み込む
    model = whisper.load_model(model_size)

    # 音声ファイルから日本語で文字起こしを実行
    result = model.transcribe(str(audio_path), language="ja")

    # 結果をJSON形式で保存
    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
