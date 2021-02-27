from collections import Counter

def get_topwords(word_list : list, n : int) -> list:
    """
    リストから頻出単語を取得する

    Parameters
    ----------
    word_list: list
        単語を要素に持つリスト
    n: int
        取得する単語の数
    
    Returns
    -------
    topwords: tuple list
        上位n個の単語名と頻出度がtuple型で保存されている要素を持つリスト
    """
    topwords = Counter(word_list).most_common()[:n]
    return topwords


def get_ngram(text, n) -> list:
    '''
    textをngramに分割する

    Parameters
    ----------
    text: str
        文字列のテキスト
    n: int
        ngram
    
    Returns
    -------
    wlist: list
        ngramに分割された要素を持つリスト 
    '''
    wlist = []
    for i in range(len(text)-(n-1)):
        wlist.append(text[i:i+n])
    return wlist