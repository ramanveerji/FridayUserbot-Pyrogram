from fridaybot.Configs import Config
from googletrans import LANGUAGES
from google_trans_new import google_translator

def tr(text):
    kk = Config.LANG if LANGUAGES.get(Config.LANG) else 'en'
    if kk == 'en':
        hmm = text
    else:
        try:
            translator = google_translator()
            translated = translator.translate(text, lang_tgt=kk)
            hmm = translated
        except:
            hmm = text
    return hmm
