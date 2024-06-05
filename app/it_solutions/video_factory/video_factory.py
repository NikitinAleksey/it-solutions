import os.path

from moviepy.editor import ImageClip, TextClip, CompositeVideoClip


def create_text_clip(input_text: str) -> TextClip:
    text_clip = TextClip(txt=input_text, color='white', fontsize=250)
    text_clip.duration = 3
    text_width = len(input_text) * 100
    screen_width = 1600
    text_clip = text_clip.set_position(lambda t: (1600 + t*-((text_width + screen_width) / 3), 300))

    return text_clip


def create_background() -> ImageClip:
    file_path = os.path.abspath(os.path.join('it_solutions', 'video_factory', 'background.png'))
    background = ImageClip(file_path)
    background.duration = 3

    return background


def create_final_clip(input_text: str) -> str:
    final_clip = CompositeVideoClip([create_background(), create_text_clip(input_text=input_text)])
    final_clip.duration = 3
    path_to_video = os.path.abspath(os.path.join('it_solutions', 'video_factory', 'my_video.mp4'))
    final_clip.write_videofile(path_to_video, fps=60)

    return 'my_video.mp4'
