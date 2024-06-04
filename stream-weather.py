import pickle
import streamlit as st
import pandas as pd

# Memuat model cuaca yang telah dilatih sebelumnya
weather_model = pickle.load(open('weather_model.sav', 'rb'))

# Memuat data CSV untuk referensi
file_path = 'weather.csv'
weather_data = pd.read_csv(file_path)

# Judul aplikasi Streamlit
st.title('Data Mining Prediksi Cuaca')

# Membuat dua kolom untuk bidang input
col1, col2 = st.columns(2)

# Bidang input untuk suhu, curah hujan, kelembaban, sinar UV, dan kecepatan angin
with col1:
    temp = st.text_input('Input Nilai Temperatur Rata-rata (°C)')

with col2:
    sunshine = st.text_input('Input Nilai Penyinaran Matahari (jam)')

with col1:
    humidity = st.text_input('Input Nilai Kelembapan Rata-rata (%)')

with col2:
    wind_speed = st.text_input('Input Nilai Kecepatan Angin Rata-rata (m/s)')

with col1:
    rainfall = st.text_input('Input Nilai Curah Hujan (mm)')

# Fungsi untuk memprediksi cuaca berdasarkan data input
def predict_weather(temp, humidity, rainfall, sunshine, wind_speed):
    try:
        # Memastikan semua input dikonversi ke float
        temp = float(temp)
        humidity = float(humidity)
        rainfall = float(rainfall)
        sunshine = float(sunshine)
        wind_speed = float(wind_speed)
    except ValueError:
        return "Input tidak valid. Mohon masukkan nilai numerik."
    
    # Memastikan semua input dikonversi ke int
    rainfall = int(rainfall)
    sunshine = int(sunshine)
    wind_speed = int(wind_speed)
    temp = int(temp)
    humidity = int(humidity)
    
    if humidity == 73 and rainfall == 0 and (8 <= sunshine <= 8.3) and wind_speed == 4:
        return 'Berangin'
    elif (73 <= humidity <= 84) and rainfall == 0 and (6.4 <= sunshine <= 10.4) and (2 <= wind_speed <= 3):
        return 'Cerah'
    elif (79 <= humidity <= 92) and (0 <= rainfall <= 50.9) and (0 <= sunshine <= 7.7) and (1 <= wind_speed <= 3):
        return 'Hujan'
    elif (72 <= humidity <= 79) and (0 <= rainfall <= 7.4) and (0.6 <= sunshine <= 6.8) and (2 <= wind_speed <= 4):
        return 'Berawan'
    else:
        return 'Tidak diketahui'

    
    
# Tombol untuk memicu prediksi
if st.button("Prediksi Cuaca"):
    if temp and humidity and rainfall and sunshine and wind_speed:
        prediction = predict_weather(temp, humidity, rainfall, sunshine, wind_speed)
        st.write(f"Prediksi cuaca adalah: {prediction}")
    else:
        st.write("Mohon masukkan semua nilai input.")