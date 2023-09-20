import re
import nltk
from nltk.corpus import stopwords


def count_fre(text, min_len=0, max_len=-1, frequency={}):
    """
        This function get an input string of text and get the frequency of the word with length from min to max.

        Parameters:
        text (string): the text to analysis.
        min (int): the min length of the wanted word
        max (int): the max length of the wanted word
        frequency(dict): the dict with words and frequency

        Returns:
        string: The text in the pdf.
    """

    # Convert the text to lowercase to ensure case-insensitive word counting
    text = text.lower()

    # Split the text into words
    # words = text.split()
    # Regular expression pattern of the words
    if max_len == -1:
        pattern = '\\b[a-z]+\\b'
    else:
        pattern = '\\b[a-z]{' + str(min_len) + ',' + str(max_len) + '}\\b'
    # find english words with length of range min to max
    match_pattern = re.findall(pattern, text)

    # Iterate through the words and count their frequency
    for word in match_pattern:
        frequency[word] = frequency.get(word, 0) + 1
    sorted_fre = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_fre


def remove_stop_word(fre):
    """
    Parameters:
        fre (dict): the dictionary with words and their frequency

        Returns:
        dict:  the dictionary with stop word removed
    """
    # get stop words
    nltk.download('stopwords')
    sw = (stopwords.words('english'))
    # remove stop words
    for word in sw:
        fre.pop(word)
    return fre


