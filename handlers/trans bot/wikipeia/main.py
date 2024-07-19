import wikipedia

wikipedia.set_lang('uz')

def wiki_bot(text):
    try:
        return f"Salom sizga biz qanday yordam bera olaman"
    except:
        return f"Kechirasiz lekin bizda bunday malumot yo'q"