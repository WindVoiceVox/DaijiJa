#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
cli.py
DaijiJaのコマンドラインインターフェース
"""
import sys
import argparse
from typing import List, Optional
from . import daiji

def main(args: Optional[List[str]] = None) -> int:
    """
    DaijiJaのコマンドラインインターフェースのメイン関数

    Args:
        args: コマンドライン引数のリスト。Noneの場合はsys.argvが使用される。

    Returns:
        終了コード。正常終了の場合は0。

    Examples:
        $ daijija 123456
        壱拾弐万参千四百五拾六
        
        $ daijija 123456 --mode 2
        壹拾貳万參千四百五拾六
        
        $ daijija 123456 --mode 3
        壹拾貳萬參仟肆佰伍拾陸
        
        $ daijija 123456 --charlist "零一二三四五六七八九十百千万億"
        一十二万三千四百五十六
    """
    parser = argparse.ArgumentParser(
        description='数値を大字（領収書などに記載する漢数字表記）に変換するツール'
    )
    
    parser.add_argument(
        'number', 
        type=int, 
        help='変換する数値（0から999,999,999,999までの自然数）'
    )
    
    parser.add_argument(
        '--mode', 
        type=int, 
        choices=[1, 2, 3], 
        default=1, 
        help='漢数字の表記モード（1: 一般的な表記、2: 古い表記、3: より古い表記）'
    )
    
    parser.add_argument(
        '--charlist', 
        type=str, 
        default='', 
        help='カスタム漢数字表記（例: "零一二三四五六七八九十百千万億"）'
    )
    
    if args is None:
        args = sys.argv[1:]
    
    parsed_args = parser.parse_args(args)
    
    try:
        result = daiji(
            parsed_args.number, 
            mode=parsed_args.mode, 
            charlist=parsed_args.charlist
        )
        print(result)
        return 0
    except (ValueError, TypeError) as e:
        print(f"エラー: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
