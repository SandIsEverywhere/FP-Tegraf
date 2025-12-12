## Anggota Kelompok B07
| Name           | NRP        | Kelas     |
| ---            | ---        | ----------|
| Joaquin Fairuz Nawfal Ismono | 5025241106 | B |
| Hasan Abdurrahman | 5025241114 | B |
| Royan Habibi Alfatih | 5025241115 | B |

## Soal 1
> The Knight's Tour

**Jawaban:**

- Alur Penggunaan

  Pengguna akan diprompt untuk suatu nilai, ini adalah berapa iterasi per detik yang akan disimulasikan.\
  Kemudian akan tersedia screen dengan chessboard kosong, perlu klik salah satu square untuk starting point dari knight's tour ini.


## Soal 2
> Largest Monotonically Increasing Subsequence

**Jawaban:**

- Alur Penggunaan

  Disini tidak terdapat visualisasi, dan contoh sequence dari soal sudah ada, dan jika ingin diganti maka diganti dari situ saja.\
  Output akan terdiri dari value node di tree dan id-nya (untuk tujuan debugging), level dari node tersebut bisa dibaca dari indentasinya.\
  Parent dari suatu node didapat dari node pertama diatasnya dengan inden 1 kurang dari node tersebut.\
  Contoh:
  ```
  4 (id 1)
    13 (id 2)
    7 (id 3)
  ```
  Untuk mendapat largest monotonically increasing subsequence, lihat dari yang indennya paling banyak, dan work backwards dari situ.
