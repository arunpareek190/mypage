
# example/views.py

from django.shortcuts import render

from datetime import datetime

from django.http import HttpResponse

# def index(request):
#     now = datetime.now()
#     html = f'''
#     <html>
#         <body>
#             <h1>Hello from Vercel!  ARUN...</h1>
#             <p>The current time is { now }.</p>
#         </body>
#     </html>
#     '''
#     return HttpResponse(html)

def index(request):
    return render(request, 'index.html')



