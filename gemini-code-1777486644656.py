import streamlit as st

st.set_page_config(page_title="Automotive Director Suite: Cinematic Edition", page_icon="🏎️", layout="wide")

st.title("🏎️ Automotive Director Suite: Cinematic Edition")
st.markdown("---")

# --- SIDEBAR: THE RIG ---
with st.sidebar.expander("📷 Camera & Motion", expanded=True):
    angle = st.selectbox("Camera Angle", [
        "Low-Angle Hero Shot", "High-Angle 3/4", "Bird's Eye", 
        "Frontal Dead-On", "Rear 3/4", "Tracking Shot", "Interior Dashboard View"
    ])
    lens = st.selectbox("Lens", ["14mm Ultra-Wide", "24mm Wide", "35mm Street", "50mm Prime", "85mm Portrait", "200mm Telephoto"])
    
    motion_blur = st.toggle("Enable Motion Blur?", value=False)
    if motion_blur:
        speed = st.select_slider("Perceived Speed", options=["Cruising", "Fast", "High-Speed Chase"])
        motion_desc = f"Action shot with heavy motion blur, wheel rotation blur, {speed} shutter speed effect."
    else:
        motion_desc = "Static shot, sharp focus, frozen moment."

# --- SIDEBAR: NEW! CINEMATOGRAPHY & LIGHTING ---
with st.sidebar.expander("🎬 Vibe & Color Grade", expanded=False):
    vibe = st.selectbox("Color Grade", [
        "Natural / Raw",
        "Technicolor (Vintage 70s, High Saturation)",
        "Bleach Bypass (Gritty, High Contrast, Desaturated)",
        "Nordic (Cool Blues, Clean Whites, Minimalist)",
        "Teal & Orange (Hollywood Blockbuster Pop)"
    ])

with st.sidebar.expander("💡 Lighting Modifiers", expanded=False):
    lighting_mod = st.selectbox("Lighting Style", [
        "Standard Commercial",
        "Light Painting (Long exposure streaks)",
        "Gobo Shadows (Palm trees/Blinds patterns)",
        "High-Key (Bright, clean, white-out background)",
        "Chiaroscuro (Dramatic shadows and highlights)"
    ])

with st.sidebar.expander("🔥 Physical Effects (SFX)", expanded=False):
    sfx = st.multiselect("Active Elements", ["Exhaust Flames", "Glowing Brake Rotors", "Dust Kick-up", "Water Spray"])

# --- SIDEBAR: INTERIOR & EXTERIOR ---
with st.sidebar.expander("🛋️ Interior Luxury", expanded=False):
    show_interior = st.checkbox("Focus on Interior?")
    int_material = st.selectbox("Leather Type", ["Rich Brown Leather", "Tan Tuscany Leather", "Gray Nappa Leather", "Black Quilted Leather", "Alcantara & Carbon"])
    int_detail = st.selectbox("Stitching/Finish", ["Hand-stitched contrast seams", "Diamond-quilted patterns", "Open-pore wood trim", "Brushed aluminum accents"])

with st.sidebar.expander("🚗 Exterior & Paint", expanded=False):
    brand = st.text_input("Brand/Model", "Porsche 911")
    finish = st.selectbox("Paint", ["Nardo Gray", "Metallic Midnight Blue", "Matte Stealth Black", "Liquid Silver"])
    wheels = st.selectbox("Wheels", ["Forged Alloys", "Center-lock Racing", "Multi-spoke Mesh"])

# --- SIDEBAR: THE WORLD ---
with st.sidebar.expander("☁️ Environment", expanded=False):
    time_of_day = st.selectbox("Time", ["Golden Hour", "Blue Hour", "Midnight", "Overcast Day"])
    weather = st.selectbox("Weather", ["Clear", "Heavy Rain", "Foggy", "Post-Rain Puddles"])

# --- PROMPT GENERATION ---

# Build SFX String
sfx_string = f" Featuring {', '.join(sfx)}." if sfx else ""

# Logic for Subject
if show_interior:
    subject_brief = f"Detailed luxury interior of a {brand}, {int_material} with {int_detail}."
else:
    subject_brief = f"{brand} in {finish} paint, {wheels} wheels.{sfx_string}"

# Nano Banana 2
nano_prompt = (
    f"A professional automotive photograph. Angle: {angle}. Lens: {lens}. "
    f"Subject: {subject_brief}. {motion_desc} Setting: {weather} during {time_of_day}. "
    f"Visual Style: {vibe}. Lighting: {lighting_mod}. "
    f"High-end CGI render, ray-traced reflections, 8k resolution, cinematic advertising aesthetic."
)

# Midjourney
mj_prompt = (
    f"{subject_brief}, {angle}, {lens}, {motion_desc}, {weather}, {time_of_day}, "
    f"{vibe} color grade, {lighting_mod} lighting, photorealistic, 8k, "
    f"automotive photography style --ar 16:9 --v 6.0"
)

# --- DISPLAY ---
col1, col2 = st.columns(2)
with col1:
    st.subheader("🍌 Nano Banana 2")
    st.code(nano_prompt, language="text")
with col2:
    st.subheader("⛵ Midjourney")
    st.code(mj_prompt, language="text")

st.success(f"Director's Note: Currently rendering a {vibe} aesthetic with {lighting_mod} lighting.")
