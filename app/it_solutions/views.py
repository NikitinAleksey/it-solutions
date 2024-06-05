import os

from django.http import FileResponse
from django.conf import settings

from .models import Request

from .video_factory.video_factory import create_final_clip


def get_input_text(request, input_text):
    save_request(request, input_text)
    filename = send_text_to_video_factory(input_text=input_text)
    uploading = upload_video(filename)

    return uploading


def save_request(request, input_text):
    log = Request(path=request.path + '/' + input_text)
    log.save()


def send_text_to_video_factory(input_text):
    return create_final_clip(input_text=input_text)


def upload_video(filename: str) -> FileResponse:
    file_path = os.path.join(settings.BASE_DIR, 'it_solutions', 'video_factory', filename)

    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'video/mp4'
    response['Content-Disposition'] = f'attachment; filename={filename}.mp4'

    return response