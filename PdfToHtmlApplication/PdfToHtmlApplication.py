import tkinter as tk
from tkinter import filedialog
from pdfminer.high_level import extract_text
from html import escape
from bs4 import BeautifulSoup
import re

def pdf_to_html(pdf_path, output_html_path):
    text = extract_text(pdf_path)
    lines = text.split('\n')
    html_content = """
    <html>
    <head>
        <title>PDF to HTML</title>
    </head>
    <body>
    """

    for line in lines:
        line = line.strip()
        if len(line) > 0:
            if re.match(r'^[A-Z ]+$', line):
                html_content += f"<h2>{escape(line)}</h2>\n"
            else:
                html_content += f"<p>{escape(line)}</p>\n"

    html_content += """
    </body>
    </html>
    """

    soup = BeautifulSoup(html_content, 'html.parser')

    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"HTML file saved as '{output_html_path}'.")

def select_pdf_and_convert():
    root = tk.Tk()
    root.withdraw()

    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if pdf_path:
        output_html_path = pdf_path.rsplit('.', 1)[0] + '.html'
        pdf_to_html(pdf_path, output_html_path)
    else:
        print("No PDF file selected.")

select_pdf_and_convert()
