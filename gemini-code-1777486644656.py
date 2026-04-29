import streamlit as st

st.set_page_config(page_title="Pro Automotive Render Architect", page_icon="🏎️", layout="wide")

st.title("🏎️ Pro Automotive Render Architect")
st.markdown("---")

# --- SIDEBAR: THE GARAGE ---
st.sidebar.header("🚗 Vehicle Configuration")

use_custom = st.sidebar.checkbox("Use Custom Subject?")
if use_custom:
    subject = st.sidebar.text_input("Custom Subject", "A vintage motorcycle")
else:
    brand = st.sidebar.selectbox("Car Brand", ["Porsche", "Audi", "Plymouth", "Ferrari", "Lamborghini", "Tesla", "BMW"])
    model_type = st.sidebar.text_input("Specific Model (Optional)", "911 GT3 RS")
    subject = f"{brand} {model_type}".strip()

finish = st.sidebar.selectbox("Paint Finish", 
    ["Nardo Gray", "High-Gloss Metallic", "Matte Stealth Black", "Candy Apple Red", "Satin Pearl White", "Raw Carbon Fiber"])

# --- SIDEBAR: THE SETTING ---
st.sidebar.header("🌍 Environment & Mood")

location = st.sidebar.selectbox("Location", [
    "Scenic Coastal Highway at sunset",
    "Industrial Warehouse District with puddles",
    "Trendy Urban Coffee Shop exterior",
    "Modernist Concrete Villa driveway",
    "Neon-drenched Tokyo Underground",
    "Salt Flats under a midday sun"
])

# Lighting & Tech (kept from before)
lighting = st.sidebar.select_slider("Lighting", 
    options=["Golden Hour", "Cinematic Rim Lighting", "Softbox Studio", "Harsh Midday", "Moody Overcast"])

camera = st.sidebar.selectbox("Camera", ["Hasselblad X2D", "Sony FX3 Cinema", "Leica M11"])
aspect_ratio = st.sidebar.selectbox("Aspect Ratio", ["16:9", "4:5", "1:1", "21:9"])

# --- GENERATION LOGIC ---

# Nano Banana 2 (Natural, Context-heavy)
nano_prompt = (
    f"A high-end commercial automotive photograph of a {subject} featuring a {finish} finish. "
    f"The car is positioned at a {location}. Shot on {camera}. "
    f"Lighting: {lighting}. 8k resolution, photorealistic, intricate textures, sharp focus, "
    f"commercial car advertisement style. Aspect ratio {aspect_ratio}."
)

# Midjourney (Tokenized)
mj_ar = aspect_ratio.replace(":", ":")
mj_prompt = (
    f"{subject}, {finish} paint, {location}, shot on {camera}, {lighting} lighting, "
    f"automotive photography, advertising style, hyper-realistic --ar {mj_ar} --v 6.0"
)

# --- DISPLAY ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🍌 Nano Banana 2")
    # Using st.code with no button—it has a built-in copy button!
    st.code(nano_prompt, language="text")
    st.caption("Click the icon in the top right of the box to copy.")

with col2:
    st.subheader("⛵ Midjourney")
    st.code(mj_prompt, language="text")
    st.caption("Click the icon in the top right of the box to copy.")
    st.write("Prompt copied to clipboard! (Simulated)")
