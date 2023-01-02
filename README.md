# Name

DaijiJa

数値を大字（日本の領収書などに記載する改ざんの難しい漢数字表記）に変換する

For non-Japanese Readers（日本語圏以外の方向けの説明）:

This module is designed to convert numerical values into Japanese Kanji characters.

Since the kanji representing numbers have a simple form, it is sometimes possible to rewrite a number as another number by simply adding a few lines. In order to protect (usually handwritten) numbers representing monetary values from malicious rewriting, it has been done to use different kanji that have the same pronunciation and are difficult to rewrite, instead of using regular Japanese numerals.

This Python module converts natural numbers into Japanese Kanji characters when they are entered.

# DEMO

通常はmode=1（領収書などでよく使われる表記）を使います。
旧字体を使いたい場合はmode=2またはmode=3を使用します。

Normally use mode=1 (the notation often used on receipts, etc.).
If you want to use the old style, use mode=2 or mode=3.

```python
import DaijiJa
print(DaijiJa.daiji(123456)) # 壱拾弐万参千四百五拾六
print(DaijiJa.daiji(123456,mode=2)) # 壹拾貳万參千四百五拾六
print(DaijiJa.daiji(123456,mode=3)) # 壹拾貳萬參仟肆佰伍拾陸
```

modeごとのそれぞれの漢数字表記は以下の通りです。

| mode | 使用される文字列 |
| ---- | ---- |
| 1(default)  | 零壱弐参四五六七八九拾百千万億 |
| 2 | 零壹貳參四五六七八九拾百千万億 |
| 3 | 零壹貳參肆伍陸漆捌玖拾佰仟萬億 |

引数charlistを使用して、表記をカスタマイズすることもできます。

```python
import DaijiJa
print(DaijiJa.daiji(123456, charlist='0123456789jhsmo')) # 1j2m3s4h5j6
```

# Requirement

N/A

# Installation

通常通りpipでインストールできます。

You can install with pip as usual.

```bash
pip install git+https://github.com/WindVoiceVox/DaijiJa
```

# Note

作者は変換した結果に責任を持つものではありません。もしバグを見つけた方はご連絡ください。

# Author

WindVoice

# License

DaijiJa is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
