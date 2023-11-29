import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from streamlit_autorefresh import st_autorefresh


# Load data
daily_sentiment = pd.read_csv('./data/daily_sentiment.csv')
daily_sentiment['time'] = pd.to_datetime(daily_sentiment['time'])
daily_sentiment = daily_sentiment.set_index('time')
df_positive = pd.read_csv('./data/positive_reviews.csv')
df_negative = pd.read_csv('./data/negative_reviews.csv')

# Set up page
st.set_page_config(layout="wide", page_title='My Time at Sandrock Dashboard', page_icon='icon sandrock.png')
st_autorefresh(interval=5000, key=5)

# Judul
st.markdown("<h1 style='text-align: center; color: black;'>Business Intelligence Dashboard for <span style='color:green'> My Time at Sandrock </span></h1>", unsafe_allow_html=True)


# nampilin daily sentiment plot
with st.container():
    st.markdown("<h2 style='text-align: center; color: black;'>Jumlah Player dan Rasio Sentimen Harian</h2>", unsafe_allow_html=True)
    # Tanggal release date
    release_date = pd.to_datetime('2023-11-02')

    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(daily_sentiment.index, daily_sentiment['sentiment_ratio'], marker='x')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sentiment Ratio')

    # Menggabungkan sumbu y
    ax2 = ax.twinx()
    ax2.plot(daily_sentiment.index, daily_sentiment['Players'], color='orange', marker='o')
    ax2.set_ylabel('Players')
    
    # menambahkan legenda untuk kedua plot (tolong jadikan satu legenda)
    
    # Menambahkan garis vertikal untuk tanggal rilis
    ax.axvline(release_date, color='red', linestyle='--')
    # tambahkan keterangan tanggal rilis
    ax.text(release_date, 0.72, 'Release Date', rotation=0, horizontalalignment='right', verticalalignment='bottom', weight='bold', fontsize=8, color='red',bbox=dict(facecolor='white', alpha=0.5, edgecolor='red', boxstyle='round'))

    # Adding legend
    ax.legend(['Sentiment Ratio'], loc='upper right')
    ax2.legend(['Players'], loc='lower right')
    st.pyplot(fig)

    with st.expander("**Show Analysis**"):
        st.markdown("""
        - **Sebelum tanggal rilis** (yang ditandai oleh garis putus-putus merah), rasio dari sentimen cukup stabil, menandakan bahwa ulasan dari para pemain yang merasakan game ini pada masa ini cenderung positif.
        \n- Kemudian pada saat game tersebut **baru rilis**, terjadi **peningkatan yang signifikan dalam jumlah pemain**, hal yang dapat kita perkirakan bahwa banyak pemain yang sangat antusias dalam menunggu perilisan dari game ini.
                    Hal tersebut bisa disebabkan karena mereka menjadi tertarik setelah melihat trailer dari game ini atau dengan membaca ulasan dari para pemain yang sudah memainkan game ini sebelum perilisan.
        \n- Seiring berjalannya waktu, terjadi **penurunan jumlah pemain yang cukup signifikan**, yang dapat diperkirakan bahwa banyak pemain yang merasa kecewa dengan game ini. Hal tersebut dapat disebabkan oleh beberapa hal, seperti **banyak bug yang terjadi**, **performa game yang kurang optimal**, atau **masalah teknis lainnya**.
        \nUntuk mengetahui penyebabnya, kita akan melakukan analisis lebih lanjut dari ulasan yang diberikan oleh para pemain.                   
        """)

