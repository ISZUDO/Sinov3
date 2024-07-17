import wikipedia
wikipedia.set_lang('uz')
def wiki_bot(text):
    try:
        return wikipedia.summary(text)
    except:
      return f"Bu ma`lumot topilmadi"