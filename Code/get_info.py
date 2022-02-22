import re
import html_tag


def by_press(url):

    if 'donga.com/news' in url:
        title, date_list, writer, body_text = html_tag.get_DONGA(url)
        press = '동아일보'

    elif 'news.jtbc' in url:
        title, date_list, writer, body_text = html_tag.get_JTBC(url)
        press = 'JTBC'

    elif 'hani.co.kr' in url:
        title, date_list, writer, body_text = html_tag.get_HANI(url)
        press = '한겨레'

    elif 'news.sbs.co.kr' in url:
        title, date_list, writer, body_text = html_tag.get_SBS(url)
        press = 'SBS'

    elif 'news.kbs.co.kr' in url:
        title, date_list, writer, body_text = html_tag.get_KBS(url)
        press = 'KBS'

    elif 'imnews.imbc.com' in url:
        title, date_list, writer, body_text = html_tag.get_MBC(url)
        press = 'MBC'

    elif 'joongang.co.kr' in url:
        title, date_list, writer, body_text = html_tag.get_JOONGANG(url)
        press = '중앙일보'

    else:
        return None

    info = (press, title, date_list, writer, body_text)
    return info


def divide_sentence(info):

    pattern = re.compile(r'\s*(.+?\D[\.\n]+)\s*')
    body = info[4]
    sentences = []
    for line in body:
        sentences.extend(re.findall(pattern, line))

    return sentences


def get_keyword(sentences, key_words):

    res = []
    for sentence in sentences:
        for keyword in key_words:
            if keyword in sentence:
                res.append(sentence)
                break

    return res

