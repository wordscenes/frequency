from wordfreq import top_n_list
import json

language_codes = [
  'ar', # Arabic
  'bn', # Bengali
  'bs', # Bosnian
  'bg', # Bulgarian
  'ca', # Catalan
  'zh', # Chinese
  'hr', # Croatian
  'cs', # Czech
  'da', # Danish
  'nl', # Dutch
  'en', # English
  'fi', # Finnish
  'fr', # French
  'de', # German
  'el', # Greek
  'he', # Hebrew
  'hi', # Hindi
  'hu', # Hungarian
  'id', # Indonesian
  'it', # Italian
  'ja', # Japanese
  'ko', # Korean
  'lv', # Latvian
  'mk', # Macedonian
  'ms', # Malay
  'nb', # Norwegian
  'fa', # Persian
  'pl', # Polish
  'pt', # Portuguese
  'ro', # Romanian
  'ru', # Russian
  'sr', # Serbian
  'es', # Spanish
  'sv', # Swedish
  'tr', # Turkish
  'uk', # Ukrainian
]

for language_code in language_codes:
  print('Processing %s' % language_code)
  file_name = '../../frequency/%s-freq.txt' % language_code
  top_n = top_n_list(language_code, 100000000)
  with open(file_name, 'w') as file:
    for word in top_n:
      file.write('%s\n' % word)
    file.close()
  