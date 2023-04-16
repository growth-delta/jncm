import os
from django.shortcuts import render
import markdown

def GPTCode(request):

    markdown_file = os.path.join('./templates/applications/ai/openai/components/ReadMe.md')
    with open(markdown_file, 'r') as file:
        markdown_text = file.read()
    content = markdown.markdown(markdown_text) # Markdown text to HTML

    languages = ['css', 'csv', 'django', 'docker', 'excel-formula', 'gitignore', 'javascript', 'jsx', 'makefile', 'markdown', 'markup', 'powershell', 'python', 'rust', 'sass', 'scss', 'sql', 'swift', 'tsx', 'typescript']
    # print(sorted(languages)) # Sort List Alphabetical Order

    if request.method == 'POST':
        code = request.POST['code']
        lang = request.POST['lang']
        return render(request, 'applications/ai/openai/index.html', {
            'languages': languages,
            'content': content,
            'code': code,
            'lang': lang,
        })

    return render(request, 'applications/ai/openai/index.html', {
        'languages': languages,
        'content': content,
    })