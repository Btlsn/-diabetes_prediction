import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Sayfa yapılandırması
st.set_page_config(
    page_title="Diyabet Tahmin Uygulaması",
    page_icon="🏥",
    layout="wide"
)

# CSS ile stil ekleyelim
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Başlık
st.title('🏥 Diyabet Risk Tahmin Uygulaması')
st.markdown('---')

# Model ve scaler'ı yükle
try:
    model = joblib.load('eniyi.joblib')
    scaler = joblib.load('scaler.joblib')
except:
    st.error('Model dosyaları bulunamadı! Lütfen "eniyi.joblib" ve "scaler.joblib" dosyalarının app.py ile aynı dizinde olduğundan emin olun.')
    st.stop()

# Seçenek eşleştirmeleri
secenekler = {
    'Evet': 'Yes',
    'Hayır': 'No'
}

# Ana container
with st.container():
    # İki sütunlu layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('📋 Kişisel Bilgiler')
        age = st.number_input('Yaş', min_value=18, max_value=100, value=30)  # max_value 100'e yükseltildi
        gender = st.selectbox('Cinsiyet', ['Kadın', 'Erkek'])
        bmi = st.number_input('Vücut Kitle İndeksi (BMI)', min_value=15.0, max_value=50.0, value=25.0)
        blood_sugar = st.number_input('Kan Şekeri Seviyesi (mg/dL)', min_value=70, max_value=300, value=100)  # max_value 300'e yükseltildi
        family_history = st.selectbox('Ailede Diyabet Geçmişi', ['Evet', 'Hayır'])
    
    with col2:
        st.subheader('🌟 Yaşam Tarzı Bilgileri')
        blood_pressure = st.number_input('Kan Basıncı (mmHg)', min_value=90, max_value=180, value=120)
        smoking = st.selectbox('Sigara Kullanımı', ['Evet', 'Hayır'])
        alcohol = st.selectbox('Alkol Tüketimi', ['Evet', 'Hayır'])
        sleep = st.slider('Günlük Uyku Süresi (saat)', 4.0, 10.0, 7.0, step=0.1)
        exercise = st.slider('Haftalık Egzersiz Günü', 0, 7, 3)

# Tahmin butonu
if st.button('🔍 Diyabet Riskini Hesapla'):
    # Türkçe seçenekleri İngilizce'ye çevir
    gender_eng = 'Female' if gender == 'Kadın' else 'Male'
    family_history_eng = secenekler[family_history]
    smoking_eng = secenekler[smoking]
    alcohol_eng = secenekler[alcohol]
    
    # Kullanıcı verilerini DataFrame'e dönüştür
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender_eng],
        'BMI': [bmi],
        'Blood_Sugar_Level': [blood_sugar],
        'Family_History': [family_history_eng],
        'Blood_Pressure': [blood_pressure],
        'Smoking': [smoking_eng],
        'Alcohol_Consumption': [alcohol_eng],
        'Sleep_Duration': [sleep],
        'Exercise_Frequency': [exercise]
    })
    
    # Kategorik değişkenleri dönüştür
    input_data = pd.get_dummies(input_data)
    
    # Eksik sütunları ekle
    required_columns = scaler.feature_names_in_
    for col in required_columns:
        if col not in input_data.columns:
            input_data[col] = 0
    
    # Sütunları doğru sıraya koy
    input_data = input_data[required_columns]
    
    # Verileri ölçeklendir
    input_scaled = scaler.transform(input_data)
    
    # Tahmin yap
    prediction = model.predict(input_scaled)[0]
    
    # Sonuç gösterimi
    st.markdown('---')
    st.subheader('🔍 Tahmin Sonucu')
    
    if prediction == 1:
        st.error('⚠️ DİYABET RİSKİ TESPİT EDİLDİ!')
        
        st.markdown("""
        ### 📋 Öneriler:
        * Acilen bir sağlık kuruluşuna başvurun
        * Beslenme alışkanlıklarınızı gözden geçirin
        * Düzenli egzersiz yapmaya başlayın
        * Düzenli kan şekeri takibi yapın
        * Yaşam tarzı değişikliklerine önem verin
        """)
    else:
        st.success('✅ DİYABET RİSKİ TESPİT EDİLMEDİ')
        
        st.markdown("""
        ### 📋 Öneriler:
        * Sağlıklı yaşam tarzınızı sürdürün
        * Düzenli check-up yaptırın
        * Dengeli beslenmeye devam edin
        * Fiziksel aktivitenizi koruyun
        * Yıllık sağlık kontrollerinizi ihmal etmeyin
        """)

# Sayfa altı bilgilendirme
st.markdown('---')
st.markdown("""
    <div style='text-align: center'>
        <p style='color: gray; font-size: 14px;'>
            ⚠️ Bu uygulama sadece bir tahmin aracıdır ve kesin tanı koyamaz. 
            Sağlık durumunuzla ilgili endişeleriniz varsa mutlaka bir sağlık uzmanına başvurunuz.
        </p>
    </div>
""", unsafe_allow_html=True)
