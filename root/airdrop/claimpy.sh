#!/bin/bash

# Path default
ROOT_PATH="/root/airdrop"

# Buat direktori LOG jika belum ada
mkdir -p "${ROOT_PATH}/LOG"

# Menghapus karakter '\r' dari file list_bot.txt jika ada
sed -i 's/\r$//' "${ROOT_PATH}/list_bot.txt"

# Mendapatkan menit saat ini (0-59)
current_minute=$(date +"%M")

# Jika current_minute == 0, kill all processes under "/root/airdrop/" dan hapus semua isi LOG
if [[ "$current_minute" == "00" ]]; then
  # Menghentikan semua proses yang berhubungan dengan "/root/airdrop/"
  pgrep -f "/root/airdrop/" | xargs kill
  # Tambahkan delay 5 detik untuk memastikan semua proses telah berhenti
  sleep 3
  # Menghapus semua file di dalam direktori LOG
  rm -rf ${ROOT_PATH}/LOG/*
fi

# Mendapatkan waktu saat ini dalam format HH:MM:SS
current_time=$(date +"%H:%M:%S")

# Baca file list_bot.txt baris per baris
while IFS='|' read -r line log_option intervals || [[ -n "$line" ]]; do
  # Hilangkan spasi yang tidak perlu
  line=$(echo "$line" | xargs)
  log_option=$(echo "$log_option" | xargs)
  intervals=$(echo "$intervals" | xargs)

  # Ekstrak direktori dan nama file dari setiap baris
  DIR=$(dirname "$line")
  FILE=$(basename "$line")

  # Pastikan ada ekstensi pada FILE
  if [[ "$FILE" != *.* ]]; then
    FILE="$FILE.py"
  fi
  
  # Ambil nama file tanpa ekstensi
  FILENAME="${FILE%.*}"

  # Buat path lengkap untuk log file
  LOG_FILE="${ROOT_PATH}/LOG/LOG_${FILENAME}.log"
  
  # Pisahkan intervals berdasarkan koma dan periksa setiap interval
  IFS=',' read -ra interval_array <<< "$intervals"
  for interval in "${interval_array[@]}"; do
    # Jika current_minute cocok dengan salah satu interval, jalankan script
    if [[ "$current_minute" == "$interval" ]]; then
      # Pindah ke direktori dan eksekusi script Python sesuai opsi log
      if [[ "$log_option" == "log" ]]; then
        # Tampilkan waktu dan kemudian log
        echo "run on $current_time" > "$LOG_FILE"
        (cd "${ROOT_PATH}/${DIR}" && python "${ROOT_PATH}${line}" >> "$LOG_FILE" 2>&1) &
      else
        # Jalankan tanpa menampilkan log
        (cd "${ROOT_PATH}/${DIR}" && python "${ROOT_PATH}${line}") &
      fi
    fi
  done
done < "${ROOT_PATH}/list_bot.txt"