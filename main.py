import streamlit as st
import zxcvbn

def check_password_strength(password):
    result = zxcvbn.zxcvbn(password)
    strength = result['score']
    feedback = result['feedback']['suggestions']
    
    strength_levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    return strength, strength_levels[strength], feedback

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, strength_text, feedback = check_password_strength(password)

    # Color-coded strength bar
    colors = ["red", "orange", "yellow", "lightgreen", "green"]
    st.markdown(
        f"""
        <div style='width:100%; background:#ddd; border-radius:10px;'>
            <div style='width:{(strength + 1) * 20}%; background:{colors[strength]}; padding:5px; 
                        border-radius:10px; text-align:center; color:white;'>
                {strength_text}
            </div>
        </div>
        """, unsafe_allow_html=True
    )

    # Show feedback for all passwords
    if feedback:
        st.warning("🔹 Suggestions to improve your password:")
        for tip in feedback:
            st.write(f"- {tip}")
    else:
        st.success("✅ Your password is strong!")

    # Show password strength score
    st.write(f"Password strength score: {strength}/4")
