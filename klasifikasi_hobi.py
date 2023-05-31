import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('hobi_anak.sav', 'rb'))

st.title('Prediksi Hobi Anak')
c1, c2, c3 = st.columns(3)

with c1:
    Olympiad_Participation = st.number_input('Berpartisipasi Olimpiade Sains/MTK')
    Fav_sub = st.number_input('Mata Pelajaran Favorit')
    Time_sprt = st.number_input('Waktu Untuk Bermain')
    Act_sprt = st.number_input('Mengikuti Kegiatan Olahraga')
    Time_art = st.number_input('Waktu Untuk Membuat Seni')

with c2:
    Scholarship = st.number_input('Telah Menerima Beasiswa')
    Projects = st.number_input('Menyelesaikan Projek')
    Medals = st.number_input('Memenangkan Medali')
    Fant_arts = st.number_input('Membuat Lukisan Fantasi')

with c3:
    School = st.number_input('Senang Pergi Ke Sekolah')
    Grasp_pow = st.number_input('Daya Tangkap')
    Career_sprt = st.number_input('Melanjutkan Karir Di Olahraga')
    Won_arts = st.number_input('Memenangkan Lomba Seni')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Olympiad_Participation, Scholarship, School, Fav_sub, Projects, Grasp_pow,
                               Time_sprt, Medals, Career_sprt, Act_sprt, Fant_arts, Fant_arts, Time_art]])

    if (prediksi [0] == 0):
        prediksi = ('Hobi Yang Disarankan Adalah Di Bidang Akademik')
    elif (prediksi == 1):
        prediksi = ('Hobi Yang Disarankan Adalah Di Bidang Seni')
    else:
        prediksi = ('Hobi Yang Disarankan Adalah Di Bidang Olahraga')
st.success(prediksi)