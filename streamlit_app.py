import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan data
model = joblib.load("dropout_model.pkl")
data = pd.read_csv("data_cleaned.csv")

st.title("🎓 Prediksi Mahasiswa Dropout")
st.markdown("Masukkan informasi mahasiswa untuk memprediksi kemungkinan dropout.")

age = st.number_input("Usia saat masuk", min_value=15, max_value=70, value=20)
grade_1st = st.number_input("Nilai rata-rata semester 1", min_value=0.0, max_value=20.0, value=10.0)
grade_2nd = st.number_input("Nilai rata-rata semester 2", min_value=0.0, max_value=20.0, value=10.0)
approved_1st = st.number_input("Jumlah MK lulus semester 1", min_value=0, max_value=20, value=5)
approved_2nd = st.number_input("Jumlah MK lulus semester 2", min_value=0, max_value=20, value=5)
tuition_paid = st.selectbox("SPP dibayar lunas?", ("Yes", "No"))
scholarship = st.selectbox("Penerima beasiswa?", ("Yes", "No"))
debtor = st.selectbox("Memiliki utang pendidikan?", ("Yes", "No"))
evening = st.selectbox("Program kelas?", ("Siang", "Malam"))

# Mapping input ke format model
input_data = pd.DataFrame([{
    "Age_at_enrollment": age,
    "Curricular_units_1st_sem_grade": grade_1st,
    "Curricular_units_2nd_sem_grade": grade_2nd,
    "Curricular_units_1st_sem_approved": approved_1st,
    "Curricular_units_2nd_sem_approved": approved_2nd,
    "Tuition_fees_up_to_date": 1 if tuition_paid == "Yes" else 0,
    "Scholarship_holder": 1 if scholarship == "Yes" else 0,
    "Debtor": 1 if debtor == "Yes" else 0,
    "Daytime_evening_attendance": 0 if evening == "Siang" else 1
}])

# Prediksi
if st.button("Prediksi Dropout"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction]

    if prediction == 1:
        st.error(f"⚠️ Mahasiswa berpotensi **Dropout** dengan probabilitas {probability:.2%}")
    else:
        st.success(f"✅ Mahasiswa **Tidak Dropout** dengan probabilitas {probability:.2%}")

# Tampilkan data sample
with st.expander("🔍 Lihat 5 contoh data"):
    st.dataframe(data.head())

