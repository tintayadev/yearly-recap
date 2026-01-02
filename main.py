from pathlib import Path

from moviepy import ImageClip, VideoFileClip, concatenate_videoclips, vfx
from proglog import TqdmProgressBarLogger
from tqdm import tqdm


IMAGE_DURATION = 0.2
VIDEO_DURATION = 0.4
VIDEO_SPEED = 2

WIDTH = 1080
HEIGHT = 1920
FPS = 30

IMAGES_DIR = Path("media/images")
VIDEOS_DIR = Path("media/videos")
OUTPUT_FILE = "yearly_recap_vertical.mp4"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv"}


def load_images():
    files = [f for f in IMAGES_DIR.glob("*") if f.suffix.lower() in IMAGE_EXTENSIONS]
    clips = []

    print(f"Processing {len(files)} images")

    for img in tqdm(files, desc="Images", unit="img"):
        clip = ImageClip(str(img))
        clip = clip.with_duration(IMAGE_DURATION)
        clip = clip.resized(height=HEIGHT)
        clip = clip.with_background_color(
            size=(WIDTH, HEIGHT),
            color=(0, 0, 0),
            pos=("center", "center"),
        )
        clips.append(clip)

    return clips


def load_videos():
    files = [f for f in VIDEOS_DIR.glob("*") if f.suffix.lower() in VIDEO_EXTENSIONS]
    clips = []

    print(f"Processing {len(files)} videos")

    for vid in tqdm(files, desc="Videos", unit="vid"):
        clip = VideoFileClip(str(vid))
        clip = clip.without_audio()
        clip = clip.resized(height=HEIGHT)
        clip = clip.with_background_color(
            size=(WIDTH, HEIGHT),
            color=(0, 0, 0),
            pos=("center", "center"),
        )

        max_source_duration = min(VIDEO_DURATION * VIDEO_SPEED, clip.duration)
        clip = clip.subclipped(0, max_source_duration)
        clip = clip.with_effects([vfx.MultiplySpeed(VIDEO_SPEED)])

        clips.append(clip)

    return clips


def main():
    clips = []
    clips.extend(load_images())
    clips.extend(load_videos())

    print(f"Concatenating {len(clips)} clips")
    final_video = concatenate_videoclips(clips, method="compose")

    logger = TqdmProgressBarLogger()

    final_video.write_videofile(
        OUTPUT_FILE,
        fps=FPS,
        codec="libx264",
        preset="ultrafast",
        audio=False,
        logger=logger,
    )

    print(f"Video saved as {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
