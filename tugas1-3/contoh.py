"""Contoh file untuk latihan query."""

import os
from pathlib import Path


def tambah(a, b):
    """Menjumlahkan dua angka."""
    hasil = a + b
    print("tambah:", hasil)
    return hasil


def sapa(nama, salam="Halo"):
    """Menyapa seseorang."""
    pesan = f"{salam}, {nama}"
    print(pesan)
    return pesan


def baca_file(path):
    """Membaca isi file."""
    return Path(path).read_text()
