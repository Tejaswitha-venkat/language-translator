
from translate import Translator

def translate_educational_content(text, target_language):
    try:
        # Initialize the translator with the target language
        translator = Translator(to_lang=target_language)

        # Translate the text
        translated_text = translator.translate(text)

        return {
            "original_text": text,
            "translated_text": translated_text,
            "translated_language": target_language
        }
    except Exception as e:
        return f"Error in translation: {e}"

# Get user input for text and target language
text_to_translate = input("Enter the text to translate: ")
target_lang_code = input("Enter the target language code (e.g., 'fr' for French): ")

# Translate the text
result = translate_educational_content(text_to_translate, target_lang_code)

if isinstance(result, dict):
    print(f"Original text: {result['original_text']}")
    print(f"Translated text: {result['translated_text']}")
    print(f"Translated language: {result['translated_language']}")
else:
    print(result)

