import googletrans
import logging

class GoogletransNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text": ("STRING", {"multiline": True, "default": "Hello, how are you?"}),
                "source_language": (["auto"] + list(googletrans.LANGUAGES.values()), {"default": "english"}),
                "destination_language": (list(googletrans.LANGUAGES.values()), {"default": "english"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translated_text",)
    FUNCTION = "do_translate"
    CATEGORY = "text"

    def do_translate(self, input_text, source_language, destination_language, *args, **kwargs):
        try:
            # Use synchronous translation - googletrans supports both sync and async
            translator = googletrans.Translator()
            translated = translator.translate(str(input_text), src=source_language, dest=destination_language)
            
            return (translated.text,)
        except Exception as e:
            logging.exception(f"Error translating text. input_text={str(input_text)}, source_language={source_language}, destination_language={destination_language}, args={args}, kwargs={kwargs}")
            return (str(e),)

NODE_CLASS_MAPPINGS = {
    "googletrans": GoogletransNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "googletrans": "Google Moogle",
}
