# cek.py — pemindai TODO, fungsi panjang, dan error Python

Skrip kecil berbasis Tree-sitter untuk memindai folder berisi file `.py`.

## Instalasi

```bash
python -m pip install tree-sitter==0.25.2 tree-sitter-python==0.25.0
```

Versi yang dipakai saat praktikum: Python 3.14.5, `tree-sitter` 0.25.2, `tree-sitter-python` 0.25.0.

## Cara menjalankan

Dari dalam folder `cek/`:

```bash
cd cek
python cek.py uji/
```

Atau dari root repo, arahkan ke folder mana pun (misalnya repo hasil clone):

```bash
python cek/cek.py C:/Users/adhiy/repo-uji/itsdangerous
```

Hasil bisa disimpan dengan redirection / `tee`:

```bash
python cek.py uji/ | tee output-uji.txt
```

## Contoh output

```
uji\panjang.py:1: fungsi fungsi_panjang (33 baris)
uji\rusak.py:1: error pada )
uji\todo.py:1: # TODO: rapikan validasi
```

Format setiap baris: `file:baris: pesan`. Tiga pesan yang mungkin muncul:

- teks komentar yang mengandung `TODO` atau `FIXME`;
- `fungsi <nama> (<jumlah> baris)` untuk fungsi lebih dari 30 baris;
- `error pada <tipe node>` bila file memiliki node `ERROR`/`MISSING`.

## Fitur

1. **TODO/FIXME** — komentar dicari lewat query Tree-sitter `(comment) @c`, lalu difilter dengan regex `\b(TODO|FIXME)\b`. Regex batas kata ini menghindari false positive seperti `TODOLIST`, yang tetap cocok bila memakai `(#match? @c "TODO|FIXME")`.
2. **Fungsi > 30 baris** — query `(function_definition name: (identifier) @nama) @fungsi`, panjang dihitung dari `start_point` sampai `end_point` secara inklusif.
3. **Error sintaks** — `tree.root_node.has_error`, lalu telusuri rekursif sampai ketemu node `is_error` atau `is_missing`.

## Batasan

- Fungsi di dalam class dan fungsi bersarang (nested) **ikut dihitung** karena keduanya adalah `function_definition`.
- Teks node di-decode dengan `errors="replace"`, sehingga file non-UTF-8 tidak membuat skrip crash (karakter rusak diganti).
- Folder `venv`, `.venv`, `.git`, `node_modules`, dan `__pycache__` dilewati saat menjelajah.
- Hanya file `.py` yang dipindai.
- Saat melaporkan error, yang dicetak adalah `node.type`; untuk node `MISSING` ini bisa berupa token yang hilang, misalnya `)` pada `cek/uji/rusak.py`.
