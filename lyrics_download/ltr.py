from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import re

# from googletrans import Translator


def toString(text):
    text = ''.join(text)
    return text


def contains_hindi(text):
    transliterated_text = transliterate(text, 'devanagari', 'itrans')
    return text != transliterated_text


def toHindi(lyrics):
    script = sanscript.ITRANS
    output = sanscript.transliterate(lyrics, script, sanscript.DEVANAGARI)
    return output

# def toHindi(text):
#     translator = Translator()
#     translated_text = translator.translate(text, dest='hi')
#     return translated_text.text


def preprocessyrics(lyrics):
    lyrics = toString(lyrics)
    # Join the list of strings into a single string

    pattern = r'^\[.*\]\n?'
    lyrics = re.sub(pattern, '', lyrics, flags=re.MULTILINE)

    # Define the regular expression pattern
    pattern = r'(.+?)\s*\[x(\d+)\]\s*\n'

    def replace_match(match):
        # Extract the line and the number
        line = match.group(1)
        number = int(match.group(2))
        # Return the line repeated number times
        return (line + '\n') * number

    # Replace the matches using the defined function
    lyrics = re.sub(pattern, replace_match, lyrics)

    return lyrics
