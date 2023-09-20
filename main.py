import read_write
import count


def count_pdf_fre(file_r, file_w, page_s=0, page_e=-1, word_len_min=0, word_len_max=-1, stopword=True):
    if page_s < 0:
        page_s = 0
    if page_e != -1 & page_e < 0:
        page_e = -1
    if word_len_min < 0:
        word_len_min = 0
    if word_len_max != -1 & word_len_max < 0:
        word_len_max = -1
    text = read_write.read_scanned_pdf(file_r, page_s, page_e)
    fre = count.count_fre(text, word_len_min, word_len_max)
    if stopword:
        count.remove_stop_word(fre)
    read_write.write_dict_to_xls(fre, file_w)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count_pdf_fre('/Users/lucia/Downloads/security+/REVIEW_GUIDE.pdf', 'review_guide1', 29)
