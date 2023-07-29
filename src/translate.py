from google.cloud import translate
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/dingchaoz/.config/gcloud/application_default_credentials.json"

def translate_text(text="はい、いきますよ", project_id="dogwood-boulder-118001"):

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    # try and catch error, if error, return original text
    try: 
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [text],
                "mime_type": "text/plain",
                "source_language_code": "ja",
                "target_language_code": "en-US",
            }
        )
    except:
        print("Translation error")
        return text

    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))

    return translation.translated_text

def translate_array_elements(array):
    for item in array:
        item['text'] = translate_text(item['text'])

# translate_text()
