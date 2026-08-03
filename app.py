import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Assistant")

# 2. Sidebar for API Key Input (Secure Way)
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

if api_key:
    # Initialize Groq Client
    client = Groq(api_key=api_key)

    # 3. System Prompt / Instructions
    system_instruction = {
        "role": "system",
        "content": "Aap ek helpful AI assistant hain. User ke sawalon ke polite aur accurate jawabat dein."
    }

    # 4. Chat History Setup
    if "messages" not in st.session_state:
        st.session_state.messages = [system_instruction]

    # 5. Display Past Messages
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

    # 6. User Input & Response Generation
    if user_prompt := st.chat_input("Ask a question..."):
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.write(user_prompt)

        with st.chat_message("assistant"):
            try:
                # Llama 3.3 70B model call (Free on Groq)
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.messages,
                    temperature=0.7,
                )
                
                bot_reply = completion.choices[0].message.content
                st.write(bot_reply)

                st.session_state.messages.append({"role": "assistant", "content": bot_reply})

            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("👈 Chatbot start karne ke liye sidebar mein apni Groq API Key (`gsk_...`) paste karein.")
