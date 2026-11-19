# Hitungan Manual

Dihitung dari isi `contoh.py` **sebelum** melihat output query.

| File | Fungsi | Parameter | print | import |
| --- | --- | --- | --- | --- |
| contoh.py | 3 | 5 | 2 | 2 |

## Rincian

- **Fungsi (3):** `tambah`, `sapa`, `baca_file`.
- **Parameter (5):** `tambah(a, b)` = 2, `sapa(nama, salam="Halo")` = 2,
  `baca_file(path)` = 1.
- **`print` (2):** `print("tambah:", hasil)` di `tambah`, dan `print(pesan)` di
  `sapa`. Tidak ada `print` di luar fungsi.
- **Import (2):** `import os` dan `from pathlib import Path`.

## Perbandingan dengan output query

| Ukuran | Manual | Hasil query | Cocok? |
| --- | --- | --- | --- |
| Fungsi | 3 | 3 baris (`output-nama-fungsi.txt`) | ya |
| Parameter | 5 | 2 + 2 + 1 (`output-parameter.txt`) | ya |
| print | 2 | 2 match | ya |
| import | 2 | 2 baris (`output-import.txt`) | ya |

## Catatan perbedaan yang tampak

- `output-print.txt` berisi **4 baris** padahal panggilan `print` hanya **2**.
  Penyebabnya `q.py` mencetak semua capture: 2 baris `@fn` + 2 baris `@args`.
  Jadi yang dihitung sebagai "jumlah panggilan" adalah jumlah match, bukan
  jumlah baris.
- `sapa(nama, salam="Halo")` dihitung **2 parameter**, bukan 3. Node
  `default_parameter` adalah satu parameter beserta nilai bawaannya.
- `from pathlib import Path` menambah **1 import**, bukan 2. `Path` adalah nama
  yang diimpor, bukan modul tambahan.
