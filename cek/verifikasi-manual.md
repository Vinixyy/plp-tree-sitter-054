# Verifikasi manual dua file dari repo uji

Repo uji: `C:\Users\adhiy\repo-uji\itsdangerous` (clone `--depth 1`, commit `672971d`, 2025-06-14).
Dua file yang diperiksa: `src/itsdangerous/timed.py` dan `src/itsdangerous/signer.py`.

## Cara verifikasi manual (tanpa tree-sitter)

- TODO/FIXME: `grep -n "TODO\|FIXME" <file>` (di PowerShell: `Select-String -Pattern "TODO|FIXME"`).
- Fungsi panjang: modul `ast` dari Python → `node.lineno` dan `node.end_lineno - node.lineno + 1`, laporkan bila `> 30`.
- Error sintaks: `python -m py_compile <file>`.

## Hasil perbandingan

| File | Temuan manual | Temuan `cek.py` (dari `output-repo.txt`) | Cocok? | Alasan |
| --- | --- | --- | --- | --- |
| `timed.py` | baris 182: `# TODO: Signature is incompatible because parameters were added` | `timed.py:182: # TODO: Signature is incompatible because parameters were added` | ✅ | Regex manual dan `cek.py` sama-sama menangkap komentar TODO pada baris yang sama. |
| `timed.py` | baris 72: `unsign` (87 baris) | `timed.py:72: fungsi unsign (87 baris)` | ✅ | `ast.end_lineno - lineno + 1` = 87; tree-sitter menghitung `end_point[0] - start_point[0] + 1` = 87. |
| `timed.py` | baris 185: `loads` (36 baris) | `timed.py:185: fungsi loads (36 baris)` | ✅ | Kedua metode menghitung baris `def` sampai baris akhir fungsi secara inklusif. |
| `signer.py` | baris 129: `__init__` (45 baris) | `signer.py:129: fungsi __init__ (45 baris)` | ✅ | `__init__` di dalam class ikut terhitung sebagai `function_definition`; sesuai batasan `cek.py`. |
| `signer.py` | baris 182: `derive_key` (32 baris) | `signer.py:182: fungsi derive_key (32 baris)` | ✅ | Sama persis, termasuk batas `> 30`. |
| `timed.py` | `py_compile` exit `0` (valid) | tidak ada laporan error | ✅ | Tidak ada node `ERROR`/`MISSING`. |
| `signer.py` | `py_compile` exit `0` (valid) | tidak ada laporan error | ✅ | Tidak ada node `ERROR`/`MISSING`. |

## Kesimpulan

Seluruh temuan manual cocok dengan `cek.py` pada kedua file: tidak ada *false positive* maupun *false negative*. Satu-satunya perbedaan yang disengaja adalah `cek.py` tidak membedakan secara eksplisit antara node `ERROR` dan `MISSING` saat mencetak (`node.type` yang dipakai), tetapi deteksi `has_error`-nya tetap benar — sudah diuji terpisah dengan `cek/uji/rusak.py` di T6-4.
