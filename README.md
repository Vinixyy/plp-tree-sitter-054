# PLP — Tugas Tree-sitter

Repo tugas Tree-sitter: eksplorasi pohon sintaks Python, grammar DSL filter, highlight, dan mini proyek `cek.py` untuk memindai TODO, fungsi panjang, serta error sintaks.

## Struktur

- `tugas1-3/` — skrip parse/penjelajah/query, file `.scm`, dan output `.txt`
- `tree-sitter-filter/` — grammar `filter`, corpus tes, query highlight, generator SQL, dan parser hasil generate di `src/`
- `cek/` — `cek.py` (Python), `cek_js.py` (pengayaan JavaScript), folder `uji/`, dan output
- `docs/` — `environment.md`, `catatan-ai.md`, `laporan-sumber.md`, `proposal-sumber.md`, dan `img/`
- `laporan.pdf` (2 halaman), `proposal-draf.pdf` (1 halaman)

## Environment

Lihat `docs/environment.md`. Ringkasnya: Python 3.14.5, `tree-sitter` Python 0.25.2, `tree-sitter-python` 0.25.0, `tree-sitter-javascript` 0.25.0, dan tree-sitter CLI 0.24.7.

Aktivasi venv yang dipakai saat praktikum (Windows):

```powershell
& "C:\Users\adhiy\AppData\Local\Temp\opencode\tsvenv\Scripts\Activate.ps1"
```

## Cara menjalankan

Parse tiga potongan kode dan simpan pohonnya:

```bash
python tugas1-3/t1.py tugas1-3/potongan/fungsi.py tugas1-3/potongan/if_else.py tugas1-3/potongan/kelas.py
```

Jelajah node (versi rekursif / TreeCursor) dan jalankan query:

```bash
python tugas1-3/jelajah.py tugas1-3/contoh100.py
python tugas1-3/jelajah_cursor.py tugas1-3/contoh100.py
python tugas1-3/q.py tugas1-3/contoh.py tugas1-3/nama_fungsi.scm
```

Grammar filter (dari folder proyek):

```bash
cd tree-sitter-filter
tree-sitter generate
tree-sitter test
tree-sitter highlight contoh.filter
python sql_where.py contoh-sql.filter
cd ..
```

Pemindai kode:

```bash
cd cek
python cek.py uji/
python cek_js.py uji/
cd ..
```

## Laporan

- Sumber laporan: `docs/laporan-sumber.md` → `laporan.pdf`
- Catatan penggunaan AI: `docs/catatan-ai.md`
- Sumber proposal: `docs/proposal-sumber.md` → `proposal-draf.pdf`
- Screenshot: `docs/img/`
