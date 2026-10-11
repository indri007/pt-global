# Proposal Penelitian dan PRD: Analisis Jaringan WhatsApp dengan NodeXL

Oct 11, 2026 · @Indri Kartikasari

# Bagian A: Proposal penelitian

## Ringkasan eksekutif

Penelitian ini memetakan siapa yang mengendalikan arus informasi di grup WhatsApp dan mengapa, dengan menggabungkan analisis jaringan sosial di NodeXL dan wawancara semi-terstruktur, lalu menargetkan jurnal Scopus Q1. Dokumen ini berisi dua bagian: Bagian A adalah proposal penelitian, Bagian B adalah PRD untuk alat bantu yang mengubah ekspor chat WhatsApp menjadi data jaringan siap impor ke NodeXL.

**Judul kerja.** Struktur Jaringan Komunikasi dan Modal Sosial dalam Grup WhatsApp: Studi Metode Campuran dengan Analisis Jaringan Sosial dan Wawancara.

**Masalah.** WhatsApp adalah kanal koordinasi utama di banyak organisasi, sekolah, dan komunitas di Indonesia, tetapi pola siapa berbicara dengan siapa jarang diukur secara sistematis. Akibatnya, klaim tentang "tokoh kunci", "grup yang terpecah", atau "penyebaran hoaks" masih bersifat anekdot.

**Pendekatan.** Pesan grup yang sudah dianonimkan diubah menjadi jaringan berarah (node = anggota, edge = balasan atau mention). NodeXL menghitung sentralitas, kepadatan, reciprocity, dan komunitas. Hasilnya dipakai untuk memilih informan wawancara secara purposive, sehingga angka jaringan dijelaskan oleh alasan perilaku anggota.

**Kontribusi yang diklaim.**

1. Kontribusi teoretis: menguji modal sosial dan struktural hole pada kanal pesan tertutup, bukan media sosial terbuka.
2. Kontribusi metodologis: protokol replikasi dari ekspor chat ke edge list, termasuk validasi heuristik pembentukan edge.
3. Kontribusi praktis: alat bantu (Bagian B) dan rekomendasi tata kelola grup.

**Target publikasi.** Jurnal Scopus Q1 di bidang komunikasi, sistem informasi, atau ilmu sosial komputasional. Daftar kandidat dan strategi ada di bagian Strategi publikasi.

**Keluaran.** Satu artikel utama, satu artikel metodologi atau data (opsional), repositori kode dan data teranonimkan, serta alat konversi chat ke edge list.

**Catatan asumsi.** Objek studi ditulis generik sebagai "grup WhatsApp organisasi atau komunitas" karena objek spesifik belum ditentukan. Bagian bertanda \[isi\] perlu Anda lengkapi.

## Latar belakang dan masalah penelitian

Grup WhatsApp sudah menjadi infrastruktur komunikasi sehari-hari: koordinasi kerja, pengumuman sekolah, arisan, organisasi keagamaan, hingga kampanye. Bedanya dengan media sosial terbuka, WhatsApp adalah ruang semi-privat. Siapa yang boleh masuk dibatasi, pesan tidak bisa dicari publik, dan norma grup dibentuk oleh admin serta kebiasaan anggota. Karena itu, hasil studi tentang X atau Facebook tidak otomatis berlaku.

### Mengapa topik ini penting

- **Informasi mengalir lewat sedikit orang.** Pengamatan umum di banyak grup: sebagian kecil anggota menulis sebagian besar pesan. Jika pola ini terbukti, kualitas keputusan grup bergantung pada orang-orang tersebut.
- **Risiko misinformasi.** Pesan berantai (forwarded) menyebar cepat di ruang tertutup dan sulit diverifikasi dari luar. Literatur internasional tentang WhatsApp banyak membahas ini, tetapi data konteks Indonesia pada tingkat grup kecil masih terbatas.
- **Koordinasi organisasi.** Bagi organisasi, pertanyaan praktisnya sederhana: apakah informasi sampai ke semua orang, atau hanya beredar di satu klik?

### Celah yang ditangani

Studi jaringan WhatsApp yang ada cenderung berfokus pada grup publik berukuran besar dan topik politik. Tiga celah muncul:

1. **Grup kecil hingga menengah yang bersifat organisasional** (puluhan anggota) jarang dianalisis, padahal di sini sebagian besar koordinasi nyata terjadi.
2. **Penjelasan perilaku.** Banyak studi berhenti pada metrik sentralitas. Mengapa seseorang menjadi pusat atau tetap di pinggir jarang dijawab dengan data wawancara.
3. **Transparansi metode.** Cara mengubah teks chat menjadi edge sering tidak dilaporkan, sehingga hasil sulit direplikasi dan dibandingkan.

### Rumusan masalah

Bagaimana struktur jaringan komunikasi terbentuk di grup WhatsApp organisasi atau komunitas, siapa yang menempati posisi strategis, dan bagaimana anggota sendiri menjelaskan posisi tersebut?

### Ruang lingkup

- Unit analisis: grup WhatsApp (\[isi: jumlah grup\]) dengan \[isi: kisaran jumlah anggota\] anggota.
- Periode data: \[isi: misalnya 6 bulan\], termasuk satu periode peristiwa penting untuk analisis perubahan jaringan.
- Yang tidak dicakup: isi pesan pribadi (japri), grup publik terbuka, dan analisis gambar atau suara.

## Tinjauan pustaka dan celah riset

Tinjauan ini disusun dalam tiga aliran: studi WhatsApp sebagai objek penelitian, teori jaringan yang dipakai, dan metode analisis jaringan dengan NodeXL. Rujukan di bawah ditulis dari pengetahuan umum penulis dan belum diverifikasi satu per satu; cek tahun, halaman, dan DOI di Scopus atau Google Scholar sebelum dikutip.

### Aliran 1: WhatsApp sebagai objek penelitian

| Rujukan | Fokus | Relevansi untuk studi ini | Keterbatasan |
| --- | --- | --- | --- |
| Garimella & Tyson (2018), ICWSM | Karakterisasi data grup WhatsApp publik | Menunjukkan bahwa data grup WhatsApp bisa dikumpulkan dan dianalisis secara sistematis | Hanya grup publik, bukan grup organisasi tertutup |
| Caetano et al. (2018) | Diskusi politik di grup publik WhatsApp | Contoh analisis aktivitas dan struktur grup pada konteks politik | Konteks Brasil, grup besar |
| Resende et al. (2019), WWW | Penyebaran misinformasi di grup publik WhatsApp | Rujukan utama untuk pola penyebaran konten dan lintas grup | Fokus konten viral, bukan peran anggota |
| Studi organisasi dan pendidikan tentang WhatsApp | Pemakaian untuk koordinasi dan pembelajaran | Menunjukkan WhatsApp sebagai kanal kerja nyata | Umumnya survei persepsi, jarang data interaksi sebenarnya |

### Aliran 2: Teori jaringan

- **Kekuatan ikatan lemah** (Granovetter, 1973): ikatan lemah menjembatani kelompok dan membawa informasi baru. Relevan untuk anggota yang menghubungkan sub-kelompok di grup.
- **Struktural hole** (Burt, 1992; 2004): aktor yang menjembatani bagian jaringan yang tidak saling terhubung memperoleh keunggulan informasi. Dioperasionalkan lewat betweenness dan constraint.
- **Sentralitas** (Freeman, 1978; Borgatti & Everett): degree, closeness, dan betweenness mengukur bentuk pengaruh yang berbeda, sehingga hasilnya harus ditafsirkan per metrik, bukan digabung.
- **Modal sosial** (Putnam; Lin; Coleman): jaringan sebagai sumber daya yang memudahkan koordinasi dan kepercayaan.
- **Difusi inovasi** (Rogers, 2003): adopter awal dan opinion leader mempercepat penyebaran. Relevan untuk menjelaskan bagaimana informasi atau kebiasaan baru menyebar di grup.

### Aliran 3: Metode dan alat

- **NodeXL** dikembangkan sebagai alat analisis dan visualisasi jaringan berbasis Excel; buku acuannya adalah Hansen, Shneiderman & Smith, *Analyzing Social Media Networks with NodeXL*. Kekuatannya: mudah dipakai peneliti non-pemrogram dan menyediakan metrik graf serta deteksi grup standar.
- **Deteksi komunitas**: algoritma modularitas Newman (2006) dan Clauset, Newman & Moore (2004) menjadi dasar opsi pengelompokan di NodeXL.
- **Metode campuran**: Creswell & Plano Clark untuk desain eksplanatori sekuensial, dan Fetters, Curry & Creswell (2013) untuk integrasi data kuantitatif dan kualitatif.
- **Analisis tematik**: Braun & Clarke (2006) untuk menganalisis transkrip wawancara.

### Celah riset yang disimpulkan

