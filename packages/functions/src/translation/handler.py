from easynmt import EasyNMT
import time
import json
import os
import nltk 


cache_folder_path = "/tmp/cache"
os.environ["NLTK_DATA"] = cache_folder_path
os.environ["EASYNMT_CACHE"] = cache_folder_path

nltk.data.path.append("/tmp/nltk_data")
nltk.download('punkt', download_dir="/tmp/nltk_data")

def main(event):
    print("Hello from translation handler!")


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


    nmt = EasyNMT("opus-mt", cache_folder=cache_folder_path)

    start = time.time()

    source_lang = nmt.language_detection(source_text)

    translated_text = nmt.translate(source_text, target_lang=target_lang, source_lang=source_lang)
    
    end = time.time()

    print(f"Translating from {source_lang} to {target_lang} usign model opus-mt")
    print(f"Took {end - start}s")

    return {"result": translated_text}
