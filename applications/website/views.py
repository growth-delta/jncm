from django.shortcuts import render
from django.http import JsonResponse
import openai

def landing_page(request):
    return render(request, "website/landing_page.html")

def Example_React_App(request):
    return render(request, "applications/example_react/react_app.html")

def Example_React_Component(request):
    return render(request, "applications/example_react/react_component.html")

# if request.method == 'POST':
#         code = request.POST['code']
#         language = request.POST['language']
#         if language == 'Select a Programming Language':
#             messages.success(request, 'No Programming Language SELECTED...')
#         if code == '':
#             messages.success(request, 'No Code SUBMITTED...')
#             return render(request, 'applications/ai/openai/index.html', {
#                 'languages': languages,
#                 'content': content,
#                 'code': code,
#                 'language': language,
#             })
#         else:
#             KEY = settings.OPENAI_API_KEY
#             openai.api_key = KEY
#             openai.Model.list()
#             try:
#                 response = openai.Completion.create(
#                     engine = 'text-davinci-003', # OpenAi Model to Query
#                     prompt = f'Respond only with code. Fix this {language} code: {code}', # Query / Prompt
#                     temperature = 0, # Model Refinement
#                     max_tokens = 1000, # Max Text Length
#                     top_p = 1.0,
#                     frequency_penalty = 0.0,
#                     presence_penalty = 0.0,
#                 )
#                 response = (response['choices'][0]['text']).strip()
#             return render(request, 'applications/ai/openai/index.html', {
#                 'response': response,
#                 'language': language,
#             }),