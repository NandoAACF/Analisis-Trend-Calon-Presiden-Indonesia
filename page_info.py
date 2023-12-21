import streamlit as st
import pandas as pd

def show_info():
    st.title('Data Information')

    st.image('images/google_trends.jpg', width=400)
    st.write('Data yang digunakan adalah data yang diambil dari Google Trends mulai tanggal 21 September 2023 sampai 17 Desember 2023.')
    st.write('Data ini berisi tentang trend pencarian 3 calon presiden Indonesia 2024, yaitu Ganjar Pranowo, Anies Baswedan, dan Prabowo Subianto.')

    st.image('images/apify.png')
    st.write('Scraping Google Trends menggunakan Python dengan library apify-client dengan input keyword "Ganjar", "Anies", dan "Prabowo" yang menghasilkan output berupa timestamp dan trend valuenya.')
    st.write('Hasil scraping disimpan dalam bentuk file csv untuk divisualisasikan dan dianalisis insight-nya.')

    st.markdown('## **Thank You 😀**')