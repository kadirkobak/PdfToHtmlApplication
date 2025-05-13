from pdfminer.high_level import extract_text
from html import escape

def pdf_to_html(pdf_path, output_html_path):
   
    text = extract_text(pdf_path)
    
   
    html_content = f"""
    <html>
    <head>
        <title>PDF to HTML</title>
    </head>
    <body>
        <pre>{escape(text)}</pre>
    </body>
    </html>
    """
    
    
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML dosyasý '{output_html_path}' olarak kaydedildi.")


pdf_path = 'input.pdf' 
output_html_path = 'output.html' 

pdf_to_html(pdf_path, output_html_path)

