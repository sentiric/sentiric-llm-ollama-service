### 📄 File: `README.md` | 🏷️ Markdown

```markdown
# 🦙 Sentiric LLM Ollama Service

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Language](https://img.shields.io/badge/language-Python-blue.svg)]()
[![Engine](https://img.shields.io/badge/engine-OllamaLocal-purple.svg)]()

**Sentiric LLM Ollama Service**, Ollama gibi yerel LLM dağıtım araçlarıyla entegrasyonu sağlayan bir adaptör servisidir. Bu sayede Sentiric platformu, hassas veriler veya yüksek maliyet kaygıları olan ortamlar için LLM yeteneklerini özel donanım üzerinde çalıştırabilir.

## 🎯 Temel Sorumluluklar

*   **Ollama Adaptasyonu:** Ollama'nın REST API'sine (özellikle streaming API'ye) bağlanmayı ve istekleri formatlamayı yönetir.
*   **Yerel Yönlendirme:** `OLLAMA_API_URL` değişkeni üzerinden Ollama konteynerine veya harici bir URL'ye bağlanır.
*   **Model Yönetimi:** Hangi yerel modelin kullanılacağını (llama3, mistral vb.) yapılandırır.

## 🛠️ Teknoloji Yığını

*   **Dil:** Python 3.11
*   **Web Çerçevesi:** FastAPI / Uvicorn
*   **İstemci:** httpx (Asenkron HTTP)
*   **Bağımlılıklar:** `sentiric-contracts` v1.9.0

## 🔌 API Etkileşimleri

*   **Gelen (Sunucu):**
    *   `sentiric-llm-gateway-service` (HTTP POST / gRPC): `Generate` RPC'si.
*   **Giden (İstemci):**
    *   Ollama REST API (Yerel ağdaki bir konteyner veya host).

---
## 🏛️ Anayasal Konum

Bu servis, [Sentiric Anayasası'nın](https://github.com/sentiric/sentiric-governance) **AI Engine Layer**'ında yer alan uzman bir bileşendir.