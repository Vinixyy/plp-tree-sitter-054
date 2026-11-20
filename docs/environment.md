# Environment

Versi yang benar-benar dipakai saat praktikum (Windows, bukan WSL):

- OS: Microsoft Windows 11 Pro, build 10.0.26300
- Python: 3.14.5
- tree-sitter CLI: 0.24.7 (`5e8760bf462ce7b19b3d2396d5b7860f3906a297`), dipasang lokal di folder temp
- Python binding: tree-sitter 0.25.2
- Grammar: tree-sitter-python 0.25.0; tree-sitter-javascript tidak dipasang
- GCC: MinGW.org GCC-6.3.0-1 (32-bit); untuk `filter.so` dipakai MSVC 14.44.35207 x64 karena Python 64-bit tidak bisa memuat DLL 32-bit
- Node/npm: v24.16.0 / 11.13.0

## Perintah aktivasi

```powershell
& "C:\Users\adhiy\AppData\Local\Temp\opencode\tsvenv\Scripts\Activate.ps1"
```

Pada WSL sesuai contoh panduan:

```bash
source ~/.venvs/plp/bin/activate
```

## Catatan

- `tree-sitter init-config` menulis `%APPDATA%\tree-sitter\config.json`. `parser-directories` ditambah dengan `E:\Tugas\Sem 3\PLP\tree-sitter` agar grammar ditemukan dari folder lain.
- `tree-sitter.json` proyek memakai `file-types: ["filter"]` dan `highlights: "queries/highlights.scm"`.
- Field `metadata.version` wajib ada agar CLI 0.24.7 bisa memuat grammar saat pencarian dari `parser-directories` (tanpa itu: `No language found`).
- CLI 0.25.x menolak struktur `tree-sitter.json` dari panduan karena `metadata` bersifat wajib; itulah sebabnya versi 0.24.7 yang dipakai.
