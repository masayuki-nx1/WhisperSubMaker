from video_utils import extract_audio
from whisper_utils import transcribe_audio
from subtitle_renderer import generate_subtitle_images
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog

def main():
    # Tkinterの初期化（ウィンドウは表示しない）
    root = tk.Tk()
    root.withdraw()

    # ファイル選択ダイアログ（MP4）
    video_path_str = filedialog.askopenfilename(
        title="動画ファイルを選択してください",
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
    )

    # キャンセルされたら終了
    if not video_path_str:
        print("キャンセルされました。")
        return

    # Whisperモデル名をダイアログで入力（初期値: medium）
    model = simpledialog.askstring(
        "Whisperモデル選択",
        "使用するモデルを入力してください（例:small, medium, large）",
        initialvalue="medium"
    )
    if not model:
        model = "medium"

    # パスオブジェクトに変換
    mp4_path = Path(video_path_str)
    output_dir = Path(__file__).parent / f"output_{mp4_path.stem}"
    output_dir.mkdir(exist_ok=True)

    wav_path = output_dir / f"{mp4_path.stem}.wav"
    json_path = output_dir / f"{mp4_path.stem}.json"

    # 音声抽出
    extract_audio(mp4_path, wav_path)

    # Whisperで文字起こし
    transcribe_audio(wav_path, json_path, model)

    # 字幕付き画像の生成
    generate_subtitle_images(mp4_path, json_path, output_dir)

    print("完了しました。出力先:", output_dir)

if __name__ == "__main__":
    main()
