import os
from json import loads, JSONDecodeError
from fridaybot.Configs import Config
import logging

k = logging.getLogger("TR-ENGINE")
lang = Config.LANG

if not os.path.exists(f'fridaybot/tr_engines/languages_json/{lang}.devsexpojson'):
    k.warning("Invalid Language. Using Default Language - English")
    lang_path = f"fridaybot/tr_engines/languages_json/en.devsexpojson"
else:
    lang_path = f"fridaybot/tr_engines/languages_json/{lang}.devsexpojson"
    
try:
    lang_string = loads(open(lang_path, encoding='utf-8').read())
except JSONDecodeError:
    lang_string = loads(open(f"fridaybot/tr_engines/languages_json/en.devsexpojson", encoding='utf-8').read())
    k.warning("Invalid JSON File. Reverting To English As Default Language.")
    
def tr_engine(string="?"):
    hmm = lang_string['STRINGS']
    final_s = hmm.get(string)
    return final_s   
