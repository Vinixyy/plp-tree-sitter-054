# Catatan Penggunaan AI

Rubrik mewajibkan minimal satu kesalahan atau kekurangan hasil AI yang ditemukan,
beserta buktinya. Catat setiap bantuan AI, bukan hanya yang salah.

## Tugas 3 — Query import

- **Tanggal:** 2026-11-..
- **Yang saya minta:** "Tulis query tree-sitter Python untuk menangkap nama modul pada import dan from import."
- **Hasil AI:** query memakai field `module`.
- **Kesalahan/kekurangan:** `Invalid field name 'module'` saat dijalankan.
- **Bukti verifikasi:** output `python jelajah.py import_contoh.py` menunjukkan field yang benar adalah `module_name`.
- **Perbaikan:** ganti `module` menjadi `module_name`, lalu hitung ulang hasil.
- **Yang saya pelajari:** nama field harus dicek dari pohon, bukan ditebak dari nama yang terdengar masuk akal.

## Tugas 6 — Regex TODO

- **Tanggal:** ...
- **Yang saya minta:** ...
- **Hasil AI:** ...
- **Kesalahan/kekurangan:** regex `TODO|FIXME` juga cocok dengan `TODOLIST`.
- **Bukti verifikasi:** file uji berisi `# TODOLIST` ikut dilaporkan, padahal bukan TODO.
- **Perbaikan:** gunakan batas kata yang didukung query, atau filter tambahan di Python.
- **Yang saya pelajari:** ...
