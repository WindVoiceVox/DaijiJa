# -*- coding: utf-8 -*-
"""
DaijiJa.py
数値を日本語の大字に変換するモジュール

このモジュールは、数値を日本語の大字（領収書などに記載する漢数字表記）に変換する機能を提供します。
0から999,999,999,999までの自然数を変換することができます。
"""
from typing import Dict, Union, Literal

# 漢数字の定義
_mode: Dict[int, str] = {
    1: '零壱弐参四五六七八九拾百千万億',
    2: '零壹貳參四五六七八九拾百千万億',
    3: '零壹貳參肆伍陸漆捌玖拾佰仟萬億'
}

def daiji(number: int, mode: Literal[1, 2, 3] = 1, charlist: str = '') -> str:
    """数値を大字（領収書などに記載する漢数字表記）に変換する

    Args:
        number: 変換する数値。自然数で0から999,999,999,999までであること。
        mode: 漢数字の表記のモード。領収書などは通常1を使用する。古い表記を使用したい場合は2または3を使用する。
            1: 一般的な表記（壱、弐、参など）
            2: 古い表記（壹、貳、參など）
            3: より古い表記（壹、貳、參、肆、伍など）
        charlist: 表記をカスタマイズしたい場合に使用する。
            '零壱弐参四五六七八九拾百千万億'のように文字の例を指定する。
            指定する場合は15文字である必要があります。

    Returns:
        大字表記された数値の文字列

    Raises:
        ValueError: 数値が0未満または999,999,999,999より大きい場合、またはcharlistの長さが不適切な場合
        TypeError: 数値が整数でない場合

    Examples:
        >>> daiji(123456789)
        '壱億弐千参百四拾五万六千七百八拾九'
        >>> daiji(123456789, mode=2)
        '壹億貳千參百四拾五万六千七百八拾九'
        >>> daiji(123456789, mode=3)
        '壹億貳仟參佰肆拾伍萬陸仟漆佰捌拾玖'
        >>> daiji(123456789, charlist='零一二三四五六七八九十百千万億')
        '一億二千三百四十五万六千七百八十九'
    """
    if isinstance(number, int):
        if number < 0 or number > 999999999999:
            raise ValueError('Not a natural number (0 to 999,999,999,999)')
        else:
            if charlist != '' and len(charlist) != len(_mode[1]):
                raise ValueError('charlist not proper length')
            if charlist == '':
                kanjichar = _mode[mode]
            else:
                kanjichar = charlist
            return(_daiji(number, kanjichar))
    else:
        raise TypeError('Not a Number.')

def _daiji(number: int, charlist: str) -> str:
    """数値を大字に変換する内部関数

    Args:
        number: 変換する数値
        charlist: 使用する漢数字の文字列

    Returns:
        大字表記された数値の文字列
    """
    # Only zeros are processed first
    if number == 0: return charlist[0]
    c1 = ''
    c2 = ''
    c3 = ''
    n = number % 10000
    c1 = _daiji4(n, charlist)
    if number > 9999:
        n = (number // 10000) % 10000
        if n != 0: c2 = _daiji4(n, charlist) + charlist[13]
    if number > 99999999:
        n = (number // 100000000) % 10000
        if n != 0: c3 = _daiji4(n, charlist) + charlist[14]
    return c3 + c2 + c1

def _daiji4(number4: int, charlist: str) -> str:
    """4桁までの数値を大字に変換する内部関数

    Args:
        number4: 変換する数値（1から9999までの自然数）
        charlist: 使用する漢数字の文字列

    Returns:
        大字表記された数値の文字列
    """
    # Number4 is a natural number between 1 and 9999
    c1 = ''
    c2 = ''
    c3 = ''
    c4 = ''
    n = number4 % 10
    if n != 0: c1 = charlist[n]
    if number4 > 9:
        n = (number4 // 10) % 10
        if n != 0: c2 = charlist[n] + charlist[10]
    if number4 > 99:
        n = (number4 // 100) % 10
        if n != 0: c3 = charlist[n] + charlist[11]
    if number4 > 999:
        n = (number4 // 1000) % 10
        if n != 0: c4 = charlist[n] + charlist[12]
    return c4 + c3 + c2 + c1
