import tkinter as tk
from tkinter import filedialog
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

    print(f"HTML dosyası '{output_html_path}' olarak kaydedildi.")

def select_pdf_and_convert():
   
    root = tk.Tk()
    root.withdraw()  

    
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if pdf_path: 
        output_html_path = pdf_path.rsplit('.', 1)[0] + '.html' 
        pdf_to_html(pdf_path, output_html_path)
    else:
        print("PDF dosyası seçilmedi.")


select_pdf_and_convert()
