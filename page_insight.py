import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    # Menampilkan data
    df = pd.read_csv('google_trends_data_2023-12-21_09-49-51.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    return df

df = load_data()


def show_insight():
    st.title("Trend Analysis of 2024 President Candidates in Indonesia")

    st.markdown("### **Bagaimana tren calon presiden Indonesia 2024 setiap harinya?**")

    plt.figure(figsize=(12, 7))
    sns.lineplot(data=df, x='Date', y='Trend Value', hue='Name', palette='bright')

    plt.title('Tren Calon Presiden Indonesia 2024')
    plt.xlabel('Date')
    plt.ylabel('Trend Value')
    plt.legend(title='Calon Presiden')
    plt.grid(True)
    st.pyplot(plt)

    st.write('Tampak bahwa trend Ganjar dan Prabowo mengalami lonjakan signifikan sekitar tanggal 18-23 Oktober 2023. Hal tersebut masuk akal karena sekitar tanggal tersebut para capres secara resmi mendaftarkan dirinya ke KPU sehingga masyarakat mulai mencari informasi tentang capres tersebut.')
    st.write('Trend Anies mengalami lonjakan signifikan pada tanggal 12 Desember 2023. Pada tanggal tersebut terjadi debat capres pertama. Debat capres ini menyebabkan angka pencarian Anies naik drastis.')
    st.write('Secara umum, tampak bahwa trend Anies lebih tinggi dibandingkan kedua calon presiden yang lain.')


    st.markdown("### **Bagaimana tren calon presiden Indonesia 2024 setiap bulannya?**")

    df['Month'] = df['Date'].dt.to_period('M')

    monthly_trends = df.groupby(['Name', 'Month'])['Trend Value'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=monthly_trends, x='Month', y='Trend Value', hue='Name', palette='bright')

    plt.title('Tren Calon Presiden Indonesia Setiap Bulan')
    plt.xlabel('Month')
    plt.ylabel('Trend Value')
    plt.legend(title='Calon Presiden')
    plt.grid(True)
    st.pyplot(plt)

    st.write('Tampak bahwa trend Prabowo sangat tinggi pada bulan Oktober 2023.')
    st.write('Pada bulan September, November, dan Desember, trend Anies yang paling tinggi dibandingkan capres yang lain.')
    st.write('Mayoritas trend Ganjar lebih rendah dari 2 capres lainnya.')
    st.write('Fakta menarik dari data tersebut tampak pada bulan Oktober di mana trend Prabowo menjadi sangat tinggi. Hal ini disebabkan karena pada tanggal 22 Oktober 2023, Prabowo resmi menggandeng Gibran menjadi calon wakil presidennya dan hal ini cukup mengejutkan untuk masyarakat Indonesia sehingga banyak masyarakat Indonesia mencari tahu tentang hal ini.')


    st.markdown("### **Bagaimana distribusi tren setiap calon presiden?**")

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Name', y='Trend Value', palette='bright')

    plt.title('Distribusi Tren Setiap Calon Presiden')
    plt.xlabel('Calon Presiden')
    plt.ylabel('Trend Value')
    plt.grid(True)
    st.pyplot(plt)

    st.write('Tampak bahwa trend Anies lebih tinggi dibandingkan kedua capres lainnya.')
    st.write('Median trend Prabowo dan Ganjar mirip. Yang membedakan adalah variabilitasnya. Variabilitas Ganjar jauh lebih kecil dibandingkan Prabowo dan Anies karena trend value Ganjar hanya tersebar di bawah 40 dan ada outlier di 100. Namun, trend value Prabowo dan Anies tersebar mulai dari 10-100 sehingga variabilitas trend valuenya jauh lebih tinggi.')
    st.write('Hal ini menunjukkan bahwa lonjakan trend value sering terjadi pada Prabowo dan Anies, sedangkan trend value Ganjar lebih konsisten di bawah 40.')


    st.markdown("### **Bagaimana tren kumulatif calon presiden Indonesia 2024?**")
    
    df['Cumulative Trend'] = df.groupby('Name')['Trend Value'].cumsum()

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Date', y='Cumulative Trend', hue='Name', palette='bright')

    plt.title('Tren Kumulatif Calon Presiden Indonesia 2024')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Trend Value')
    plt.legend(title='Calon Presiden')
    plt.grid(True)
    st.pyplot(plt)

    st.write('Tampak bahwa trend Ganjar yang paling stabil dan paling rendah dibandingkan kedua capres lainnya.')
    st.write('Trend Prabowo mengalami kenaikan pesat setelah resmi menggandeng Gibran sebagai calon wakil presidennya.')
    st.write('Namun, setelah debat capres perdana tanggal 12 Desember 2023, trend Anies langsung meningkat dan menyalip trend Prabowo.')
    st.write('Sampai tanggal 17 Desember 2023, secara keseluruhan trend Anies masih lebih unggul dibandingkan Ganjar dan Prabowo.')

    
    st.markdown("## **Kesimpulan**")
    st.write("- Trend Anies lebih tinggi dibandingkan kedua capres lainnya terutama setelah debat calon presiden perdana.")
    st.write("- Trend Prabowo mengalami lonjakan setelah resmi menggandeng Gibran sebagai calon wakil presidennya.")
    st.write("- Trend Ganjar paling rendah dan paling stabil dibanding Anies dan Prabowo.")