# nampilin analisis wordcloud untuk setiap sentiment
with st.container():
    st.markdown("<h2 style='text-align: center; color: black;'>Analisis Ulasan untuk Setiap Label Sentimen</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([0.5, 0.5])

    # col 1 for positive sentiment
    with col1:
        st.markdown("<h3 style='text-align: center'>Inspeksi Data Ulasan Positif</h3>", unsafe_allow_html=True)
        st.write(df_positive.loc[:, ['time', 'review', ]])

        st.markdown("<h3 style='text-align: center'>Wordcloud Sentimen Positif</h3>", unsafe_allow_html=True)
        st.image('wordcloud_positive.png', use_column_width=True)

        with st.expander("Aspek Positif yang Disoroti oleh Pemain"):
            st.markdown("""
            - **Gameplay Dinamis dan Menarik** :
                    Para pemain merasa bahwa kompleksitas dan kekayaan dari activity yang disediakan oleh pengembang "My Time at Sandrock" sangatlah menarik, 
                        mereka sangat menghargai fitur yang diciptakan oleh pengembang. Kata-kata seperti "crafting", "Building", "Farming", dan "Exploration" yang muncul secara menonjol
                        mengindikasikan bahwa game ini berhasil dalam memberikan pengalaman yang imersif dan interaktif bagi para pemainnya. Mereka diberikan dunianya sendiri, sehingga
                        mereka memiliki kebebasan untuk mengeksplorasi berbagai hal yang ada di dalam dunia tersebut.
            \n- **Keindahan Cerita dan Keunikan Karakter** : 
                        Terdapat apresiasi yang tinggi dari para pemain terhadap aspek cerita dan pendalaman karakter yang ada di game ini. Hal tersebut dicerminkan oleh
                        kata-kata seperti "Story", "NPC", "Character", "Romance Option". Pemain merasa terhubung dengan kisah yang diceritakan oleh game ini dan juga karakter
                        yang mereka jumpai.
            """)
        
        with st.expander("Elemen Pendorong Kepuasan Pemain"):
            st.markdown("""
            - **Pengalaman Bermain yang Menyenangkan** : Kata-kata seperti "Fun", "Enjoy", dan "Chill" yang dominan, menandakan bahwa game ini memberikan pengalaman bermain yang menyenangkan bagi para pemainnya.
                Hal ini mengindikasikan bahwa "My Time at Sandrock" dianggap sebagai sumber hiburan yang dapat diandalkan, menyediakan tempat yang sempurna bagi para pemainnya untuk
                        relaksasi dan menyediakan pelarian yang menyenangkan dari realitas. Istilah seperti "Relaxing" dan "Cozy" secara khusus menegaskan bahwa game ini dianggap sebagai
                        cara bagi para pemain untuk beristirahat dan mengisi waktu luang dengan kegiatan yang dapat memuaskan secara emosional.
            \n- **Kualitas Visual yang Memukau** : Visual dari game tersebut juga mendapatkan pujian, dengan munculnya kata "Graphic" dan "Art" yang mencolok, menunjukkan bahwa para pemain
                        menghargai kualitas grafik dan keindahan estetika yang disajikan oleh game ini. Hal ini mencerminkan betapa pentingnya desain visual yang baik dan bagaimana itu dapat
                        meningkatkan pengalaman bermain secara keseluruhan.
            \n - **Referensi Positif dan Komparasi dengan Game Lain**: Referensi terhadap game lain, seperti "Stardew Valley", "Portia" (game yang dikembangkan sebelumnya oleh Pathea Games), dan 
                        "Harvest Moon" mencerminkan pengakuan dan pujian dalam konteks genre game yang sama. Pemain membandingkan "My Time at Sandrock" 
                        dengan game serupa dan menemukan bahwa game ini memenuhi harapan mereka yang telah dibangun oleh game terkenal lainnya dalam genre yang sama.                    
                        """)
        
        st.markdown("<h3 style='text-align: center'>Topic Modelling dan Ringkasan untuk Sentimen Positif</h3>", unsafe_allow_html=True)


        st.write("Dari keseluruhan ulasan positif yang diberikan oleh para pemain, kami menggunakan topic modelling dengan LDA untuk mendapatkan 5 topik utama yang muncul dari ulasan tersebut. Topik tersebut dapat menjadi ide untuk pengembangan fitur game lebih lanjut. Berikut ini adalah 5 topik yang dihasilkan dari pemodelan menggunakan LDA :")
        st.latex(r'''
                 \begin{align*}
                 \text{Topic 1} & = \text{game feel character sandrock story time portia combat quest play} \\
                 \text{Topic 2} & = \text{game play time story character multiplayer hour sandrock player fun} \\
                 \text{Topic 3} & = \text{game character time love lot play story sandrock life event} \\
                 \text{Topic 4} & = \text{game portia time time portia fun love sandrock lot enjoy story} \\
                 \text{Topic 5} & = \text{game time character story feel lot portia commission item play} \\
                 \end{align*}
                 ''')
        st.write("Kemudian, kami menggunakan topic text yang dihasilkan dari LDA untuk membuat ringkasan dari setiap topik yang muncul. Berikut adalah ringkasan dari setiap topik yang muncul :")
        with st.expander("Ringkasan Topik 1, Pengalaman dan Narasi yang Menarik "):
            st.markdown(""" 
                        Para pemain menyoroti elemen gameplay yang menarik, seperti "farming" dan "building". Mereka menikmati
                        proses membangun, mengumpulkan sumber daya, dan menyelesaikan quest utama yang memberikan hadiah dan membuka kisah pribadi dari karakter lain.
                        
                        """)
        with st.expander("Ringkasan Topik 2, Eksplorasi dan Interaktivitas"):
            st.markdown(""" 
                        Game ini sering dibandingkan dengan 'Stardew Valley' dan 'Minecraft', dimana pemain dapat memilih pekerjaan, bertemu karakter baru,
                        dan membangun rumah mereka. Mereka menikmati kebebasan untuk menjelajahi dan mengambil tugas seperti perburuan harta karun dan dungeon raiding, yang semuanya memberikan pengalaman
                        yang menyenangkan dan menarik.
                        """)
        with st.expander("Ringkasan Topik 3, Kehidupan dan Komunitas dalam Game"):
            st.markdown(""" 
                        Pemain mengapresiasi peningkatan kualitas dan penambahan mode multiplayer jika dibandingkan dengan game sebelumnya, Portia. NPC yang lebih hidup
                        dengan cerita yang lebih mendalam memberikan pengalaman baru pada game. Mereka merasa bahwa 'Sandrock' berdiri sendiri sebagai judul yang kuat
                        dalam seri ini, dengan menawarkan sistem crafting, farming, romansa, dan pertarungan yang lebih baik.
                        """)
        with st.expander("Ringkasan Topik 4, Keseruan dalam Bermain"):
            st.markdown("""
                        'Sandrock' dipuji sebagai penghilang waktu yang menyenangkan dan membangun game yang menarik. Para pemain menemukan cerita yang menarik dan gameplay
                        yang menyenangkan meskipun terkadang terasa berulang (looping). Game ini dianggap sebagai hadiah ulang tahun yang indah bagi penggemar, dengan banyak pemain yang berkomitmen
                        untuk mengurangi kualitas grafis demi memainkannya tanpa hambatan internet, ini menunjukkan kesetiaan penggemar terhadap pengalaman yang ditawarkan.

            """)

        with st.expander("Ringkasan Topik 5, Permainan dan Kualitas"):
            st.markdown("""
                        Dalam topik ini, pemain mencatat gameplay yang menarik, sehingga membuat mereka tetap bermain. Grafis yang sederhana dan cocok untuk jenis game ini
                    
                        serta perbaikan dari seri sebelumnya, Portia, termasuk perbaikan dalam pertarungan dan peningkatan kualitas dari fitur lainnya yang patut diapresiasi.
                        Pemain berpengalaman yang sering berpindah dari satu game ke game lain menemukan bahwa 'Sandrock' cukup menarik untuk membuat mereka bermain selama berjam-jam.
                        """)
    
    # col 2 for negative sentiment
    with col2:

        st.markdown("<h3 style='text-align: center'>Inspeksi Data Ulasan Negatif</h3>", unsafe_allow_html=True)
        st.write(df_negative.loc[:, ['time', 'review', ]], use_width_container=True)


        st.markdown("<h3 style='text-align: center'>Wordcloud Sentimen Negatif</h3>", unsafe_allow_html=True)
        st.image('wordcloud_negative.png', use_column_width=True)

        with st.expander("Area untuk Perbaikan dan Pengembangan"):
            st.markdown("""
            - **Masalah Teknis** : Kata-kata seperti "Bug", "Crashes", dan "Loading yang menonjol sebagai isu utama yang memberikan pengaruh negatif terhadap
                         pengalaman bermain yang buruk. Kata-kata ini dapat menggambarkan bahwa para pemain sering mengalami gangguan teknis yang dapat mengganggu imersi dan kelancaran bermain.
            \n- **Optimasi Gameplay** : Hal ini diperlukan karena adanya kata "Grinding" dan "Stuck" yang muncul, menunjukkan bahwa beberapa aspek
                        dari mekanisme game mungkin terlalu berulang yang dapat memicu rasa bosan dalam bermain. 
            \n- **Isu UI/UX** : Isu tersebut muncul dalam bentuk kata-kata seperti "Marker" dan "Menu" yang mungkin menujukkan bahwa navigasi dalam game
                        atau antarmuka pengguna yang memerlukan peningkatan intuitif. 
            """)

        st.write("Dari keseluruhan ulasan negatif yang diberikan oleh para pemain, kami menggunakan topic modelling dengan LDA untuk mendapatkan 5 topik utama yang muncul dari ulasan tersebut. Topik tersebut dapat menjadi ide untuk evaluasi terhadap game oleh developer. Berikut ini adalah 5 topik yang dihasilkan dari pemodelan menggunakan LDA :")
        st.latex(r'''
                 \begin{align*}
                 \text{Topic 1} & = \text{game time day bug teleport play workshop bad quest mtap} \\
                 \text{Topic 2} & = \text{game play issue fun release time loading wait access load} \\
                 \text{Topic 3} & = \text{game portia time bug story hour time portia progress main play} \\
                 \text{Topic 4} & = \text{game multiplayer sandrock dev npc content player story update miss} \\
                 \text{Topic 5} & = \text{feel game quest character time town lot location complete design} \\
                 \end{align*}
                 ''')
        
        # summarize
        st.write("Kemudian, kami menggunakan topic text yang dihasilkan dari LDA untuk membuat ringkasan dari setiap topik yang muncul. Berikut adalah ringkasan dari setiap topik yang muncul :")
        with st.expander("Ringkasan Topik 1, Masalah Teknis dan Pengalaman Bermain "):
            st.markdown(""" 
                        Pemain mengalami masalah teknis yang berulang, termasuk bug, crash dalam gameplay yang memengaruhi transisi adegan dan saat memulai game. 
                        Dengan lebih dari 90 jam gameplay yang didapat, masalah seperti ini menjadi sangat menonjol, menunjukkan perlunya peningkatan dalam stabilitas dan pengujian game secara lebih lanjut.
                        """)
        with st.expander("Ringkasan Topik 2, Bug dan Masalah Progress"):
            st.markdown("""
                        Pemain sering menghadapi bug yang mengganggu progress mereka dalam game, terutama yang berkaitan dengan cerita utama
                        yang dapat menyebabkan kehilangan jam bermain dan kemajuan dalam game. Hal ini menunjukkan bahwa developer perlu untuk memberi perhatian lebih
                        terhadap pengalaman bermain setelah rilis game dengan update yang lebih sering untuk mengatasi masalah tersebut.
            """)
        with st.expander("Ringkasan Topik 3, Keterbatasan Multiplayer dan Masalah Pemuatan"):
            st.markdown(""" 
                        Ulasan yang ada menyoroti kekecewaan terhadap fitur multiplayer yang terbatas dan waktu pemuatan yang lama. Hal ini mengurangi kepuasan pemain.
                        Meskipun game ini dianggap menyenangkan, masalah teknis dan pembatasan konten multiplayer membatasi rekomendasi pemain untuk game ini.
                        yang menyenangkan dan menarik.
                        """)
        with st.expander("Ringkasan Topik 4, Komitmen dan Kepercayaan Developer"):
            st.markdown(""" 
                        Ada rasa frustrasi terhadap sesuatu yang dipandang sebagai janji yang tidak ditepati oleh developer, terutama dalam hal konten multiplayer yang dijanjikan.
                        Komunitas merasa dikhianati karena perubahan arah secara mendadak yang tidak diharapkan dan tidak adanya kesempatan untuk pengembalian dana, yang menimbulkan 
                        pertanyaan tentang integritas dan komunikasi developer.
                        """)

        with st.expander("Ringkasan Topik 5, Desain dan Mekanisme Game"):
            st.markdown("""
                        Terdapat kekecewaan terhadap elemen desain tertentu seperti pertarungan dan eksplorasi, pemain merasa bahwa developer kurang inovatif dan cenderung
                        mengulang hal yang sama dengan game sebelumnya. Diperlukan adanya pendekatan yang lebih kreatif dan inovatif terhadap detail desain yang berguna untuk memperbaiki
                        pengalaman bermain secara keseluruhan.
                        """)
