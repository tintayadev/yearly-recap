
# Yearly Recap Video Generator

A simple Python script that generates a fast-paced vertical video recap from images and videos

Images are shown briefly, videos are shortened and sped up, and everything is exported as a single 9:16 video.

---

## Features

- Vertical output (1080x1920)
- Images shown for a fixed short duration
- Videos trimmed and sped up
- Audio removed from all videos
- Progress indicators during processing and rendering
- Compatible with MoviePy 2.x

---

## Project Structure

```

.
├── main.py
├── media/
│   ├── images/
│   │   ├── image1.jpg
│   │   └── image2.png
│   └── videos/
│       ├── video1.mp4
│       └── video2.mov
└── README.md

```

---

## Requirements

- Python 3.10+
- FFmpeg installed on your system

### Python dependencies

```

moviepy>=2.2
tqdm
proglog
pillow

````

---

## Installation

Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate
````

Install dependencies:

```bash
pip install moviepy tqdm proglog pillow
```

Make sure FFmpeg is installed:

* macOS:

```bash
brew install ffmpeg
```

* Ubuntu:

```bash
sudo apt install ffmpeg
```

---

## Usage

Place your media files into the following folders:

* Images: `media/images`
* Videos: `media/videos`

Then run:

```bash
python main.py
```

The output file will be created as:

```
yearly_recap_vertical.mp4
```

---

## Customization

You can easily adjust these values in `main.py`:

* Image duration
* Video duration
* Video speed
* Output resolution
* FPS

All configuration values are defined at the top of the file.

---

## Notes

* The script keeps the original aspect ratio and pads with black bars if needed.
* Designed to be simple, readable, and easy to extend.
* No audio is included in the final video.
