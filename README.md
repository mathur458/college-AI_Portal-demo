# 🎓 College Portal Assistant (Flask + Mistral-7B)

This is a lightweight Flask web application that serves as an intelligent college portal assistant. It combines a contextual knowledge base with a Hugging Face-hosted LLM (`Mistral-7B-Instruct`) to answer student queries about results, fee payments, and course offerings.

---

## 🚀 Features

- 🔍 Answers student queries related to:
  - Exam Results
  - Fee Payment Process
  - Available Courses
- 🤖 AI-enhanced replies using Hugging Face's Mistral-7B model
- 🧠 Context-aware responses with fallback to local knowledge base
- 🧩 Clean Flask backend with simple API endpoint
- 🌐 HTML interface via `index.html` (optional integration)

---

## 🛠 Tech Stack

- Python 3
- Flask
- Hugging Face Inference API
- HTML/CSS (for frontend)
- REST API (AJAX-based question/answer endpoint)

---

## 📂 Project Structure

college-portal-demo/
  -|-app.py
  -|-knowledge-base/
    -|-portal.txt
  -|-templates/
    -|-index.html


---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/college-portal-assistant.git
   cd college-portal-assistant

2. Install dependencies
  ```bash
  pip install flask requests
```

3. Run the application

```bash
  python app.py
```

4. Access the app
Visit http://localhost:5000 in your browser.

## ✨ Example Questions
-"How do I check my result?"
-"Where can I pay my fees?"
-"What courses are offered in CS?"

## 📌 Notes
This is a basic proof-of-concept demo.
You can easily extend it to support more topics, log history, or connect to databases.
Ideal for academic portals or chatbot projects.

## 🔐 API Key Notice
This app uses a Hugging Face API key. For security:
  -Replace the hardcoded API key in app.py with your own key.
  -Consider storing the key in an environment variable or .env file for production.

```python
import os
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}
```

## 🤝 Contributions
Contributions, feedback, and suggestions are welcome. Feel free to open an issue or submit a PR.
