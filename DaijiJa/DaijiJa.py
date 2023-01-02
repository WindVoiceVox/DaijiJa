_mode = {
    1 :'零壱弐参四五六七八九拾百千万億',
    2 :'零壹貳參四五六七八九拾百千万億',
    3 :'零壹貳參肆伍陸漆捌玖拾佰仟萬億'
}

def daiji(number, mode=1):
    """数値を大字（領収書などに記載する漢数字表記）に変換する

    Parameters:
    ---
    number : int
        変換する数値。自然数で0から999,999,999,999までであること。
    mode : 1 or 2 or 3(Default:1)
        漢数字の表記のモード。領収書などは通常1を使用する。古い表記を使用したい場合は2または3を使用する。
    
    Returns:
    ---
    str
        大字表記された数値
    """
    if isinstance(number, int):
        if number < 0 or number > 999999999999:
            raise ValueError('Not a natural number (0 to 999,999,999,999)')
        else:
            return(_daiji(number, mode))
    else:
        raise TypeError('Not a Number.')

def _daiji(number, mode=1):
    kanjichar = _mode[mode]
    # Only zeros are processed first
    if number == 0: return kanjichar[0]
    c1 = ''
    c2 = ''
    c3 = ''
    n = number % 10000
    c1 = _daiji4(n, mode=mode)
    if number > 9999:
        n = (number // 10000) % 10000
        if n != 0 : c2 = _daiji4(n, mode=mode) + kanjichar[13]
    if number > 99999999:
        n = (number // 100000000) % 10000
        if n != 0 : c3 = _daiji4(n, mode=mode) + kanjichar[14]
    return c3 + c2 + c1

def _daiji4(number4, mode=1):
    # Number4 is a natural number between 1 and 9999
    kanjichar = _mode[mode]
    c1 = ''
    c2 = ''
    c3 = ''
    c4 = ''
    n = number4 % 10
    if n != 0: c1 = kanjichar[n]
    if number4 > 9:
        n = (number4 // 10) % 10
        if n != 0: c2 = kanjichar[n] + kanjichar[10]
    if number4 > 99:
        n = (number4 // 100) % 10
        if n != 0: c3 = kanjichar[n] + kanjichar[11]
    if number4 > 999:
        n = (number4 // 1000) % 10
        if n != 0: c4 = kanjichar[n] + kanjichar[12]
    return c4 + c3 + c2 + c1