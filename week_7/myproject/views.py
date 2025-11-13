from django.http import JsonResponse, HttpResponse
from PIL import Image
import io
import os


def say_something(request):
    return JsonResponse({"message": "Hello from the sever side"})


def html_func(request):
    return HttpResponse("<h1>Welcome to my backend server</h1>")


def xml_func(request):
    return HttpResponse("<message>This is a xml data</message>", content_type="application/xml")


def text_func(request):
    return HttpResponse("This is a text file")


def csv_func(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="premier_league_table.csv"'
    sheet = '''
        Pos Club, Pts
        1, Arsenal, 85
        2. Chelsea, 72
        3. Man U, 70
    '''
    response.write(sheet)
    return response


def image_func(request):
    img = Image.open('media/imagejsample.jpg')

    desired_size = (800, 600)
    img.thumbnail(desired_size, Image.Resampling.LANCZOS)

    output_buffer = io.BytesIO()

    img.save(output_buffer, format="png")

    image_data = output_buffer.getvalue()

    response = HttpResponse(image_data, content_type='image/jpg')
    return response


def pdf_func(request):
    pdf_path = os.path.join("media", "invoice.pdf")

    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_content = pdf_file.read()
    except FileNotFoundError:
        return HttpResponse("File not found", status=500)
    return HttpResponse(pdf_content, content_type="application/pdf")


def vid_func(request):
    vid_path = os.path.join("media", "videosample.mp4")
    try:
        with open(vid_path, 'rb') as vid_file:
            return HttpResponse(vid_file.read(), content_type="video/mp4")
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)
