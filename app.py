import streamlit as st

# Judul & Deskripsi Aplikasi
st.title("🔮 Mini Quiz Tebak Kepribadian")
st.write("Jawab pertanyaan berikut untuk mengetahui kepribadianmu (Pendiam, Pemarah, Pemalu, atau Netral).")

# --- Gambar Logo (opsional, bisa diganti dengan file logo.png di foldermu) ---
st.image(
    "berfikir.png",
    caption="Mini Quiz App",
    width=200
)

# --- Pertanyaan & Jawaban ---
questions = {
    "Apa yang biasanya kamu lakukan saat ada acara ramai?": {
        "Tetap diam dan mengamati": "pendiam",
        "Cepat tersulut emosi kalau ada yang mengganggu": "pemarah",
        "Malu untuk banyak bicara": "pemalu",
        "Ikut biasa saja, netral": "netral"
    },
    "Bagaimana responmu saat diminta presentasi di depan umum?": {
        "Lebih suka diam & menghindar": "pendiam",
        "Kesal & tidak suka dipaksa": "pemarah",
        "Gugup & malu-malu": "pemalu",
        "Santai & lakukan seperlunya": "netral"
    },
    "Kalau ada masalah dengan teman, apa yang biasanya kamu lakukan?": {
        "Lebih memilih diam & memendam": "pendiam",
        "Langsung marah & melawan": "pemarah",
        "Takut & menghindar bicara": "pemalu",
        "Biasa saja, coba netralisir": "netral"
    }
}

# --- Skor ---
scores = {"pendiam": 0, "pemarah": 0, "pemalu": 0, "netral": 0}

# --- Jawaban Pengguna ---
st.subheader("📝 Pertanyaan")
for q, options in questions.items():
    answer = st.radio(q, list(options.keys()))
    if answer:
        scores[options[answer]] += 1

# --- Tombol Hasil ---
if st.button("🔎 Lihat Hasil"):
    result = max(scores, key=scores.get)

    st.subheader("📊 Hasil Kuis")
    if result == "pendiam":
        st.success("Kamu cenderung **Pendiam** 🧘‍♂️. Lebih suka tenang, mengamati, dan menjaga diri.")
        st.image("pendiam.png", width=150)
    elif result == "pemarah":
        st.error("Kamu cenderung **Pemarah** 😡. Cepat bereaksi & emosional.")
        st.image("pemarah.png", width=150)
    elif result == "pemalu":
        st.warning("Kamu cenderung **Pemalu** 🙈. Sering gugup dan lebih nyaman di belakang layar.")
        st.image("malu.png", width=150)
    else:
        st.info("Kamu cenderung **Netral** 🙂. Santai, fleksibel, dan mudah beradaptasi.")
        st.image("netral.png", width=150)

    # Menampilkan skor detail
    st.write("### 📌 Skor Detail:")
    st.write(scores)
