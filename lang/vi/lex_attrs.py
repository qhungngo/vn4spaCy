# coding: utf8
from __future__ import unicode_literals

from ...attrs import LIKE_NUM


_num_words = [
    "không",
    "một",
    "hai",
    "ba",
    "bốn",
    "năm",
    "sáu",
    "bảy",
    "tám",
    "chín",
    "mười",
    "mươi",
    "trăm",
    "ngàn",
    "nghìn",
    "triệu",
    "tỷ",
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    if text.lower() in _num_words:
        return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
