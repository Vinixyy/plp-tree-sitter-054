# Perkiraan Pohon

## Contoh format (bukan jawaban)

Kode: `x = 1`

Perkiraan:

```text
(module
  (expression_statement
    (assignment
      left: (identifier)
      right: (integer))))
```

## fungsi.py

### Perkiraan

```text
(module
  (function_definition
    name: (identifier)
    parameters: (parameters
      (identifier))
    (return_statement
      (identifier))))
```

### Hasil sebenarnya

```text
(module
  (function_definition
    name: (identifier)
    parameters: (parameters
      (identifier))
    body: (block
      (expression_statement
        (assignment
          left: (identifier)
          right: (string
            (string_start)
            (string_content)
            (interpolation
              expression: (identifier))
            (string_end))))
      (return_statement
        (identifier)))))
```

### Perbedaan

- Saya kira isi fungsi langsung berupa `return_statement`, ternyata seluruh isi
  badan fungsi dibungkus node `block`.
- Baris `pesan = f"Halo, {nama}"` bukan node lepas, melainkan
  `expression_statement` -> `assignment`. Saya tidak menulis keduanya.
- Field `body:` pada `function_definition` tidak saya tulis (begitu juga
  `name:` dan `parameters:`).
- F-string tidak disimpan sebagai satu node `string` saja. Di dalamnya ada
  `string_start`, `string_content`, `string_end`, dan bagian
  `{nama}` menjadi `interpolation expression: (identifier)`.
- Saya tidak menulis field `left:` dan `right:` pada `assignment`.

## if_else.py

### Perkiraan

```text
(module
  (assignment
    (identifier)
    (integer))
  (if_statement
    (comparison_operator
      (identifier)
      (integer))
    (block
      (assignment
        (identifier)
        (string)))
    (else_clause
      (block
        (assignment
          (identifier)
          (string))))))
```

### Hasil sebenarnya

```text
(module
  (expression_statement
    (assignment
      left: (identifier)
      right: (integer)))
  (if_statement
    condition: (comparison_operator
      (identifier)
      (integer))
    consequence: (block
      (expression_statement
        (assignment
          left: (identifier)
          right: (string
            (string_start)
            (string_content)
            (string_end)))))
    alternative: (else_clause
      body: (block
        (expression_statement
          (assignment
            left: (identifier)
            right: (string
              (string_start)
              (string_content)
              (string_end))))))))
```

### Perbedaan

- `assignment` tidak pernah berdiri sendiri; selalu dibungkus
  `expression_statement`.
- Field yang tidak saya tulis: `condition:`, `consequence:`, `alternative:`,
  serta `body:` pada `else_clause`.
- `else` bukan node anonim di dalam `if_statement`, tetapi anak bernama
  `else_clause`.
- `"lulus"` dan `"remedial"` tidak berupa satu node `string`; isinya dipecah
  menjadi `string_start`, `string_content`, dan `string_end` (string tanpa
  interpolasi tetap punya ketiga bagian itu).
- Operator `>=` tidak tampil di S-expression karena node anonim, jadi
  `comparison_operator` hanya menampilkan dua anak bernama.

## kelas.py

### Perkiraan

```text
(module
  (class_definition
    name: (identifier)
    (block
      (function_definition
        name: (identifier)
        parameters: (parameters
          (identifier)
          (identifier))
        (block
          (assignment
            (attribute
              (identifier)
              (identifier))
            (identifier))))
      (function_definition
        name: (identifier)
        parameters: (parameters
          (identifier))
        (block
          (return_statement
            (string)))))))
```

### Hasil sebenarnya

```text
(module
  (class_definition
    name: (identifier)
    body: (block
      (function_definition
        name: (identifier)
        parameters: (parameters
          (identifier)
          (identifier))
        body: (block
          (expression_statement
            (assignment
              left: (attribute
                object: (identifier)
                attribute: (identifier))
              right: (identifier)))))
      (function_definition
        name: (identifier)
        parameters: (parameters
          (identifier))
        body: (block
          (return_statement
            (string
              (string_start)
              (string_content)
              (interpolation
                expression: (attribute
                  object: (identifier)
                  attribute: (identifier)))
              (string_end))))))))
```

### Perbedaan

- Nama method `__init__` dan `perkenalan` hanya tampil sebagai
  `name: (identifier)`; saya membayangkan node khusus untuk nama method.
- Ternyata method di dalam kelas memakai node yang sama dengan fungsi biasa,
  yaitu `function_definition`, bukan tipe tersendiri.
- `body:` belum saya tulis pada `class_definition` maupun pada kedua
  `function_definition`.
- `self.nama = nama` butuh tiga lapis: `expression_statement` -> `assignment`
  -> `attribute`. Saya hanya menulis dua lapis.
- `attribute` punya field `object:` dan `attribute:`, sedangkan `assignment`
  punya `left:` dan `right:`.
- String `f"Saya {self.nama}"` dipecah seperti f-string di `fungsi.py`, dan
  bagian interpolasinya berisi `attribute`, bukan `identifier` biasa.
