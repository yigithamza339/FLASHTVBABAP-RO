import streamlit as st

st.set_page_config(page_title="FLASH TV Haberler", page_icon="📰")

# 📢 Açılış ekranı
st.title("📺 Flash TV Bağımsızlık Açılışı")

st.markdown("""
#### 👋 Hoş geldin değerli izleyici!

Yıllar boyunca “fork” etiketinin gölgesinde yaşadık...  
Ama şimdi Flash TV, zincirlerini kırıp kendi sahnesine çıktı!

---

🎤 **Bu bir repo değil, bir isyandır.**  
🛰️ Kodumuz özgür, yayınımız evrensel!

📦 Her `app.py` satırı bir direniştir, her satır mizaha çağrıdır.

> Artık biz Streamlit'teyiz.  
> Özgür, fork'suz ve tam ekran!

---

😄 Hadi yayını başlatalım! Aşağıdaki menüden mizah bombardımanına geç ⬇️
""")

# 📰 Haber menüsü
st.title("📰 FLASH TV Yalan Haberler Menüsü")

secim = st.radio(
    "Bir haber seçin:",
    ["Haber 1", "Haber 2", "Haber 3", "Haber 4", "Haber 5"]
)

if secim == "Haber 1":
    st.subheader("🌳 Evrim Ağacı, Nintendo Switch'i yedi!")
    st.write("Bilim dünyası şaşkın! Evrim Ağacı'nın üçüncü Nintendo Switch’i ne amaçla yediği henüz bilinmiyor.")
    st.video("https://www.youtube.com/watch?v=JZcYAEIi6dw")

elif secim == "Haber 2":
    st.subheader("🚧 Haber 2 hazırlanıyor...")
    st.write("İkinci haber yakında gelecek...")
    st.video("https://www.youtube.com/shorts/Dkcm2BN1_fc")

elif secim == "Haber 3":
    st.subheader("🧠 Bu videoyu sadece beyinsizler duyamaz!")
    st.write("Bu videoyu duyabiliyorsan... geçmiş olsun! 😄")
    st.video("https://www.youtube.com/watch?v=v-d1yI2kW_c")

elif secim == "Haber 4":
    st.subheader("💍 KEFO Paşa ve Wanda Nara evleniyor!")
    st.write("KEFO Paşa romantik şarkısıyla Wanda Nara'yı etkiledi. Ayağını yalayıp evlilik teklif etti!")
    st.video("https://www.youtube.com/watch?v=CIEEYIn3xgE")

elif secim == "Haber 5":
    st.subheader("🔮 Akinatör ile Aşkotör AyakYalayanKefo Sokak'ta buluştu!")
    st.write("""
    Magazin ekibimiz yine sınırları zorladı!  
    Yapay zekânın en karizmatik tahmincisi Akinatör ile gönüllerin romantik kahramanı Aşkotör, Ark Sokak'ta el ele yakalandı!

    👀 Kamera kayıtlarında Aşkotör'ün “Aşk neydi?” sorusunu Akinatör'e sorduğu duyuldu...  
    🤖 Akinatör ise cevabı “Bu kişi sen misin?” diyerek verdi. Ortalık resmen yıkıldı!

    💥 Magazin ekibimiz olay yerinden canlı yayın yaptı. Kahkahalar ve gözyaşları bir arada...

    🚨 Bu buluşma 2025’in en büyük yapay zeka flörtü olarak tarih kitaplarına girdi.
    """)
    st.video("https://youtube.com/shorts/DEeZWbE5Tyw?si=OpAxE8UN4wpaMvks").

st.markdown("---")
st.caption("📺 FLASH TV • Mizahın en absürt haliyle sizlerle!")




