from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# College knowledge base
KNOWLEDGE = {
    "results": "Steps to check results:\n1. Login at portal.example.com\n2. Click 'Examinations'\n3. Select 'Result Dashboard'\n4. Choose your semester",
    "fees": "Fee payment process:\n1. Visit 'Finance' section\n2. Click 'Pay Fees'\n3. Select: Online (UPI/Card) or Offline (Cash at Office)\n4. Submit receipt to office if offline",
    "courses": "Available courses:\n- Computer Science (CS)\n- Electrical Engineering (EE)\n- Mechanical Engineering (ME)\nView details under 'Academics > Courses'"
}

# HuggingFace API setup
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": "HF_API_KEY"}  

def query_ai(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.json()[0]['generated_text']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json["question"].lower()
    
    # Find relevant context
    context = ""
    if "result" in user_question:
        context = KNOWLEDGE["results"]
    elif "fee" in user_question:
        context = KNOWLEDGE["fees"]
    elif "course" in user_question:
        context = KNOWLEDGE["courses"]
    else:
        context = "General help: Ask about results, fees, or courses"

    # AI-enhanced response
    prompt = f"""You are a helpful college portal assistant. Answer politely using this context:
    
    Context: {context}
    Question: {user_question}
    
    Answer: """
    
    try:
        ai_response = query_ai(prompt)
        answer = ai_response.split("Answer: ")[-1].strip()
    except:
        answer = f"From our knowledge base:\n{context}"
    
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
