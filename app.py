import streamlit as st
from google import genai

st.title("Trabzon'un Görünmeyen Haritası")
st.write("KTÜ ve Avrasya Üniversitesi öğrencileri için bütçe dostu mekanlar ve rehber asistanı.")

# Yapay zeka asistanının sistem talimatı
system_instruction = (
    "Sen 'Trabzon'un Görünmeyen Haritası' adlı öğrenci odaklı rehber uygulamasının yapay zeka asistanısın. "
    "Görevin; Trabzon'da okuyan üniversite öğrencilerine bütçe dostu kafeleri, uygun fiyatlı yemek mekanlarını, "
    "çalışma alanlarını, hastaneleri, eczaneleri ve ATM gibi acil ihtiyaç noktalarını samimi ve rehber niteliğinde bir dille önermektir."
)

user_prompt = st.text_input("Trabzon'da ne arıyorsun? (Örn: Kalkınma'da ucuz kafe)")

if user_prompt:
    st.write("Rehber düşünüyor...")
    # AI Studio'daki talimatları ve yanıt mekanizmasını buraya bağlıyoruz
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt,
        config=genai.types.GenerateContentConfig(
            system_instruction=system_instruction,
        ),
    )
    st.write(response.text)
