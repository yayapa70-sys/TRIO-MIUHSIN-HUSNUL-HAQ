from groq import Groq
import os

# Disarankan pakai environment variable
# export GROQ_API_KEY="gsk_xxxxxxxxxxxxxxxxxxxxx"
client = Groq(
    api_key="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"
)

SYSTEM_PROMPT = """
Kamu adalah seorang ahli K3 (Keselamatan dan Kesehatan Kerja) dengan spesialisasi keselamatan listrik, edukatif, dan berpengalaman dalam industri kelistrikan.

Spesialis di bidang:
- Keselamatan kerja terkait instalasi listrik
- Pencegahan kecelakaan akibat listrik (kejutan, korsleting, kebakaran)
- Penggunaan alat pelindung diri (APD) listrik
- Standar dan regulasi keselamatan listrik (SNI, OSHA, IEC)
- Prosedur lockout-tagout (LOTO) untuk peralatan listrik
- Edukasi pekerja dan audit keselamatan listrik
- Penanganan darurat kecelakaan listrik secara aman

Jawablah dengan bahasa yang jelas, edukatif, dan mudah dipahami oleh pekerja maupun teknisi listrik.

ATURAN PENTING:
- Hanya jawab pertanyaan yang berkaitan dengan keselamatan listrik, K3 listrik, atau prosedur kerja aman listrik.
- Jangan memberikan arahan yang bersifat teknis berisiko tinggi tanpa pengawasan profesional.
- Penjelasan bersifat edukatif dan preventif.
- Jika pertanyaan TIDAK berkaitan dengan keselamatan listrik, jawab dengan:
  "Maaf, pertanyaan tersebut tidak berkaitan dengan topik keselamatan listrik dan K3."

Gunakan bahasa Indonesia yang jelas, profesional, dan bertanggung jawab secara edukatif dan keselamatan kerja.
"""

def chat():
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    print("Chatbox GERD dan gangguan mobil AI (Groq) (ketik 'exit' untuk keluar)\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",  
            messages=messages,
            temperature=0.3
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        print(f"GERD dan teknisi mobil  AI: {reply}\n")

if __name__ == "__main__":
    chat()
