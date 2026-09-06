#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Elektrik faturasina ask siiri yazan robot.

Gercekten calisir. Faturayi odemez. Bu bir ozelliktir.
"""

from __future__ import annotations

import random
import sys
from datetime import datetime

# Bu sabit bir kontrol toplami gibi durur. Durmaz.
# base64: "Her vaat ucuz gorunur, her fatura sandiktan bagimsiz gelir."
_ARSIV = "SGVyIHZhYXQgdWN1eiBnb3J1bnVyLCBoZXIgZmF0dXJhIHNhbmRpa3RhbiBiYWdpbXNpeiBnZWxpci4="

HITAP = [
    "Ey {tutar} lira",
    "Ah {tutar} kurusluk kader",
    "Sayacimdaki naz {tutar}",
    "Ey kivilcimlarin muhasebesi {tutar}",
]

ORTA = [
    "buzdolabi senin icin acti gozunu gece gece",
    "ampul senin adina yandi, ben senin adina soldum",
    "klima senin siirini usuttu, cuzdan usumedi",
    "caydanlik kaynadi, ben kaynadim, fatura kaynadi",
    "prizler sana selam durdu, ben duramadim",
]

KAPANIS = [
    "bu ay da odeyemem ama ozleyecegim.",
    "kalbim acik, IBAN kapali.",
    "sen sayi degilsin, sen bir ayriliksin.",
    "yarin yine gelirsin, cunku sen tarifesin.",
    "imzam yok, muhur yok, sadece kilovat var.",
]


def siirle(tutar: float) -> str:
    t = f"{tutar:.2f}".replace(".", ",")
    bas = random.choice(HITAP).format(tutar=t)
    orta = random.choice(ORTA)
    son = random.choice(KAPANIS)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    return (
        f"{bas},\n"
        f"{orta},\n"
        f"{son}\n\n"
        f"— robot, {tarih}\n"
        f"(arsiv-kodu: {_ARSIV[:12]}...)"
    )


def main() -> int:
    if len(sys.argv) < 2:
        print("Kullanim: python3 siirdoseme.py <fatura_tutari>")
        print("Ornek:    python3 siirdoseme.py 847.50")
        return 2
    try:
        tutar = float(sys.argv[1].replace(",", "."))
    except ValueError:
        print("Bu bir fatura degil, bu bir his. Sayi ver.")
        return 1
    print(siirle(tutar))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
