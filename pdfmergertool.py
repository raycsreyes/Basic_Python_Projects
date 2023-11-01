"""
Description : Combine ALL .pdf files in the current directory into 1 pdf file.
How to use : python pdfmergertool.py trial1.pdf
"""

import PyPDF2 as pdf
import sys
import os
from sys import argv

merger = pdf.PdfMerger()
pdffilename = argv[1]  # user input filename

# Get all files in directory into a list. Check if each file is a .pdf
# If pdf, append the file.
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

# Create a file for the merged pdfs from the for loop. merger.write("combined_trial1.pdf")
merger.write(pdffilename)
