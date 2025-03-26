import googletrans
import logging
import asyncio

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

    async def translate_text(self, text, src, dest):
        translator = googletrans.Translator()
        return await translator.translate(str(text), src=src, dest=dest)

    def do_translate(self, input_text, source_language, destination_language, *args, **kwargs):
        try:
            # Create new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            # Run the translation
            translated = loop.run_until_complete(
                self.translate_text(input_text, source_language, destination_language)
            )
            
            # Clean up
            loop.close()
            
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