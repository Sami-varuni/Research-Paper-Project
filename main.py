import pyPDF
import os
folder_path="./pdfs"
lst_all_text=[]
pdf_files=[f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
for file in pdf_files:
    object = PyPDF2.PdfFileReader(os.path.join(file))
    # get number of pages
    NumPages = object.getNumPages()
    text =  ""
    # extract text and do the search
    for i in range(0, NumPages):         
        PageObj = object.getPage(i)
        text += PageObj.extractText() 
            
    lst_all_text.append(text)
