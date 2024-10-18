#!/bin/bash

# Path default
ROOT_PATH="/root/airdrop"

# Buat direktori LOG jika belum ada
mkdir -p "${ROOT_PATH}/LOG"

# Menghapus karakter '\r' dari file list_bot.txt jika ada
sed -i 's/\r$//' "${ROOT_PATH}/list_bot.txt"

# Baca file list_bot.txt baris per baris
while IFS= read -r line || [[ -n "$line" ]]; do
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
  
  # Pindah ke direktori dan eksekusi script Python, arahkan output ke log file
  cd "${ROOT_PATH}/${DIR}" && python "${ROOT_PATH}${line}" > "$LOG_FILE" 2>&1 &
done < "${ROOT_PATH}/list_bot.txt"
