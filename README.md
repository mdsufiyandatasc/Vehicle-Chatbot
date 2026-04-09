🚗 Vehicle Chatbot (GenAI Project)

A conversational AI chatbot built using LangChain and Google Gemini (LLM) that provides accurate and controlled information about two-wheelers and four-wheelers.

🚀 Features
💬 Conversational chatbot with memory (chat history)
🧠 Prompt engineering for controlled responses
🚫 Restricts answers to vehicle-related queries only
👤 Remembers user name and handles basic interactions
⚡ Fast responses using Gemini (LLM)
🧠 Tech Stack
Python
LangChain
Google Gemini API
Prompt Engineering
dotenv (Environment Variables)
📊 How It Works
Uses LangChain message framework to manage conversation
Maintains chat history for contextual understanding
Applies system rules (prompt engineering) to control responses
Uses Gemini LLM for generating answers
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/vehicle-chatbot.git
cd vehicle-chatbot
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Add API Key

Create a .env file and add:

GOOGLE_API_KEY=your_api_key_here
4️⃣ Run the Application
python app.py
💡 Example Usage
You: Hello  
AI: Hello! Please ask about vehicles.

You: My name is Sufiyan  
AI: Nice to meet you Sufiyan! Please ask about vehicles.

You: Best bike under 1 lakh?  
AI: (Provides answer)

You: What is my name?  
AI: Your name is Sufiyan.
📁 Project Structure
vehicle-chatbot/
│── app.py
│── requirements.txt
│── .env
│── .gitignore
│── README.md
🎯 Key Learnings
Prompt engineering for domain-restricted chatbots
Working with LLM APIs (Google Gemini)
Managing conversational memory using LangChain
Building rule-based AI assistants
🔮 Future Improvements
🌐 Add Streamlit web interface
🧾 Integrate database for long-term memory
🔍 Implement RAG (Retrieval-Augmented Generation)
🚀 Deploy as a web application
🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.
