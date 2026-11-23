# College Enquiry Chatbot (Roll No. 11)

A simple Streamlit chatbot that answers college-related questions using only the information provided in `college_info.txt`. It uses the Groq API and does not train a model.

## Features
- Chat interface and session-based chat history
- College enquiry answers grounded in the supplied text file
- Prompt instruction to avoid guessing or inventing information
- Clear chat button

## Requirements
- Python 3.10 or newer
- Internet connection
- Groq API key

## Run on macOS
1. Install Python 3 if needed.
2. Open Terminal and move into this project directory.
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Create the API-key file:
   ```bash
   cp .env.example .env
   ```
6. Open `.env` in a text editor and replace the placeholder with your Groq API key. Never commit `.env` to GitHub.
7. Replace the sample contents of `college_info.txt` with accurate information for your college.
8. Start the app:
   ```bash
   streamlit run app.py
   ```
9. The app opens in your browser. Ask sample questions such as “How can I apply?”, “What courses are offered?” and “What are the fees?”.

## Sample questions to test
- How can I apply for admission?
- What courses are offered?
- Tell me about facilities.
- What are the fees?
- What is the official contact number? (The bot should say the information is not available if it is not in the file.)
- Tell me the capital of France. (The bot should redirect to college enquiries.)

## Project structure
```
college_enquiry_chatbot/
├── app.py
├── college_info.txt
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── screenshots/   # add 3–5 screenshots of your running app here
```
