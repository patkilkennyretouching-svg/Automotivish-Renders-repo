import streamlit as st

# Page Config
st.set_page_config(page_title="AI Render Architect", page_icon="🎨")
st.title("🎨 AI Render Architect")
st.subheader("Generate pro-level prompts for Nano Banana & Midjourney")

# --- SIDEBAR PARAMETERS ---
st.sidebar.header("Configuration")

# 1. Subject & Action
subject = st.sidebar.text_input("Core Subject", "A futuristic electric sports car")
action = st.sidebar.text_input("Action/Context", "driving through a neon-lit cyberpunk city")

# 2. Camera & Lens
camera = st.sidebar.selectbox("Camera Body", ["Hasselblad X2D", "Sony FX3 Cinema", "Leica M11", "Fujifilm GFX100 II", "GoPro Hero 12"])
lens = st.sidebar.selectbox("Lens Type", ["35mm Street Lens", "85mm Portrait (f/1.2)", "24mm Wide Angle", "Macro Lens", "Anamorphic Lens"])

# 3. Lighting & Mood
lighting = st.sidebar.select_slider("Lighting Style", 
    options=["Golden Hour", "Chiaroscuro (High Contrast)", "Softbox Studio", "Neon Cyberpunk", "Overcast/Moody"])

# 4. Technical Specs
aspect_ratio = st.sidebar.selectbox("Aspect Ratio", ["16:9", "4:5", "1:1", "9:16", "21:9"])
stylize = st.sidebar.slider("Midjourney Stylize (--s)", 0, 1000, 250)
chaos = st.sidebar.slider("Midjourney Chaos (--c)", 0, 100, 0)

# --- PROMPT LOGIC ---

# Nano Banana 2 Logic (Natural Language & Descriptive)
nano_prompt = (
    f"A high-end commercial render of {subject}, {action}. "
    f"Shot on {camera} with a {lens}. Lighting is {lighting}. "
    f"Intended for a luxury marketing campaign, 4K resolution, hyper-realistic textures, "
    f"cinematic color grading. Aspect ratio {aspect_ratio}."
)

# Midjourney Logic (Shorthand & Flags)
mj_ar = aspect_ratio.replace(":", ":")
mj_prompt = (
    f"{subject}, {action}, shot on {camera}, {lens}, {lighting} lighting, "
    f"commercial photography style --ar {mj_ar} --s {stylize} --c {chaos} --v 6.0"
)

# --- DISPLAY ---
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("🍌 Nano Banana 2")
    st.info("Best for Google Gemini/Nano Banana interfaces.")
    st.code(nano_prompt, language="text")
    if st.button("Copy Nano Prompt"):
        st.write("Prompt copied to clipboard! (Simulated)")

with col2:
    st.header("⛵ Midjourney")
    st.info("Optimized with --flags for Discord/Web.")
    st.code(mj_prompt, language="text")
    if st.button("Copy MJ Prompt"):
        st.write("Prompt copied to clipboard! (Simulated)")