# WhisperSubMaker

WhisperSubMakerは、動画ファイル（MP4）から音声認識を行い、
そのセリフを動画のスクリーンショット上に字幕のように書き込んだ画像を自動生成するPythonアプリです。

動画を再生せず、画像とセリフだけで内容を把握できるようにすることを目的に作成しました。

---

## 🔧 使用技術・ライブラリ

以下のライブラリ・ソフトウェアを使用しています：

- OpenAI Whisper（音声認識）
- ffmpeg（音声抽出）
- opencv-python（画像処理）
- moviepy（フレーム抽出）
- Pillow（字幕描画）

---

## ⚠ 注意点

- Whisperのモデル（特に medium や large）はサイズが大きく、初回ダウンロードに時間がかかります。
- 実行時間もモデルサイズに比例して長くなります。PCの性能に応じて tiny や small の使用を推奨します。
- WhisperはGPU対応ですが、CPUのみでも動作します。

---

## 🖥 動作環境

- Python 3.8 以上
- ffmpeg（環境変数PATHに登録されている必要あり）

---

## 📦 インストール方法

```bash
pip install -r requirements.txt
```

---

## ▶ 使い方

### ✅ GUIモード（初心者向け）

```bash
python main.py
```

- ファイル選択ダイアログが表示されます。MP4動画を選んでください。
- モデルサイズ（例：small, medium, large）を入力すると処理が始まります。

### ✅ コマンドラインモード

```bash
python main.py <動画ファイルパス> [Whisperモデル名]
```

例：

```bash
python main.py "video.mp4" medium
```

---

## 📂 出力例

```
output_video/
├── video.wav         # 音声ファイル
├── video.json        # Whisperの文字起こし結果
├── frame_0000.jpg    # 字幕付き画像
├── frame_0001.jpg
└── ...
```

---

## 📁 ディレクトリ構成

```
WhisperSubMaker/
├── main.py
├── video_utils.py
├── whisper_utils.py
├── subtitle_renderer.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🪪 免責事項

- 自由に使用・改変・再配布可能です。
- 製作者は一切の問い合わせに応じません。
- 使用によるいかなる損害についても責任を負いません。
