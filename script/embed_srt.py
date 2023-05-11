import argparse
from moviepy import editor
import pysrt
import os
from moviepy.config import change_settings
"""
IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"  # Update with your ImageMagick path
assert os.path.isfile(IMAGEMAGICK_BINARY), "ImageMagick binary not found!"
change_settings({"IMAGEMAGICK_BINARY": IMAGEMAGICK_BINARY})"""
def embed_subtitles(video_file, srt_file, output_file):
    # Load the video
    video = editor.VideoFileClip(video_file)

    # Load the subtitles
    subs = pysrt.open(srt_file)

    # Generate a TextClip for each subtitle and add it to a list
    clips = []
    for sub in subs:
        txt_clip = (editor.TextClip(sub.text, fontsize=24, color='white', method='caption')
                    .set_position(('center', 'bottom'))
                    .set_duration((sub.end.ordinal - sub.start.ordinal) / 1000.0)
                    .set_start(sub.start.ordinal / 1000.0))
        clips.append(txt_clip)

    # Composite the TextClips onto the original video
    final = editor.CompositeVideoClip([video] + clips)

    # Write the output
    final.write_videofile(output_file, codec='libx264')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Embeds an SRT file into a video.')
    parser.add_argument('-v', '--video', type=str, required=True, help='Path to the video file.')
    parser.add_argument('-s', '--srt', type=str, required=True, help='Path to the SRT file.')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path to the output video file.')
    args = parser.parse_args()

    embed_subtitles(args.video, args.srt, args.output)