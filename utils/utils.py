import os
import json
import streamlit as st
import shutil
import base64
from st_social_media_links import SocialMediaIcons 



def social_media(justify=None):
    # This function will help you to render socila media icons with link on the app
    social_media_links = [
    "https://github.com/PrajjwalSule21",
    "https://www.instagram.com/iamsule21/?hl=en",
    "https://www.linkedin.com/in/prajjwal-sule/"
                        ]   

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render(sidebar=True, justify_content=justify) # will render in the sidebar



def style_app():
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding: 1rem; }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: #E6F4EA;
    }

    [data-testid="stSidebar"][aria-expanded="true"] {
        min-width: 450px;
        max-width: 450px;
        background-color: #111111;
        color: #ffffff;
    }

    [data-testid="stSidebar"] .stTextInput label,
    [data-testid="stSidebar"] .stTextInput div,
    [data-testid="stSidebar"] .stTextInput input,
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
    }

    .stButton>button {
        background-color: #000;
        color: #fff;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        font-weight: 600;
    }

    .stButton>button:hover {
        background-color: #333;
        color: #fff;
    }

    .stMarkdown h1 {
        font-size: 2.5rem;
        margin-top: 2rem;
    }

    .stMarkdown p {
        font-size: 1.1rem;
        margin-top: -1rem;
        color: #444;
    }

    </style>
    """, unsafe_allow_html=True)



def page_config(layout = "centered"):
    st.set_page_config(
        page_title="FinSightAI",
        layout=layout,  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="📊"
    )

def about_app():
    with st.sidebar.expander("📊 FinSightAI - AI-Powered Stock Analyzer"):
        st.sidebar.caption("""Welcome to FinSightAI, your AI-powered assistant for performing fundamental analysis on stock data.  
                            Enter your API Key and the ticker symbol of the company you want to analyze. 
                           """)
                


def template_end():
    st.sidebar.markdown("### 👨‍💻 About the Developer")
    st.sidebar.markdown(
        """
        This app is built using **FastAPI**, **Streamlit**, and **Lyzr Agent API**  
        by **Prajjwal Sule** – an AI-focused Backend Developer with 2 years of experience building intelligent micro-apps, API services, and LLM-integrated solutions using Python, FastAPI, and modern AI agent frameworks. Proven expertise in Retrieval-Augmented Generation (RAG), LangChain, and LlamaIndex with hands-on knowledge of vector databases.
        
        🔗 [GitHub](https://github.com/PrajjwalSule21)  
        💼 [LinkedIn](https://www.linkedin.com/in/prajjwalsule/)  
        📧 suleprajjwal21@gmail.com
        """,
        unsafe_allow_html=True
    )
