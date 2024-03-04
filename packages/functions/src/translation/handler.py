from easynmt import EasyNMT
import json

def main(event, context):
    path_params = event.get("pathParameters", {})
    
    try:
        body_dict = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError as e:
        print(f"Error parsing body JSON: {e}")
        return

    target_lang = path_params.get("languageCode")
    print("Setting target language to", target_lang)

    source_text = body_dict.get("text")

    if target_lang is None:
        print("Error: 'languageCode' not found in path parameters.")
        return
    if source_text is None:
        print("Error: 'text' not found in body.")
        return


    nmt = EasyNMT("opus-mt")

    source_lang = nmt.language_detection(source_text)

    print(f"Translating from {source_lang} to {target_lang}")

    translated_text = nmt.translate(source_text, target_lang=target_lang, source_lang=source_lang)

    return {"result": translated_text}
