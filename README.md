## 🚗 Vehicle Chatbot (Generative AI Project)

A domain-restricted conversational AI chatbot built using LangChain and Google Gemini (LLM). The application is designed to provide accurate information exclusively about two-wheelers and four-wheelers, while maintaining contextual conversation using chat history.

## 📌 Overview

This project demonstrates the practical implementation of Generative AI and Large Language Models (LLMs) for building a controlled, domain-specific chatbot. It leverages prompt engineering techniques to ensure that responses remain relevant, consistent, and aligned with predefined business rules.

## 🚀 Key Features
Domain-Specific Responses: Handles queries strictly related to vehicles (cars, bikes, SUVs, etc.)
Prompt Engineering: Enforces structured behavior using system-level instructions
Conversational Memory: Maintains chat history for context-aware interactions
User Interaction Handling: Supports greetings, name recognition, and follow-up queries
Response Control: Filters out irrelevant queries with predefined fallback responses
## 🧠 Tech Stack
Programming Language: Python
Framework: LangChain
LLM: Google Gemini (via langchain-google-genai)
Environment Management: python-dotenv
## ⚙️ System Architecture

The chatbot operates using:

System Message: Defines rules and constraints (prompt engineering)
Human Messages: Captures user inputs
AI Messages: Stores model-generated responses
Chat History: Ensures continuity and contextual understanding
## 📂 Project Structure
vehicle-chatbot/
│── app.py                # Main application script
│── requirements.txt     # Project dependencies
│── .env                 # API keys (not included in repo)
│── .gitignore           # Ignored files
│── README.md            # Project documentation
## ⚙️ Installation & Setup
1. Clone the Repository
 git clone https://github.com/your-username/vehicle-chatbot.gitcd vehicle-chatbot
 2. Install Dependencies
 pip install  -r requirements.txt
3. Configure Environment Variables

Create a .env file and add your API key:

GOOGLE_API_KEY=your_api_key_here
4. Run the Application
python app.py
## 💡 Sample Interaction
You: Hello  
AI: Hello! Please ask about vehicles.  

You: My name is Sufiyan  
AI: Nice to meet you Sufiyan! Please ask about vehicles.  

You: Best SUV under 10 lakh?  
AI: [Relevant vehicle information]  

You: What is my name?  
AI: Your name is Sufiyan.  
## 🎯 Key Learnings & Outcomes
Applied prompt engineering to control LLM behavior
Built a context-aware chatbot using LangChain
Integrated Google Gemini API for real-time response generation
Designed a rule-based AI system to handle domain-specific queries
## 🔮 Future Enhancements
Develop a web interface using Streamlit
Implement Retrieval-Augmented Generation (RAG) for improved accuracy
Add database integration for persistent memory
Deploy the application on cloud platforms (e.g., Render, Hugging Face)
## 👨‍💻 Author

Mohammad Sufiyan
