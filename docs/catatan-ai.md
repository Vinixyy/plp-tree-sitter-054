# Catatan Penggunaan AI

Rubrik mewajibkan minimal satu kesalahan atau kekurangan hasil AI yang ditemukan,
beserta buktinya. Catat setiap bantuan AI, bukan hanya yang salah.

## Tugas 3 — Query import

- **Tanggal:** 2026-11-19
- **Yang saya minta:** "Tulis query tree-sitter Python untuk menangkap nama modul pada import dan from import."
- **Hasil AI:** query memakai field `module`.
- **Kesalahan/kekurangan:** `Invalid field name 'module'` saat dijalankan.
- **Bukti verifikasi:** output `python jelajah.py import_contoh.py` menunjukkan field yang benar adalah `module_name`.
- **Perbaikan:** ganti `module` menjadi `module_name`, lalu hitung ulang hasil.
- **Yang saya pelajari:** nama field harus dicek dari pohon, bukan ditebak dari nama yang terdengar masuk akal.

## Tugas 6 — Regex TODO

- **Tanggal:** 2026-11-20
- **Yang saya minta:** "Bandingkan query `(#match? @c \"TODO|FIXME\")` dengan filter regex batas kata pada komentar Python."
- **Hasil AI:** pola `#match?` dianggap sudah cukup untuk mencari TODO/FIXME.
- **Kesalahan/kekurangan:** regex `TODO|FIXME` juga cocok dengan `TODOLIST`, sehingga menghasilkan temuan palsu.
- **Bukti verifikasi:** pada file uji `# TODOLIST: bukan TODO sungguhan`, kedua pola `((comment) @c)` dan `((comment) @c (#match? @c "TODO|FIXME"))` tetap mengembalikan komentar itu; filter `re.compile(r"\b(TODO|FIXME)\b")` tidak.
- **Perbaikan:** pakai `POLA_TODO = re.compile(r"\b(TODO|FIXME)\b")` di Python setelah query `(comment) @c`, seperti di `cek/cek.py` dan `cek/cek_js.py`.
- **Yang saya pelajari:** pencarian substring di query S-expression tidak setara dengan pencarian kata utuh; verifikasi dengan input negatif (false positive) tetap perlu dilakukan.

## Tugas 4 dan 5 — Versi CLI dan metadata

- **Tanggal:** 2026-11-20
- **Yang saya minta:** "Jalankan `tree-sitter generate` mengikuti struktur `tree-sitter.json` dari panduan."
- **Hasil AI:** struktur JSON dari panduan dianggap langsung berfungsi pada CLI terbaru.
- **Kesalahan/kekurangan:** CLI 0.25.2 menolak file karena `missing field metadata`; CLI 0.24.7 bisa `generate`, tetapi pencarian grammar dari `parser-directories` menghasilkan `No language found`.
- **Bukti verifikasi:** pesan error saat `generate` dan saat `parse` dari folder lain; setelah `metadata.version` ditambah di T5-1, kedua perintah exit `0`.
- **Perbaikan:** pakai CLI 0.24.7 dan tambah `"metadata": {"version": "0.1.0"}` pada `tree-sitter.json`.
- **Yang saya pelajari:** asumsi kompatibilitas versi harus diverifikasi dengan menjalankan perintahnya, bukan hanya membaca contoh konfigurasi.
