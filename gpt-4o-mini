import streamlit as st
from openai import OpenAI

# Page Config
st.set_page_config(page_title="AI Business Customer Support Bot", page_icon="🤖")

st.title("🤖 AI Customer Support & FAQ Bot")
st.caption("Ask anything about our products, services, or business policies!")

# Sidebar for API Key & Knowledge Base Context
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    
    st.subheader("📚 Business Context")
    business_info = st.text_area(
        "Business Info / FAQ Context:", 
        value="""Company Name: TechSpark Solutions
Services: Web Development, SEO Optimization, AI Automation.
Working Hours: Mon-Fri, 9 AM - 6 PM EST.
Refund Policy: 14-day full money-back guarantee.
Contact Email: support@techspark.com""",
        height=150
    )

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! I am your AI Support Assistant. How can I help you today?"}
    ]

# Display Chat Messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input
if prompt := st.chat_input("Type your question here..."):
    if not api_key:
        st.error("Please add your OpenAI API Key in the sidebar to continue.")
        st.stop()
        
    client = OpenAI(api_key=api_key)
    
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # System Instructions incorporating business context
    system_prompt = f"""You are a polite, helpful customer support agent for a business. 
    Use the following business information to answer customer queries accurately:
    ---
    {business_info}
    ---
    If the answer isn't in the provided information, respond politely that you will connect them with human support via email."""

    # Generate Response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ]
    )
    
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
