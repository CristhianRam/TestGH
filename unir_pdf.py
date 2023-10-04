import PyPDF2
import tkinter as tk
from tkinter import filedialog

tk.Tk().withdraw()
archivos = filedialog.askopenfilenames(title="Selecciona los archivos PDF a unir", filetypes=[("PDF",".pdf")], defaultextension=".pdf", multiple=True)
nombre_salida = filedialog.asksaveasfilename(title="Ingrese el nombre del archivo unido", filetypes=[("PDF",".pdf")], defaultextension=".pdf")
pdf_final = PyPDF2.PdfMerger()

for nombre_archivo in archivos:
    pdf_final.append(nombre_archivo)

pdf_final.write(nombre_salida)
pdf_final.close()
