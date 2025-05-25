# 🔐 Project 02: Password Strength Meter
# Author: Hammad Janjua

import streamlit as st
from zxcvbn import zxcvbn
import random

# Custom CSS for animations and layout
st.markdown("""
    <style>
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #002f34;
            text-align: center;
            animation: fadeInDown 1s ease-in-out;
        }
        @keyframes fadeInDown {
            0% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .strength {
            font-weight: bold;
            text-align: center;
            padding: 10px;
            border-radius: 10px;
            margin-top: 10px;
        }
        .password-box {
            width: 100%;
            padding: 10px;
            font-size: 1.2rem;
        }
        .author {
            text-align: center;
            font-size: 1rem;
            color: gray;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Weak password blacklist
blacklist = ["password", "123456", "password123", "qwerty", "admin", "letmein"]

# Strong password generator
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Color-coded strength label
def strength_label(score):
    if score <= 1:
        return "❌ Weak", "#ff4d4d"
    elif score == 2:
        return "⚠️ Moderate", "#ffcc00"
    elif score >= 3:
        return "✅ Strong", "#4CAF50"

# Title
st.markdown('<div class="title">🔐 Password Strength Meter</div>', unsafe_allow_html=True)
st.markdown('<div class="author">Developed by: <strong>Hammad Janjua</strong></div>', unsafe_allow_html=True)

# Password input
password = st.text_input("🔑 Enter your password", type="password", key="password_input")

# "Enter" Button
if st.button("🔍 Check Strength"):
    if not password:
        st.warning("⚠️ Please enter a password before checking.")
    elif password.lower() in blacklist:
        st.error("❌ This password is too common. Please choose a stronger one.")
    else:
        result = zxcvbn(password)
        score = result['score']
        label, color = strength_label(score)

        st.markdown(f"""
            <div class="strength" style="background-color: {color}; color: white;">
                Password Score: {score} / 4 — {label}
            </div>
        """, unsafe_allow_html=True)

        if result["feedback"]["warning"]:
            st.warning(result["feedback"]["warning"])

        for tip in result["feedback"]["suggestions"]:
            st.info(f"💡 {tip}")

# Password Generator Feature
if st.button("🔁 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"✅ Suggested Password: `{strong_password}`")