1. Belum banyak studi yang memadukan **data interaksi aktual** dari grup WhatsApp organisasi dengan **penjelasan anggota** dalam satu desain.
2. **Operasionalisasi edge** dari teks chat jarang dilaporkan dan hampir tidak divalidasi. Studi ini memvalidasinya dengan penilaian manual dan koefisien kesepakatan.
3. Perbandingan **sebelum dan sesudah peristiwa** pada grup yang sama jarang dilakukan, padahal itu yang menunjukkan jaringan sebagai proses, bukan potret tunggal.

**Tugas penyelesaian tinjauan:** ambil 40 sampai 60 artikel dari Scopus dengan kata kunci ("WhatsApp" AND ("social network analysis" OR "network analysis")), saring dengan PRISMA, dan ganti tabel di atas dengan tabel hasil saringan Anda.

## Kerangka teori dan hipotesis

Kerangka ini menghubungkan posisi anggota dalam jaringan dengan akses informasi dan peran sosial. Dua teori utama, struktural hole dan modal sosial, dipakai untuk merumuskan hipotesis yang bisa diuji dengan metrik NodeXL.

### Konstruk dan operasionalisasi

| Konstruk | Definisi | Indikator di NodeXL | Level |
| --- | --- | --- | --- |
| Aktivitas komunikasi | Seberapa sering anggota mengirim dan menerima respons | Out-degree, in-degree (berbobot) | Anggota |
| Posisi jembatan | Menghubungkan sub-kelompok yang terpisah | Betweenness centrality | Anggota |
| Kedekatan informasi | Jarak rata-rata ke semua anggota lain | Closeness centrality | Anggota |
| Prestise | Dirujuk oleh anggota yang juga sentral | Eigenvector centrality, PageRank | Anggota |
| Kohesi grup | Kerapatan hubungan dalam grup | Density, clustering coefficient, reciprocity | Grup |
| Fragmentasi | Terpecah menjadi klaster terpisah | Modularity, jumlah komponen terhubung, jumlah grup | Grup |
| Sentralisasi | Seberapa terpusat jaringan pada sedikit anggota | Rasio degree tertinggi terhadap rata-rata, distribusi degree | Grup |

### Hipotesis

Hipotesis diturunkan dari teori dan harus disesuaikan setelah data eksplorasi awal (pilot).

1. **H1 (konsentrasi aktivitas).** Distribusi degree di grup bersifat sangat condong: sebagian kecil anggota menerima sebagian besar balasan. Dasar: pola preferential attachment pada jaringan komunikasi.
2. **H2 (jembatan).** Anggota dengan betweenness tertinggi bukan selalu anggota dengan out-degree tertinggi. Dasar: teori struktural hole, yang membedakan *banyak bicara* dari *menjembatani*.
3. **H3 (peran formal vs informal).** Admin atau pengurus formal memiliki sentralitas lebih tinggi daripada anggota biasa, tetapi sebagian anggota non-formal masuk dalam kelompok sentral teratas. Ini menunjukkan adanya pemimpin informal.
4. **H4 (resiprositas).** Reciprocity lebih tinggi di dalam komunitas hasil deteksi daripada antar-komunitas, sesuai prinsip homofili.
5. **H5 (peristiwa).** Setelah peristiwa penting (misalnya krisis, pergantian pengurus, atau kebijakan baru), density dan sentralisasi berubah secara berarti dibanding periode sebelumnya.

Untuk metode campuran, dua proposisi kualitatif melengkapi hipotesis:

- **P1.** Anggota sentral menjelaskan posisinya melalui peran tugas (tugas administrasi, penyebar pengumuman), bukan hanya sifat pribadi.
- **P2.** Anggota periferal menjelaskan diamnya melalui norma grup (sungkan, hierarki, volume pesan), bukan ketiadaan minat.

### Model konseptual

Posisi jaringan (aktivitas, jembatan, prestise) mempengaruhi akses dan kendali informasi, yang kemudian mempengaruhi hasil koordinasi seperti ketepatan informasi dan partisipasi. Faktor moderasi: norma grup, peran formal, dan ukuran grup. Model ini disajikan sebagai bagan di naskah artikel setelah data terkumpul.

## Pertanyaan penelitian, tujuan, dan kontribusi

### Pertanyaan penelitian

1. **RQ1.** Seperti apa struktur jaringan komunikasi (kepadatan, resiprositas, sentralisasi, komunitas) di grup WhatsApp organisasi atau komunitas?
2. **RQ2.** Siapa yang menempati posisi sentral dan posisi jembatan, dan apakah posisi itu sejalan dengan peran formal (admin, pengurus)?
3. **RQ3.** Bagaimana struktur jaringan berubah sebelum dan sesudah peristiwa penting di grup?
4. **RQ4.** Bagaimana anggota pada posisi sentral, jembatan, dan periferal menjelaskan pola partisipasi mereka sendiri?
5. **RQ5.** Sejauh mana penjelasan anggota (RQ4) mengonfirmasi atau bertentangan dengan pola jaringan (RQ1 sampai RQ3)?

### Tujuan

- **Umum:** menjelaskan hubungan antara struktur jaringan komunikasi dan peran sosial anggota di grup WhatsApp tertutup.
- **Khusus:** (a) mengukur struktur jaringan dengan NodeXL, (b) mengidentifikasi aktor kunci dan komunitas, (c) menguji perubahan jaringan terhadap peristiwa, (d) menjelaskan pola lewat wawancara, (e) menghasilkan protokol dan alat yang bisa direplikasi.

### Kontribusi

