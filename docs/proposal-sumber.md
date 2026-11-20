# Proposal: Linter Tree-sitter untuk Handler Express

## 1. Judul

Linter berbasis Tree-sitter untuk Express: larangan `console.log` dan kewajiban `try/catch` pada handler.

## 2. Masalah dan pengguna

Debug `console.log` sering tertinggal di kode produksi, dan handler tanpa `try/catch` membuat error bocor sebagai 500. Penggunanya: tim backend Node.js/Express dan reviewer PR yang ingin temuan dengan lokasi baris yang pasti.

## 3. Kenapa tidak cukup dengan AI saja

AI bisa menyarankan aturan, tetapi tidak menjamin semua file tercakup, tidak memberi bukti baris, dan bisa terlewat pada kasus negatif (`console.error` di `catch`). Parser sintaks memberi cakupan deterministik dan posisi node yang bisa diverifikasi ulang.

## 4. Bahasa, framework, grammar

JavaScript (Express), grammar `tree-sitter-javascript` 0.25.0 lewat Python binding `tree-sitter` 0.25.2. Target keluaran: file `.js`.

## 5. Contoh kode yang terdeteksi / tidak

- **Terdeteksi:** `console.log("debug", req.body)` di dalam handler; handler `buruk` tanpa `try`.
- **Tidak terdeteksi:** `console.error(e)` di blok `catch`; `logger.info(...)`; handler `baik` yang sudah punya `try/catch`.

## 6. Rancangan query (sudah diuji pada contoh)

```scheme
(call_expression
  function: (member_expression
    object: (identifier) @obj
    property: (property_identifier) @prop)
  (#eq? @obj "console")
  (#eq? @prop "log")) @console_log

(function_declaration
  name: (identifier) @nama
  body: (statement_block (try_statement) @try)) @handler
```

Uji pada 2 fungsi memberi 1 temuan `console.log` (`buruk`) dan 1 handler valid (`baik`).

## 7. Bentuk output

Terminal (`file:baris: aturan: pesan`), JSON `{file, baris, aturan, pesan}` untuk CI, dan opsional anotasi PR/HTML.

## 8. Cara evaluasi

Clone repo Express kecil di luar repo tugas, jalankan tool, lalu cek manual 20 temuan (10 pemanggilan `console`, 10 handler). Target minimal 18/20 keputusan benar; bandingkan dengan `grep` untuk membuktikan nilai parser.

## 9. Rencana dan risiko

Minggu 1: finalisasi query. Minggu 2: pembungkus Python + CLI. Minggu 3: evaluasi 20 temuan. Minggu 4: laporan. Risiko: `console.log.call`, handler arrow function, dan TSX perlu query tambahan; cakupan dibatasi ke `.js` pada draf ini.
