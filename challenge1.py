import streamlit as st

# --- Page setup ---
st.set_page_config(
    page_title="GenAI Program",
    page_icon="🌞",
    layout="centered"
)

# --- Smooth warm gradient background ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #FFAD60, #FFD3B6); /* soft orange to peach */
        color: #333333; /* readable dark text */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- App title ---
st.title("🌞 Social Eagle GenAI Program Day 1 Python Challenge - Anbumani Panneerselvam🌞")
st.write("Enter your details below to receive a warm greeting!")

# --- Form inputs ---
name = st.text_input("Your Name:")
age = st.slider("Your Age:", 1, 100, 25)

# --- Display greeting with smooth contrast card ---
if name:
    st.markdown(
        f"""
        <div style="
            background-color: rgba(255, 255, 255, 0.3); /* soft translucent white */
            color: #333333;
            padding: 25px;
            border-radius: 20px;
            text-align: center;
            font-size: 22px;
            box-shadow: 3px 3px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease-in-out;
        ">
            Hello, <b>{name}</b>! You are <b>{age}</b> years young always - Rock your GenAI Journey! 🌞
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("Please enter your name to see the greeting.")
