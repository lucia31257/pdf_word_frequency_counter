import pytesseract
from pdf2image import convert_from_path
import pandas as pd
import openpyxl


def read_scanned_pdf(file, start=0, end=-1):
    """
        This function read the pdf file with the given name and returns its text.

        Parameters:
        file (string): The file name.

        Returns:
        string: The text in the pdf.
    """

    # Convert each page of the PDF to an image
    pages = convert_from_path(file)
    # set the end page to be the length of the pdf if is not given
    if end == -1:
        end = len(pages)
    # Initialize an empty string to store extracted text
    extracted_text = ''

    # Loop through the pages and perform OCR on each image
    for page in pages[start:end]:
        text = pytesseract.image_to_string(page, lang='eng')
        extracted_text += text

    # return extracted text
    return extracted_text


def write_dict_to_txt(dicti, file_name):
    """
        This function write the word and frequency to txt file.

        Parameters:
        file (string): The file name.
    """
    with open(file_name, 'w') as f:
        for key, value in dicti.items():
            f.write('%s %s\n' % (key, value))
    # f.close()


def write_dict_to_xls(dicti, file_name):
    """
        This function write the word and frequency to xls file.

        Parameters:
        file (string): The file name.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(list(dicti.items()), columns=['Word', 'Fre'])

    # Write the DataFrame to an Excel file
    df.to_excel(file_name, index=False)