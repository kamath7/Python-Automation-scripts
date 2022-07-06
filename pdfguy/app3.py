import fitz

with fitz.open("students.pdf") as file:

    for page in file: 
        page1 = file[0].get_text() #only first page
        print(page1)
        # print(page.get_text())