| Jenis | Isi | Bukti yang akan ditunjukkan di naskah |
| --- | --- | --- |
| Teoretis | Uji struktural hole dan modal sosial pada kanal pesan tertutup | Hasil H2, H3, dan integrasi dengan wawancara |
| Metodologis | Protokol konversi chat ke edge list dengan validasi manual | Koefisien kesepakatan (Cohen's kappa) dan analisis sensitivitas jendela waktu |
| Empiris | Data jaringan grup organisasi Indonesia | Statistik jaringan dan visualisasi NodeXL |
| Praktis | Rekomendasi tata kelola grup dan alat bantu konversi | Bagian B (PRD) dan lampiran |

### Cara menjawab setiap RQ

| RQ | Data | Analisis | Keluaran |
| --- | --- | --- | --- |
| RQ1 | Edge list seluruh periode | Metrik graf NodeXL: density, reciprocity, modularity, diameter | Tabel statistik grup |
| RQ2 | Edge list + daftar peran formal | Metrik per anggota: betweenness, closeness, eigenvector; perbandingan dengan peran | Peringkat dan diagram sebar |
| RQ3 | Edge list per periode | Metrik graf per periode, dibandingkan | Grafik perubahan |
| RQ4 | Transkrip wawancara | Analisis tematik | Tema dan kutipan |
| RQ5 | Hasil RQ1 sampai RQ4 | Matriks integrasi (joint display) | Tabel integrasi |

## Desain penelitian metode campuran

Desain yang dipakai adalah **metode campuran eksplanatori sekuensial**: tahap kuantitatif (analisis jaringan) dilakukan lebih dulu, lalu hasilnya dipakai memilih informan dan menyusun pertanyaan wawancara pada tahap kualitatif. Kedua hasil disatukan pada tahap interpretasi.

### Tahapan

| Tahap | Kegiatan | Keluaran | Keputusan di akhir tahap |
| --- | --- | --- | --- |
| 0. Persiapan | Izin etik, izin admin dan anggota grup, uji coba (pilot) satu grup | Surat izin, protokol final | Lanjut jika izin lengkap |
| 1. Pengumpulan data | Ekspor chat, anonimisasi, pembentukan edge list | Data jaringan teranonimkan | Lanjut jika kappa validasi edge memadai |
| 2. Analisis jaringan | Metrik graf dan anggota, komunitas, perbandingan periode | Tabel dan visualisasi NodeXL | Tentukan kerangka sampel wawancara |
| 3. Wawancara | 15 sampai 25 wawancara semi-terstruktur | Transkrip | Berhenti saat tema jenuh |
| 4. Integrasi | Joint display, konfirmasi dan kontradiksi | Tabel integrasi | Rumuskan temuan utama |
| 5. Penulisan | Naskah, repositori, ringkasan kebijakan | Artikel dan paket replikasi | Kirim ke jurnal |

### Populasi dan sampel

- **Grup:** pilih \[isi: jumlah\] grup dengan kriteria: aktif (minimal \[isi\] pesan per minggu), minimal 20 anggota, bersifat organisasi atau komunitas, dan admin bersedia memberi izin. Sampel bersifat purposive.
- **Anggota:** semua anggota yang pesannya masuk ke dalam data ditawari persetujuan. Anggota yang menolak dikeluarkan dari analisis dan pesannya dihapus sebelum edge dibentuk.
- **Informan wawancara:** purposive berdasarkan hasil tahap 2 (lihat bagian Wawancara).

### Unit dan jenis data

| Data | Sumber | Dipakai untuk |
| --- | --- | --- |
| Pasangan pengirim dan penerima respons | Ekspor chat WhatsApp (tanpa media) | Edge list, bobot edge |
| Waktu pesan | Ekspor chat | Pembagian periode, jendela balasan |
| Peran formal anggota | Struktur organisasi dari admin | Atribut node |
| Panjang pesan, ada tidaknya tautan | Ekspor chat | Atribut tambahan, bukan isi pesan |
| Transkrip wawancara | Rekaman dengan izin | Analisis tematik |

### Strategi kerja dengan isi pesan

Isi pesan tidak dianalisis kata per kata kecuali untuk subsampel yang dikode manual (misalnya untuk validasi edge dan penanda jenis pesan seperti pengumuman, pertanyaan, atau pesan berantai). Pengecualian ini disetujui dalam persetujuan peserta.

### Kriteria kualitas desain

- **Triangulasi:** metrik jaringan, wawancara, dan (jika ada) dokumen organisasi saling memeriksa.
- **Replikasi:** seluruh aturan edge, versi NodeXL, dan parameter algoritma dicatat.
- **Transparansi keputusan:** setiap keputusan analisis dicatat dalam jurnal penelitian (audit trail).

## Pengumpulan data WhatsApp dan konversi ke edge list NodeXL

NodeXL tidak membaca WhatsApp secara langsung. Data harus diekspor dari aplikasi, dibersihkan, dianonimkan, lalu diubah menjadi daftar edge (Vertex 1, Vertex 2, bobot, atribut) di lembar kerja Excel.

### Langkah 1: ekspor chat

1. Admin atau anggota membuka grup, memilih menu **Ekspor chat**, lalu **Tanpa media**.
2. File `.txt` (atau `.zip` berisi `.txt`) disimpan di perangkat peneliti yang terenkripsi.
3. Format baris bergantung pada bahasa dan pengaturan ponsel, misalnya tanggal dan jam, nama pengirim, lalu teks. Peneliti harus mengecek format di pilot, karena parser harus disesuaikan per format.

### Langkah 2: pembersihan dan anonimisasi

- Ganti semua nama dan nomor telepon dengan kode (M001, M002, dan seterusnya). Tabel pemetaan kode disimpan terpisah dan terenkripsi, dihapus setelah analisis selesai sesuai protokol etik.
- Hapus pesan sistem (anggota masuk, keluar, ganti ikon) dari data pesan, tetapi simpan peristiwa masuk dan keluar sebagai data tersendiri untuk analisis perubahan jaringan.
- Hapus atau tutup informasi pengenal di dalam isi pesan jika isi dikode manual (nama, alamat, nomor).
- Keluarkan pesan anggota yang menarik persetujuan.

### Langkah 3: aturan pembentukan edge

Di ekspor chat, balasan yang dikutip tidak selalu terbaca sebagai hubungan yang jelas. Karena itu edge dibentuk dengan aturan eksplisit yang dilaporkan di naskah dan divalidasi.

| Aturan | Definisi | Kekuatan | Kelemahan |
| --- | --- | --- | --- |
| R1: mention | A menyebut @B dalam pesan, maka edge A ke B | Eksplisit, pasti | Tidak semua balasan memakai mention |
| R2: urutan balasan | Pesan A tepat setelah pesan B dalam jendela T menit dan bukan pesan A sebelumnya, maka edge A ke B | Menangkap balasan tanpa penanda | Bisa salah jika dua percakapan paralel |
| R3: kutipan | Teks pesan A mengandung kutipan dari B (jika terbaca di ekspor) | Sangat spesifik | Sering tidak tersedia di ekspor |

**Aturan utama yang diusulkan:** gabungan R1 dan R2 dengan jendela T = \[isi: misalnya 5\] menit, dan R3 jika tersedia. Jendela diuji dengan analisis sensitivitas pada T = 2, 5, 10, dan 15 menit.

### Langkah 4: validasi edge

1. Ambil sampel acak \[isi: misalnya 300\] pesan.
2. Dua penilai independen menentukan manual siapa yang dibalas oleh setiap pesan.
3. Bandingkan dengan edge hasil aturan: laporkan precision, recall, dan Cohen's kappa antar-penilai.
4. Jika kecocokan rendah, perbaiki aturan atau perpendek jendela, lalu validasi ulang.

### Langkah 5: format impor ke NodeXL

Lembar **Edges** NodeXL memerlukan kolom Vertex 1 dan Vertex 2; kolom bobot dan atribut dapat ditambahkan.

```csv
Vertex 1,Vertex 2,Edge Weight,First Interaction,Last Interaction,Edge Type
M001,M002,14,2026-03-04,2026-08-29,reply
M003,M001,6,2026-03-05,2026-08-30,mention
M002,M004,3,2026-04-12,2026-07-01,reply
```

Lembar **Vertices** diisi atribut anggota: peran formal, tanggal bergabung, jumlah pesan, dan jumlah kata rata-rata.

### Langkah 6: dataset periode

Buat satu file edge list per periode (misalnya per bulan atau per fase sebelum dan sesudah peristiwa) agar metrik graf bisa dibandingkan antar periode. Nama file: `grup01_2026-03.xlsx`, dan seterusnya.

### Pengelolaan data

- Penyimpanan: perangkat terenkripsi, akses terbatas pada tim peneliti.
- Data mentah chat dihapus setelah anonimisasi dan validasi selesai, kecuali sampel validasi.
- Data teranonimkan yang dibagikan di repositori hanya berupa edge list tanpa isi pesan, itu pun hanya jika persetujuan mencakup berbagi data.

## Analisis jaringan di NodeXL: metrik, komunitas, visualisasi

NodeXL berjalan sebagai add-in Excel di Windows, jadi peneliti dengan Mac perlu mesin Windows atau mesin virtual. Versi NodeXL (Basic atau Pro) dan versi Excel dicatat di naskah untuk replikasi.

### Pengaturan graf

- **Jenis graf:** berarah (directed), karena balasan punya arah.
- **Bobot edge:** jumlah interaksi A ke B dalam periode. Analisis dijalankan dua kali, dengan dan tanpa bobot, sebagai uji ketahanan.
- **Layout:** Harel-Koren Fast Multiscale atau Fruchterman-Reingold untuk eksplorasi; hasil akhir di naskah memakai satu layout yang sama antar periode agar perbandingan visual adil.

### Metrik tingkat graf (grup)

| Metrik | Arti | Dipakai untuk |
| --- | --- | --- |
| Vertices dan Edges | Jumlah anggota aktif dan hubungan | Deskripsi dasar |
| Graph density | Proporsi hubungan yang ada dibanding yang mungkin | Kohesi (H4, H5) |
| Reciprocity | Proporsi hubungan yang berbalas | Hubungan timbal balik |
| Connected components | Jumlah kelompok yang tidak terhubung | Fragmentasi |
| Average geodesic distance dan diameter | Jarak rata-rata dan terjauh antar anggota | Kecepatan informasi menjangkau semua orang |
| Modularity | Kekuatan pembagian komunitas | Fragmentasi dan polarisasi |

### Metrik tingkat anggota

| Metrik | Penafsiran | Hati-hati |
| --- | --- | --- |
| In-degree | Seberapa sering dirujuk atau dibalas | Bisa tinggi karena posisi admin, bukan pengaruh |
| Out-degree | Seberapa sering merespons orang lain | Anggota cerewet bisa tinggi tanpa pengaruh |
| Betweenness | Menjembatani pasangan anggota lain | Sensitif terhadap aturan edge dan jendela waktu |
| Closeness | Dekat dengan semua anggota | Tidak stabil jika graf tidak terhubung |
| Eigenvector dan PageRank | Dirujuk oleh anggota yang berpengaruh | Bergantung pada struktur global |
| Clustering coefficient | Kecenderungan kenalan saling terhubung | Rendah pada anggota jembatan |

Setiap metrik ditafsirkan sendiri. Tidak ada satu skor tunggal "pengaruh"; pernyataan di naskah harus menyebut metrik yang dipakai.

### Deteksi komunitas

- Jalankan **Clauset-Newman-Moore** (opsi pengelompokan di NodeXL) sebagai analisis utama.
- Ulangi dengan algoritma lain yang tersedia (misalnya Wakita-Tsurumi) sebagai uji ketahanan.
- Tafsirkan komunitas hanya jika modularity cukup tinggi dan komunitas masuk akal terhadap konteks organisasi (misalnya divisi atau angkatan). Cocokkan dengan informasi dari admin dan wawancara.

### Uji statistik

Graf adalah data yang saling bergantung, sehingga uji standar yang mengasumsikan independensi tidak tepat untuk perbandingan antar anggota.

- Untuk perbandingan antar periode pada satu grup: bandingkan metrik dengan interval kepercayaan hasil bootstrap pada edge, atau uji permutasi.
- Untuk korelasi sentralitas dengan peran formal: gunakan uji permutasi (QAP atau pengacakan label), dijalankan di R atau Python dengan data ekspor dari NodeXL.
- Laporkan ukuran efek dan ketidakpastian, bukan hanya nilai p.

### Visualisasi untuk naskah

1. Sosiogram per periode dengan ukuran node = betweenness dan warna = komunitas.
2. Histogram distribusi degree (skala log) untuk H1.
3. Diagram sebar betweenness versus out-degree untuk H2, dengan peran formal sebagai penanda.
4. Grafik garis density dan modularity per periode untuk H5.

Semua gambar harus terbaca dalam hitam putih dan memiliki deskripsi teks agar aksesibel.

### Alur kerja di NodeXL

1. Impor edge list ke lembar Edges dan atribut ke lembar Vertices.
2. Pilih *Directed*, atur layout, hitung **Graph Metrics** (semua metrik di atas).
3. Jalankan **Groups** dengan algoritma yang dipilih; isi atribut grup di lembar Groups.
4. Ekspor lembar Vertices dan Graph Metrics ke CSV untuk analisis lanjutan dan arsip.
5. Simpan file `.xlsx` per periode dan catat versi NodeXL.

## Wawancara semi-terstruktur dan analisis tematik

Wawancara menjelaskan *mengapa* pola jaringan terbentuk. Informan dipilih dari hasil analisis jaringan, bukan acak, supaya setiap posisi struktural terwakili.

### Kerangka sampel informan

| Kelompok | Kriteria dari NodeXL | Jumlah target | Pertanyaan utama |
| --- | --- | --- | --- |
| Sentral | Degree atau eigenvector tertinggi | 4 sampai 6 | Bagaimana Anda memandang peran Anda di grup? |
| Jembatan | Betweenness tinggi, degree sedang | 3 sampai 5 | Bagaimana Anda menghubungkan kelompok yang berbeda? |
| Periferal | Degree rendah, anggota aktif pasif | 4 sampai 6 | Apa yang membuat Anda jarang menulis? |
| Admin atau pengurus | Peran formal | 2 sampai 3 | Bagaimana Anda mengatur grup? |
| Anggota baru atau keluar | Masuk atau keluar di periode analisis | 2 sampai 3 | Mengapa bergabung atau keluar? |

Total sasaran 15 sampai 25 informan, dihentikan lebih awal jika tema sudah jenuh (tidak ada tema baru pada dua wawancara berturut-turut).

### Pelaksanaan

- **Format:** tatap muka atau video (Zoom atau Google Meet), 30 sampai 45 menit.
- **Bahasa:** Bahasa Indonesia atau bahasa yang nyaman bagi informan.
- **Rekaman:** audio dengan izin tertulis; transkripsi dengan alat bantu (Whisper, Otter, atau Google Docs voice typing) lalu diperiksa ulang oleh peneliti.
- **Pelindung anonimitas:** nama informan diganti kode yang tidak dapat ditautkan langsung ke kode node, kecuali tabel penautan disimpan terpisah dan hanya dipakai untuk integrasi data.

### Pedoman wawancara (inti)

1. **Pembuka:** ceritakan peran Anda di grup dan sejak kapan bergabung.
2. **Pemakaian grup:** jenis informasi apa yang paling sering Anda bagikan atau cari di grup ini?
3. **Hubungan:** kepada siapa Anda biasanya bertanya atau berbagi informasi, dan mengapa orang tersebut?
4. **Norma:** apa aturan tidak tertulis di grup ini (kapan boleh membalas, siapa yang boleh menegur)?
5. **Verifikasi:** bagaimana Anda menilai kebenaran informasi yang diteruskan?
6. **Peristiwa:** apa yang berubah di grup setelah \[isi: peristiwa\]?
7. **Penutup:** apa yang akan Anda ubah dari cara grup ini berkomunikasi?

Pertanyaan pendalaman (probe): "Bisa dijelaskan lebih lanjut?", "Contohnya seperti apa?", "Apa yang Anda rasakan saat itu?" Jangan mengarahkan jawaban dengan hasil NodeXL; hasil jaringan tidak ditunjukkan kepada informan sebelum wawancara selesai.

### Analisis tematik

Mengikuti enam fase Braun & Clarke (2006):

1. Membaca transkrip berulang kali dan membuat catatan awal.
2. Pengodean awal per kalimat atau paragraf.
3. Mencari tema dari kumpulan kode.
4. Meninjau tema terhadap data kode dan seluruh data.
5. Menamai dan mendefinisikan tema.
6. Menulis laporan dengan kutipan representatif.

Perangkat: Taguette (gratis), NVivo, atau ATLAS.ti. Dua pengode independen memberi kode pada 20 persen transkrip, lalu menyamakan buku kode; kesepakatan dilaporkan.

### Integrasi dengan hasil jaringan (joint display)

| Anggota (kode) | Posisi jaringan | Tema wawancara | Konfirmasi atau kontradiksi |
| --- | --- | --- | --- |
| \[isi\] | \[isi: misalnya betweenness tinggi\] | \[isi\] | \[isi\] |

Tabel ini dipakai di naskah untuk menjawab RQ5 dan menunjukkan di mana wawancara menguatkan atau menyanggah angka jaringan.

## Etika, persetujuan, dan perlindungan data

Data chat berisi informasi orang yang tidak selalu sadar sedang diteliti. Jurnal Q1 hampir selalu meminta bukti persetujuan etik dan rincian anonimisasi, sehingga bagian ini menentukan apakah naskah bisa lolos tinjauan.

### Prinsip

1. **Persetujuan berdasarkan informasi (informed consent)** dari seluruh anggota grup yang datanya dipakai, bukan hanya dari admin.
2. **Minimisasi data:** hanya ambil metadata interaksi yang dibutuhkan. Isi pesan tidak disimpan, kecuali subsampel yang dikode manual dan telah disetujui.
3. **Anonimisasi sejak awal:** kode pengganti nama dan nomor dibuat sebelum analisis.
4. **Hak keluar:** anggota boleh menarik diri sebelum analisis; datanya dikeluarkan.
5. **Risiko dan manfaat:** peneliti menilai kemungkinan anggota teridentifikasi dari posisinya di jaringan (misalnya admin yang sangat sentral).

### Tahapan perizinan

| Tahap | Dokumen | Pemberi izin |
| --- | --- | --- |
| 1 | Surat izin penelitian dan penjelasan proyek | Pimpinan organisasi atau admin grup |
| 2 | Formulir persetujuan peserta (daring) | Setiap anggota grup |
| 3 | Persetujuan etik penelitian | Komite etik institusi peneliti |
| 4 | Persetujuan wawancara dan rekaman | Setiap informan |

Persetujuan etik adalah syarat yang sering diminta jurnal; ajukan sebelum pengumpulan data dimulai, bukan sesudahnya.

### Bagian wajib dalam formulir persetujuan

- Tujuan penelitian dan cara data dipakai.
- Jenis data yang diambil (metadata pesan, bukan isi) dan jangka waktu simpan.
- Cara anonimisasi dan siapa yang bisa mengakses data.
- Hak menolak dan menarik diri tanpa konsekuensi.
- Rencana publikasi, termasuk apakah edge list teranonimkan akan dibagikan di repositori.
- Kontak peneliti dan komite etik.

### Risiko dan mitigasi

| Risiko | Mitigasi |
| --- | --- |
| Anggota teridentifikasi dari posisi unik (admin) | Laporkan peran secara umum; jangan tampilkan sosiogram dengan label peran spesifik di grup kecil |
| Kebocoran data mentah | Enkripsi perangkat, akses terbatas, hapus data mentah setelah validasi |
| Anggota merasa diawasi | Jelaskan metode secara terbuka, berikan opsi tidak ikut, tidak menganalisis isi pribadi |
| Penautan antara kode node dan kode wawancara | Pisahkan tabel penautan dan hapus setelah integrasi |
| Peneliti bagian dari grup (konflik peran) | Nyatakan posisi peneliti; hindari memasukkan hubungan kekuasaan dalam rekrutmen |

### Kepatuhan hukum

Peneliti perlu mengecek ketentuan perlindungan data pribadi yang berlaku di Indonesia (UU Pelindungan Data Pribadi) dan kebijakan institusi. Konsultasikan dengan komite etik atau bagian hukum kampus untuk menafsirkan kewajiban yang berlaku pada penelitian ini; dokumen ini bukan nasihat hukum.

## Validitas, reliabilitas, dan keterbatasan

Reviewer Q1 membaca bagian ini untuk menilai apakah peneliti paham batas klaimnya. Tulis keterbatasan secara terbuka, lengkap dengan cara menguranginya.

### Validitas dan reliabilitas

| Aspek | Ancaman | Penanganan |
| --- | --- | --- |
| Validitas konstruk | Edge dari urutan pesan belum tentu balasan sungguhan | Validasi manual, kappa, analisis sensitivitas jendela waktu |
| Validitas internal | Perubahan jaringan bisa disebabkan hal selain peristiwa | Bandingkan dengan periode kontrol, sebut penjelasan alternatif |
| Validitas eksternal | Hasil dari grup terpilih tidak berlaku untuk semua grup | Batasi klaim pada tipe grup yang diteliti; jelaskan karakteristik grup |
| Reliabilitas pengodean | Dua pengode bisa berbeda | Kappa antar-pengode dan penyelesaian perbedaan |
| Reliabilitas pengukuran | Metrik sensitif terhadap data hilang | Uji ketahanan dengan edge acak dihapus (misalnya 10 persen) |
| Kredibilitas kualitatif | Bias peneliti pada wawancara | Member checking, audit trail, refleksivitas |

### Keterbatasan yang diakui sejak awal

1. **Ekspor chat tidak lengkap.** Pesan yang dihapus, ditarik, atau pesan sebelum anggota bergabung tidak muncul. Edge dari kutipan balasan sering hilang.
2. **Interaksi di luar grup.** Percakapan japri dan di platform lain tidak terlihat, sehingga jaringan yang diamati adalah sebagian dari jaringan sosial yang sesungguhnya.
3. **Sentralitas bukan pengaruh.** Posisi di jaringan tidak sama dengan kekuasaan atau kepercayaan; wawancara dipakai untuk menafsirkan, bukan menyimpulkan sebab akibat.
4. **Ukuran sampel.** Jumlah grup sedikit membatasi uji statistik antar-grup; analisis berfokus pada kedalaman per grup.
5. **Efek pengamatan.** Anggota yang tahu sedang diteliti bisa berperilaku berbeda. Data historis (sebelum persetujuan) diprioritaskan jika diizinkan etik.
6. **Konteks budaya dan bahasa.** Singkatan, bahasa daerah, dan emoji mempersulit pengodean isi.

### Klaim yang tidak akan dibuat

- Tidak menyatakan hubungan sebab akibat dari data observasional.
- Tidak menyatakan siapa yang "paling berpengaruh" dalam arti tunggal.
- Tidak menggeneralisasi ke seluruh pengguna WhatsApp di Indonesia.

## Strategi publikasi Scopus Q1

Q1 tidak ditentukan oleh alatnya (NodeXL), tetapi oleh seberapa jelas naskah menjawab pertanyaan teoretis yang penting dan seberapa rapi metodenya. Strategi di bawah menjawab alasan penolakan yang paling umum untuk naskah SNA dan WhatsApp.

### Alasan penolakan yang umum dan respons

| Alasan penolakan | Respons dalam desain |
| --- | --- |
| Hanya deskriptif, tidak ada kontribusi teori | Hipotesis H1 sampai H5 dari teori struktural hole dan modal sosial; bagian diskusi kembali ke teori |
| Sampel kecil dan tidak representatif | Klaim dibatasi, uji ketahanan, dan deskripsi konteks yang rinci |
| Metode tidak bisa direplikasi | Aturan edge, validasi, versi alat, dan repositori kode tersedia |
| Masalah etika data | Persetujuan etik dan anonimisasi dijelaskan rinci di bagian metode |
| Sentralitas ditafsirkan berlebihan | Wawancara menjelaskan posisi; klaim sebab akibat dihindari |
| Hanya satu platform tanpa konteks | Sertakan konteks budaya Indonesia dan, jika mungkin, bandingkan dengan literatur platform lain |

### Pilihan artikel

1. **Artikel utama (metode campuran):** RQ1 sampai RQ5, struktur IMRaD, 7.000 sampai 9.000 kata (sesuaikan dengan batas jurnal).
2. **Artikel metodologi atau data (opsional):** protokol konversi chat ke edge list, dengan validasi dan alat bantu terbuka. Jurnal data atau metode lebih mudah menerima ini jika alatnya tersedia.

### Kelompok jurnal sasaran

Peringkat kuartil berubah tiap tahun. Verifikasi kuartil dan cakupan terbaru di Scopus (CiteScore) dan SCImago sebelum memilih; tabel di bawah hanya daftar kandidat untuk dicek, bukan jaminan Q1.

| Kelompok | Contoh jurnal untuk dicek | Cocok jika naskah menekankan |
| --- | --- | --- |
| Jaringan sosial | Social Networks | Metode dan teori jaringan |
| Komunikasi dan media baru | New Media & Society; Journal of Computer-Mediated Communication; Information, Communication & Society | Komunikasi di platform pesan |
| Media sosial dan masyarakat | Social Media + Society; Big Data & Society | Praktik sosial dan data digital |
| Sistem informasi dan teknologi | Telematics and Informatics; Computers in Human Behavior | Perilaku pengguna dan adopsi teknologi |

### Cara memilih jurnal

1. Cari 20 artikel Scopus yang paling dekat dengan topik; catat jurnal tempat artikel itu terbit.
2. Cek kuartil jurnal di kategori subjek yang relevan, dan cek apakah jurnal menerima studi kasus dengan sampel kecil.
3. Baca tiga artikel terbaru jurnal itu untuk melihat gaya, panjang, dan standar metode.
4. Pilih satu target utama dan dua cadangan; susun naskah sesuai panduan penulis target utama.

### Kualitas naskah

- Judul menyebut konsep dan konteks, bukan alat. Contoh: "Siapa yang menjembatani? Posisi struktural dan modal sosial di grup WhatsApp organisasi".
- Abstrak terstruktur dengan satu kalimat kontribusi yang jelas.
- Bagian diskusi memisahkan temuan, penafsiran, dan keterbatasan.
- Lampiran daring: kode, edge list teranonimkan (jika diizinkan), buku kode wawancara.
- Gunakan penyunting bahasa profesional untuk bahasa Inggris sebelum mengirim.

### Daftar periksa sebelum kirim

- [ ] Persetujuan etik tercantum di bagian metode.
- [ ] Hipotesis dan hasil terhubung satu per satu.
- [ ] Uji ketahanan dilaporkan di lampiran.
- [ ] Seluruh rujukan diverifikasi di Scopus atau DOI.
- [ ] Cek kemiripan (plagiarisme) dan kebijakan penggunaan alat AI jurnal sasaran.
- [ ] Surat pengantar menyatakan kebaruan dalam tiga kalimat.

## Jadwal penelitian

&#91;embedded content: jadwal penelitian · 8 tahap, 1 tonggak kirim\]

Wawancara berjalan tumpang tindih dengan akhir analisis NodeXL karena informan dipilih dari hasil analisis awal. Tanggal bersifat usulan dan perlu disesuaikan dengan kalender etik institusi.

### Tonggak dan syarat lanjut

| Tonggak | Syarat lanjut | Keluaran |
| --- | --- | --- |
| Persetujuan etik | Surat persetujuan komite etik terbit | Dokumen etik |
| Validasi edge | Kesepakatan penilai memadai dan aturan edge final | Protokol edge terverifikasi |
| Data lengkap | Seluruh grup dan persetujuan anggota terkumpul | Dataset teranonimkan |
| Wawancara jenuh | Tidak ada tema baru pada dua wawancara berturut-turut | Transkrip dan buku kode |
| Naskah final | Seluruh rujukan terverifikasi dan uji ketahanan selesai | Naskah dan lampiran |

# Bagian B: PRD alat konversi chat WhatsApp ke jaringan

## PRD: tujuan produk dan ruang lingkup

**Nama kerja produk:** WA2Net. Aplikasi web yang menerima ekspor chat WhatsApp, menganonimkan anggota, membentuk edge list dengan aturan yang bisa diatur, membantu memvalidasi edge memakai Gemini API, dan mengekspor berkas siap impor ke NodeXL. Aplikasi berjalan di Google Cloud Run.

### Masalah pengguna

Peneliti yang ingin memakai NodeXL harus mengubah teks chat menjadi tabel edge secara manual atau lewat skrip ad hoc. Prosesnya lambat, sulit direplikasi, rawan salah, dan berisiko membuka data pribadi karena anonimisasi dilakukan seadanya.

### Tujuan produk

| Tujuan | Ukuran keberhasilan |
| --- | --- |
| Mempercepat konversi chat ke edge list | Satu grup berisi puluhan ribu pesan diproses dalam hitungan menit |
| Menjamin anonimisasi konsisten | Tidak ada nama atau nomor asli di berkas keluaran |
| Membuat aturan edge transparan dan replikatif | Setiap keluaran menyertakan berkas parameter (aturan, jendela waktu, versi) |
| Mengurangi beban validasi manual | Gemini memberi usulan label; penilai manusia tetap memutuskan |
| Menjaga privasi | Data mentah tidak disimpan permanen |

### Dalam lingkup (versi 1.0)

- Unggah berkas ekspor `.txt` atau `.zip` dari WhatsApp (tanpa media).
- Parser untuk beberapa format tanggal dan jam, dengan pilihan format manual.
- Anonimisasi nama dan nomor menjadi kode, dengan tabel pemetaan yang hanya diunduh pengguna.
- Pembentukan edge dengan aturan R1 (mention), R2 (urutan balasan, jendela T), dan R3 (kutipan jika terbaca).
- Pemisahan data per periode (bulanan atau rentang tanggal kustom).
- Bantuan Gemini API untuk subsampel validasi dan klasifikasi jenis pesan (opsional, dimatikan secara bawaan).
- Ekspor `.xlsx` dengan lembar Edges dan Vertices sesuai format NodeXL, serta `.csv` dan berkas parameter.
- Pratinjau ringkas: jumlah anggota, jumlah edge, dan distribusi degree sederhana.

### Di luar lingkup (versi 1.0)

- Menjalankan metrik NodeXL (tetap di NodeXL; NodeXL adalah add-in Excel di Windows).
- Membaca gambar, suara, atau media.
- Menyimpan atau menampilkan isi pesan sebagai arsip.
- Mengakses WhatsApp secara langsung (tidak ada integrasi API WhatsApp atau scraping).
- Aplikasi seluler asli.

### Asumsi dan ketergantungan

- Pengguna memiliki hak mengekspor chat dan persetujuan etik penelitian.
- Penggunaan Gemini API mengikuti ketentuan Google dan kebijakan persetujuan peserta; hanya teks yang sudah dianonimkan yang boleh dikirim.
- Akun Google Cloud dengan penagihan aktif untuk Cloud Run dan penyimpanan sementara.
- Format ekspor WhatsApp bisa berubah antar versi aplikasi; parser perlu pembaruan berkala.

## PRD: persona dan user story

### Persona

| Persona | Latar | Kebutuhan | Hambatan |
| --- | --- | --- | --- |
| Peneliti utama | Dosen atau mahasiswa pascasarjana, paham metode tetapi tidak menulis kode | Mengubah chat jadi edge list yang bisa dipertanggungjawabkan ke reviewer | Tidak punya waktu menulis dan menguji skrip parser |
| Asisten peneliti | Mahasiswa sarjana yang menyiapkan data | Alur langkah demi langkah dengan pemeriksaan kesalahan | Format ekspor berbeda-beda per ponsel |
| Admin grup atau organisasi | Pemberi izin data | Kepastian bahwa data pribadi tidak bocor | Tidak paham detail teknis |
| Komite etik | Penilai protokol | Bukti anonimisasi dan penghapusan data | Sulit memverifikasi proses peneliti |

### User story

Prioritas memakai MoSCoW: **M** wajib versi 1.0, **S** sebaiknya ada, **C** bila waktu cukup.

| ID | Sebagai | Saya ingin | Agar | Prioritas |
| --- | --- | --- | --- | --- |
| US-01 | Peneliti | Mengunggah berkas ekspor chat | Memulai konversi tanpa menyalin manual | M |
| US-02 | Peneliti | Aplikasi mendeteksi format tanggal dan jam otomatis, dengan opsi koreksi manual | Parser tidak salah membaca pesan | M |
| US-03 | Peneliti | Semua nama dan nomor diganti kode | Data aman dibagikan ke tim | M |
| US-04 | Peneliti | Mengatur aturan edge dan jendela waktu T | Menyesuaikan dengan karakter grup dan melakukan uji sensitivitas | M |
| US-05 | Peneliti | Memecah data per periode | Membandingkan jaringan sebelum dan sesudah peristiwa | M |
| US-06 | Peneliti | Mengunduh `.xlsx` format NodeXL | Langsung impor tanpa mengubah kolom | M |
| US-07 | Peneliti | Mengunduh berkas parameter | Melaporkan metode secara replikatif | M |
| US-08 | Peneliti | Mengambil sampel acak pesan untuk validasi | Menghitung kesepakatan penilai | S |
| US-09 | Peneliti | Gemini mengusulkan target balasan dan jenis pesan pada sampel | Mempercepat validasi, dengan keputusan akhir tetap oleh manusia | S |
| US-10 | Peneliti | Menghitung precision, recall, dan kappa dari label manusia | Melaporkan validasi di naskah | S |
| US-11 | Peneliti | Memfilter anggota yang menolak persetujuan | Mematuhi hak keluar peserta | M |
| US-12 | Admin | Melihat ringkasan tanpa isi pesan | Memastikan privasi tetap terjaga | C |
| US-13 | Komite etik | Membaca ringkasan kebijakan data aplikasi | Menilai kepatuhan | C |

### Kriteria penerimaan (contoh)

- **US-03:** Setelah anonimisasi, pencarian nama asli di seluruh berkas keluaran tidak menghasilkan satu pun kecocokan, termasuk di dalam isi pesan yang disertakan (jika ada).
- **US-06:** Berkas `.xlsx` terbuka di NodeXL tanpa pesan kesalahan kolom, dan jumlah edge sama dengan jumlah baris aturan.
- **US-09:** Setiap usulan Gemini menampilkan label, tingkat keyakinan, dan tombol terima atau tolak; tidak ada usulan yang diterapkan otomatis.

## PRD: kebutuhan fungsional dalam tabel prioritas

Setiap kebutuhan diberi ID agar bisa dilacak ke user story dan pengujian.

### Modul 1: unggah dan parsing

| ID | Kebutuhan | Terkait | Prioritas |
| --- | --- | --- | --- |
| FR-01 | Menerima `.txt` dan `.zip` hingga batas ukuran yang ditetapkan, menolak berkas lain | US-01 | M |
| FR-02 | Mendeteksi pola tanggal dan jam; menampilkan 10 baris contoh untuk dikonfirmasi pengguna | US-02 | M |
| FR-03 | Memisahkan pesan multibaris dari pesan sistem (anggota masuk, keluar, ganti nama grup) | US-02 | M |
| FR-04 | Melaporkan baris yang gagal diurai beserta jumlahnya | US-02 | M |

### Modul 2: anonimisasi

| ID | Kebutuhan | Terkait | Prioritas |
| --- | --- | --- | --- |
| FR-05 | Mengganti nama pengirim dan nomor telepon dengan kode konsisten (M001 dan seterusnya) | US-03 | M |
| FR-06 | Mengganti nama yang disebut di dalam isi pesan (mention dan nama yang cocok dengan daftar anggota) | US-03 | M |
| FR-07 | Menghasilkan tabel pemetaan kode yang hanya bisa diunduh pengguna dan tidak disimpan di server | US-03 | M |
| FR-08 | Mengeluarkan semua pesan anggota dalam daftar penolakan persetujuan | US-11 | M |

### Modul 3: pembentukan edge

| ID | Kebutuhan | Terkait | Prioritas |
| --- | --- | --- | --- |
| FR-09 | Menerapkan R1 (mention), R2 (urutan balasan), dan R3 (kutipan) dengan pilihan aktif atau nonaktif | US-04 | M |
| FR-10 | Jendela waktu T dapat diatur; mode sensitivitas menjalankan beberapa nilai T sekaligus | US-04 | S |
| FR-11 | Pembobotan edge berupa jumlah interaksi, dengan tanggal interaksi pertama dan terakhir | US-04 | M |
| FR-12 | Pembagian periode per bulan, per minggu, atau rentang kustom | US-05 | M |

### Modul 4: validasi dengan Gemini API

| ID | Kebutuhan | Terkait | Prioritas |
| --- | --- | --- | --- |
| FR-13 | Mengambil sampel acak pesan (ukuran dapat diatur) beserta konteks beberapa pesan sebelumnya yang sudah dianonimkan | US-08 | S |
| FR-14 | Mengirim sampel ke Gemini API dan menerima keluaran JSON terstruktur: target balasan (kode anggota atau tidak ada), jenis pesan, tingkat keyakinan | US-09 | S |
| FR-15 | Menampilkan usulan Gemini berdampingan dengan hasil aturan; penilai manusia memberi label akhir | US-09 | S |
| FR-16 | Menghitung precision, recall, dan Cohen's kappa antara aturan dan label manusia, dan antar dua penilai | US-10 | S |
| FR-17 | Fitur Gemini dimatikan secara bawaan dan hanya aktif setelah pengguna menyetujui peringatan privasi | US-09 | M |
| FR-18 | Mencatat model, versi, parameter, dan tanggal pemanggilan di berkas parameter | US-07 | S |

### Modul 5: ekspor

| ID | Kebutuhan | Terkait | Prioritas |
| --- | --- | --- | --- |
| FR-19 | Ekspor `.xlsx` dengan lembar Edges (Vertex 1, Vertex 2, Edge Weight, atribut) dan Vertices (kode, jumlah pesan, peran) | US-06 | M |
| FR-20 | Ekspor `.csv` per periode dan satu berkas parameter berformat JSON | US-07 | M |
| FR-21 | Pratinjau statistik dasar: jumlah anggota, edge, distribusi degree | US-06 | S |
| FR-22 | Tombol hapus sesi yang menghapus semua data sementara seketika | US-12 | M |

### Penggunaan Gemini: batas dan perilaku

- Gemini dipakai sebagai **asisten pelabelan**, bukan penentu. Hasilnya tidak dimasukkan ke edge list final tanpa persetujuan penilai manusia.
- Keluaran dipaksa berformat JSON dengan skema tetap agar dapat divalidasi; jawaban yang tidak valid ditolak dan diulang maksimal tiga kali.
- Hanya teks yang sudah dianonimkan dan dipotong seperlunya yang dikirim. Metadata anggota asli tidak pernah dikirim.
- Nama model Gemini diatur lewat variabel konfigurasi, bukan ditulis tetap di kode, karena versi model berganti. Pilih model yang tersedia saat pengembangan dan catat di berkas parameter.
- Biaya dibatasi dengan batas jumlah sampel per sesi dan kuota harian.

## PRD: alur sistem dan arsitektur

&#91;embedded content: arsitektur WA2Net · Cloud Run, Cloud Storage, Secret Manager, Gemini API\]

Peneliti mengunggah ekspor chat ke layanan di Cloud Run; layanan memproses, mengekspor berkas NodeXL, dan satu-satunya komponen yang memanggil layanan luar adalah klien Gemini, yang bersifat opsional.

### Alur utama

1. Peneliti membuka aplikasi, mencentang persetujuan etik, lalu mengunggah berkas ekspor chat.
2. Layanan menyimpan berkas di Cloud Storage sementara (atau memprosesnya di memori), mengurai pesan, dan menampilkan 10 baris contoh untuk konfirmasi format.
3. Layanan menganonimkan anggota dan menyaring pesan anggota yang menolak persetujuan.
4. Peneliti memilih aturan edge dan jendela waktu T; layanan membentuk edge list per periode.
5. (Opsional) Peneliti mengaktifkan validasi Gemini. Layanan mengambil sampel acak, mengirim teks teranonimkan ke Gemini API, dan menampilkan usulan label berdampingan dengan hasil aturan.
6. Dua penilai manusia memberi label akhir; layanan menghitung precision, recall, dan kappa.
7. Peneliti mengunduh `.xlsx` NodeXL, `.csv`, dan berkas parameter, lalu mengimpornya di NodeXL pada komputer Windows.
8. Peneliti menekan Hapus sesi; semua berkas sementara dihapus.

### Pembagian tanggung jawab komponen

| Komponen | Tugas | Data yang disentuh | Penyimpanan |
| --- | --- | --- | --- |
| Cloud Run (layanan WA2Net) | Antarmuka web, parsing, anonimisasi, edge, ekspor | Chat mentah selama sesi, lalu data teranonimkan | Tanpa status; tidak menyimpan di disk instans |
| Cloud Storage | Menampung berkas unggahan dan hasil sementara | Berkas sesi | Aturan siklus hidup menghapus otomatis (misalnya setelah 24 jam) |
| Secret Manager | Menyimpan kunci API Gemini | Kunci API | Terenkripsi, akses lewat izin layanan |
| Gemini API | Mengusulkan label pada sampel | Hanya teks teranonimkan | Tidak ada penyimpanan di sisi aplikasi |
| NodeXL | Menghitung metrik graf dan komunitas | Edge list teranonimkan | Komputer peneliti |

## PRD: kebutuhan non-fungsional, Cloud Run, dan privasi

### Kebutuhan non-fungsional

| ID | Kategori | Kebutuhan | Cara uji |
| --- | --- | --- | --- |
| NFR-01 | Kinerja | Berkas ekspor \[isi: misalnya 50.000 pesan\] diproses di bawah \[isi: misalnya 2 menit\] | Uji beban dengan berkas sintetis |
| NFR-02 | Ketepatan parser | Lebih dari 99 persen baris pesan terurai benar pada format yang didukung | Uji pada kumpulan berkas ekspor dari beberapa ponsel dan bahasa |
| NFR-03 | Privasi | Tidak ada nama atau nomor asli di berkas keluaran, log, atau pesan kesalahan | Uji pencarian nama asli di semua keluaran |
| NFR-04 | Retensi | Data sesi terhapus otomatis paling lama 24 jam atau segera setelah tombol Hapus sesi | Cek aturan siklus hidup dan uji tombol |
| NFR-05 | Keamanan | Seluruh lalu lintas lewat HTTPS; akses antarlayanan memakai akun layanan dengan izin minimal | Tinjauan konfigurasi IAM |
| NFR-06 | Replikasi | Setiap keluaran menyertakan versi aplikasi, aturan, dan parameter | Cek berkas parameter |
| NFR-07 | Aksesibilitas | Antarmuka terbaca di ponsel dan laptop; teks bahasa Indonesia dan Inggris | Uji manual |
| NFR-08 | Biaya | Biaya bulanan terkendali oleh batas instans dan kuota Gemini | Pemantauan tagihan dengan anggaran dan peringatan |

### Konfigurasi Google Cloud Run

Nilai di bawah adalah titik awal yang harus disesuaikan dan dicek ke dokumentasi Google Cloud terbaru, karena batas dan harga dapat berubah.

| Aspek | Keputusan | Alasan |
| --- | --- | --- |
| Bentuk layanan | Satu kontainer (backend dan antarmuka web) | Sederhana untuk proyek penelitian |
| Wilayah | Pilih wilayah Jakarta (asia-southeast2) atau yang terdekat dengan pengguna | Latensi dan pertimbangan lokasi data |
| Skala | Minimum instans 0, maksimum kecil (misalnya \[isi\]) | Hemat biaya dan membatasi paparan |
| Konkurensi | Nilai rendah per instans karena pemrosesan memakai memori | Menghindari kehabisan memori pada berkas besar |
| Memori dan CPU | Atur dari hasil uji beban pada berkas terbesar | Parser memuat pesan ke memori |
| Batas waktu permintaan | Cukup untuk pemrosesan terlama; proses panjang dipecah per periode | Mencegah kegagalan di tengah pemrosesan |
| Ukuran unggahan | Periksa batas ukuran permintaan Cloud Run; berkas ekspor tanpa media umumnya kecil | Hindari kegagalan unggah |
| Akun layanan | Akun khusus dengan izin baca tulis ke satu bucket dan akses rahasia | Prinsip izin minimal |
| Kunci Gemini | Disimpan di Secret Manager, dimuat sebagai variabel lingkungan | Tidak ada kunci di kode atau repositori |
| Penyebaran | Kontainer dibangun dari repositori dan disebarkan lewat CI | Replikasi dan jejak versi |
| Akses | Dibatasi ke pengguna terdaftar (misalnya autentikasi akun) atau lewat tautan privat | Cegah pemakaian publik tak terkendali |

### Privasi dan Gemini API

1. **Teks yang dikirim ke Gemini hanya yang sudah dianonimkan**, dipotong ke jendela konteks minimal, dan hanya untuk sampel validasi.
2. **Persetujuan peserta harus menyebut pemrosesan oleh layanan AI pihak ketiga.** Jika persetujuan tidak mencakupnya, fitur Gemini tidak boleh dipakai pada grup itu.
3. **Periksa ketentuan data Google untuk tingkat layanan yang dipakai.** Ketentuan penggunaan data untuk peningkatan produk berbeda antara tingkat layanan gratis dan berbayar, dan Vertex AI punya kontrol data tersendiri. Pilih jalur yang sesuai dengan komite etik dan catat keputusannya.
4. **Gemini tidak menjadi sumber kebenaran.** Label manusia adalah standar emas; usulan model hanya mempercepat kerja.
5. **Catat penggunaan AI di naskah**: model, versi, tanggal, tujuan, dan bahwa keputusan akhir ada pada peneliti. Banyak jurnal Q1 mewajibkan pernyataan penggunaan alat AI.
6. **Pemantauan:** log hanya mencatat metadata teknis (ukuran, durasi, kode kesalahan), tidak pernah isi pesan.

### Contoh keluaran terstruktur dari Gemini

Skema yang diminta dari model untuk setiap pesan sampel:

```json
{
  "message_id": "string",
  "reply_target": "kode anggota atau null",
  "message_type": "pengumuman | pertanyaan | jawaban | berantai | lainnya",
  "confidence": 0.0,
  "rationale": "satu kalimat pendek tanpa mengutip nama"
}
```

Aplikasi menolak keluaran yang tidak sesuai skema dan tidak pernah menerapkan label tanpa persetujuan penilai.

## PRD: metrik keberhasilan, rilis, dan risiko

### Metrik keberhasilan

| Metrik | Target usulan | Cara ukur |
| --- | --- | --- |
| Waktu dari ekspor ke berkas NodeXL | Di bawah 15 menit per grup, termasuk konfirmasi format | Pencatatan waktu sesi oleh peneliti |
| Ketepatan edge terhadap label manusia | Precision dan recall dilaporkan; target \[isi\] pada validasi pilot | Modul validasi (FR-16) |
| Kesepakatan penilai | Cohen's kappa sebesar \[isi\] atau lebih | Modul validasi |
| Kebocoran data pribadi | Nol temuan pada uji pencarian nama asli | NFR-03 |
| Pengurangan waktu validasi manual | Lebih cepat dibanding validasi tanpa usulan Gemini | Studi waktu pada pilot |
| Keberterimaan oleh komite etik | Protokol aplikasi disetujui tanpa revisi besar | Hasil tinjauan etik |

### Rencana rilis

| Rilis | Isi | Syarat selesai |
| --- | --- | --- |
| 0.1 (prototipe) | Parser, anonimisasi, edge R1 dan R2, ekspor `.xlsx` lokal | Lolos uji pada berkas pilot |
| 0.5 (beta tertutup) | Penyebaran ke Cloud Run, penyimpanan sementara, hapus sesi | Lolos NFR-03 dan NFR-04 |
| 0.8 (validasi) | Modul sampel, validasi Gemini, perhitungan kappa | Lolos uji skema keluaran dan persetujuan penilai |
| 1.0 (penelitian) | Sensitivitas jendela waktu, berkas parameter, dokumentasi | Dipakai penuh pada pengumpulan data penelitian |
| 1.1 (terbuka) | Repositori kode, dokumentasi replikasi, contoh data sintetis | Siap dirujuk di naskah |

### Risiko dan mitigasi

| Risiko | Dampak | Kemungkinan | Mitigasi |
| --- | --- | --- | --- |
| Format ekspor WhatsApp berubah | Parser gagal | Sedang | Parser berbasis pola yang bisa dikonfigurasi, uji berkas baru tiap pembaruan |
| Anonimisasi tidak menangkap semua nama (nama panggilan, singkatan) | Kebocoran identitas | Sedang | Daftar alias yang diisi pengguna, pemeriksaan manual pada sampel |
| Persetujuan peserta tidak mencakup AI pihak ketiga | Fitur Gemini tak boleh dipakai | Sedang | Fitur dimatikan secara bawaan; protokol etik menyebutnya sejak awal |
| Biaya Cloud Run atau Gemini membengkak | Anggaran terlampaui | Rendah | Batas instans, kuota, anggaran dan peringatan tagihan |
| Usulan Gemini keliru atau bias | Validasi menyesatkan | Sedang | Label manusia sebagai standar emas; laporan kesalahan model di naskah |
| Model Gemini diganti atau dihentikan | Hasil tidak bisa direplikasi | Sedang | Catat versi model; laporkan sebagai keterbatasan; simpan label manusia |
| Reviewer meragukan heuristik edge | Naskah ditolak | Sedang | Validasi, sensitivitas, dan pelaporan terbuka |

### Pertanyaan terbuka

- Berapa grup dan anggota yang menjadi target, dan siapa yang memberi izin?
- Apakah komite etik institusi mengizinkan pemrosesan teks teranonimkan oleh layanan AI pihak ketiga?
- Siapa dua penilai manusia untuk validasi edge?
- Apakah repositori kode dan data akan dibuka untuk umum?

# Lampiran

## Lampiran A: template edge list dan vertices untuk NodeXL

Lembar **Edges** (contoh):

```csv
Vertex 1,Vertex 2,Edge Weight,Edge Type,Period,First Interaction,Last Interaction
M001,M002,14,reply,2027-02,2027-02-03,2027-02-27
M003,M001,6,mention,2027-02,2027-02-05,2027-02-24
M002,M004,3,reply,2027-03,2027-03-02,2027-03-10
```

Lembar **Vertices** (contoh):

```csv
Vertex,Role,Join Date,Message Count,Avg Words
M001,admin,2026-01-10,412,18
M002,anggota,2026-01-10,198,22
M003,pengurus,2026-02-01,260,15
M004,anggota,2026-05-20,31,12
```

## Lampiran B: perintah penyebaran ke Cloud Run (titik awal)

Sesuaikan nama proyek, wilayah, dan nama rahasia. Periksa dokumentasi `gcloud` terbaru sebelum menjalankan.

```bash
gcloud run deploy wa2net \
  --source . \
  --region asia-southeast2 \
  --no-allow-unauthenticated \
  --min-instances 0 \
  --max-instances 3 \
  --concurrency 4 \
  --set-secrets GEMINI_API_KEY=gemini-api-key:latest \
  --set-env-vars GEMINI_MODEL=<nama-model>,SESSION_TTL_HOURS=24
```

Aturan siklus hidup bucket sementara (menghapus objek setelah 1 hari) disetel terpisah di Cloud Storage. Nilai `<nama-model>` diisi dengan model Gemini yang tersedia dan dicatat di berkas parameter.

## Lampiran C: contoh instruksi untuk Gemini (sampel validasi)

Instruksi sistem yang diusulkan, dengan input hanya teks teranonimkan:

```text
Anda membantu peneliti memvalidasi hubungan balasan di grup chat yang sudah dianonimkan.
Diberikan satu pesan target dan 8 pesan sebelumnya (kode pengirim dan teks).
Tentukan: (1) kode anggota yang paling mungkin dibalas oleh pesan target, atau null jika bukan balasan;
(2) jenis pesan; (3) tingkat keyakinan 0 sampai 1.
Jangan menebak identitas asli. Jangan mengutip nama. Jawab hanya dalam JSON sesuai skema.
```

Setiap hasil dicek penilai manusia; instruksi, model, dan tanggal dicatat di berkas parameter.

## Lampiran D: kerangka formulir persetujuan peserta

1. **Judul dan peneliti:** nama studi, institusi, kontak.
2. **Tujuan:** menjelaskan pola komunikasi grup untuk keperluan penelitian.
3. **Data yang dipakai:** metadata pesan (pengirim, waktu, siapa membalas siapa); isi pesan tidak disimpan.
4. **Pemrosesan:** anonimisasi; sampel teks teranonimkan dapat diproses alat bantu AI pihak ketiga untuk validasi (centang setuju atau tidak).
5. **Penyimpanan dan penghapusan:** lokasi, jangka waktu, siapa yang bisa mengakses.
6. **Risiko dan manfaat:** kemungkinan teridentifikasi dan langkah pencegahannya.
7. **Hak:** menolak, menarik diri, dan meminta data dihapus tanpa konsekuensi.
8. **Publikasi:** hasil dilaporkan secara agregat; apakah edge list teranonimkan dibagikan.
9. **Tanda tangan atau persetujuan daring dan tanggal.**

## Lampiran E: daftar periksa etik dan data

- [ ] Persetujuan komite etik diperoleh sebelum pengumpulan data.
- [ ] Izin pimpinan atau admin grup diperoleh tertulis.
- [ ] Persetujuan seluruh anggota yang datanya dipakai dikumpulkan.
- [ ] Daftar anggota yang menolak tersedia dan dimasukkan ke aplikasi.
- [ ] Data mentah dienkripsi dan dijadwalkan untuk dihapus.
- [ ] Tabel pemetaan kode disimpan terpisah dan dijadwalkan untuk dihapus.
- [ ] Persetujuan mencakup pemrosesan AI pihak ketiga (jika Gemini dipakai).
- [ ] Pernyataan penggunaan alat AI siap untuk naskah.
- [ ] Rencana berbagi data sesuai persetujuan.

## Lampiran F: pedoman wawancara lengkap

| Topik | Pertanyaan utama | Pertanyaan pendalaman |
| --- | --- | --- |
| Peran | Ceritakan peran Anda di grup dan sejak kapan bergabung | Apa tugas tidak tertulis yang Anda lakukan? |
| Pemakaian | Informasi apa yang paling sering Anda bagikan atau cari? | Kapan terakhir kali grup ini sangat membantu? |
| Hubungan | Kepada siapa Anda biasanya bertanya, dan mengapa? | Apa yang membuat orang itu dipercaya? |
| Norma | Aturan apa yang berlaku untuk membalas atau menegur? | Siapa yang boleh menegur, dan bagaimana? |
| Verifikasi | Bagaimana Anda menilai kebenaran informasi yang diteruskan? | Pernah menemukan informasi yang salah? Apa yang Anda lakukan? |
| Keterlibatan | Apa yang membuat Anda menulis atau diam? | Situasi apa yang membuat Anda enggan menanggapi? |
| Perubahan | Apa yang berubah setelah \[isi: peristiwa\]? | Siapa yang menjadi lebih aktif atau lebih diam? |
| Penutup | Apa yang ingin Anda ubah dari cara grup berkomunikasi? | Ada hal lain yang belum saya tanyakan? |

## Lampiran G: glosarium

| Istilah | Arti |
| --- | --- |
| Node (vertex) | Anggota dalam jaringan |
| Edge | Hubungan arah dari satu anggota ke anggota lain |
| Degree | Jumlah hubungan yang dimiliki node |
| Betweenness | Seberapa sering node berada di jalur terpendek antar pasangan node lain |
| Closeness | Kedekatan rata-rata ke semua node lain |
| Eigenvector | Sentralitas yang memberi bobot lebih bagi hubungan dengan node sentral |
| Density | Proporsi hubungan yang ada dibanding yang mungkin |
| Reciprocity | Proporsi hubungan yang berbalas |
| Modularity | Ukuran kekuatan pembagian jaringan menjadi komunitas |
| Struktural hole | Celah antar kelompok yang tidak terhubung, dijembatani oleh satu atau beberapa aktor |
| Cohen's kappa | Ukuran kesepakatan dua penilai setelah menghitung kesepakatan kebetulan |
