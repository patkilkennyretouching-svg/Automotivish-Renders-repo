import streamlit as st

st.set_page_config(page_title="Automotive Director Console", page_icon="🏎️", layout="wide")

st.title("🏎️ Automotive Director Console")
st.markdown("Professional-grade parameters for Nano Banana & Midjourney")
st.markdown("---")

# --- SIDEBAR: CAMERA & LENS ---
with st.sidebar.expander("📷 Camera, Lens & Angle", expanded=True):
    angle = st.selectbox("Camera Angle", [
        "Low-Angle Hero Shot (Aggressive)", 
        "High-Angle 3/4 (Classic)", 
        "Bird's Eye (Top Down)", 
        "Frontal Dead-On", 
        "Rear 3/4 (Tail light focus)", 
        "Tracking Shot (Side Profile)",
        "Worm's Eye (Extreme Low)",
        "Dutch Angle (Dynamic/Tilted)"
    ])
    
    lens = st.selectbox("Lens & Perspective", [
        "14mm Ultra-Wide (Dramatic Distortion)",
        "24mm Wide Angle (Standard Commercial)",
        "35mm Street (Natural Perspective)",
        "50mm Prime (Clean & True)",
        "85mm Portrait (Compressed/Tight)",
        "200mm Telephoto (Flat/Abstract)",
        "Macro (Extreme Detail)"
    ])
    
    shot_type = st.radio("Shot Type", ["Establishing (Environment focus)", "Full Body (Car focus)", "Detail (Macro/Part focus)"])

# --- SIDEBAR: THE VEHICLE ---
with st.sidebar.expander("🚗 Vehicle Details", expanded=False):
    brand = st.text_input("Brand/Model", "Porsche 911 Turbo S")
    finish = st.selectbox("Paint Finish", ["Nardo Gray", "Frozen Matte Black", "Liquid Silver", "British Racing Green", "Candy Apple Red", "Exposed Carbon Fiber"])
    
    wheels = st.selectbox("Wheels & Tires", [
        "Center-lock Racing Alloys",
        "Deep-dish Forged Wheels",
        "Vintage Mesh Spokes",
        "Gloss Black 5-Spoke",
        "Aerodynamic Disc Wheels"
    ])
    
    tire_state = st.selectbox("Tire Condition", ["Clean/Showroom", "Tire Shine/Wet", "Scuffed/Racing Wear", "Mud-splattered"])

# --- SIDEBAR: WORLD & WEATHER ---
with st.sidebar.expander("☁️ Atmosphere & Time", expanded=False):
    time_of_day = st.selectbox("Time of Day", [
        "Blue Hour (Pre-dawn)", "Golden Hour (Sunset)", "High Noon (Harsh Shadows)", 
        "Midnight (Artificial light)", "Twilight", "Golden Morn", "Astrophotography Night"
    ])
    
    weather = st.selectbox("Weather & Effects", [
        "Clear Sky", "Heavy Rain (Wet Asphalt)", "Foggy/Misty", 
        "Post-Rain (Puddles & Reflections)", "Dusty/Hazy", "Snowing", "Thunderstorm"
    ])

# --- PROMPT LOGIC ---
# Construction of the "Director's Brief"
subject_block = f"{brand} with {finish} paint and {wheels} ({tire_state} tires)"

# Nano Banana Logic
nano_prompt = (
    f"A {shot_type} automotive render. {angle}. Shot using a {lens}. "
    f"Subject: {subject_block}. Environment: {weather} during {time_of_day}. "
    f"Cinematic lighting, ray-traced reflections, 8k resolution, commercial advertising photography."
)

# Midjourney Logic
mj_prompt = (
    f"{subject_block}, {angle}, {shot_type}, {lens}, {weather}, {time_of_day}, "
    f"highly detailed, automotive CGI, unreal engine 5 render, volumetric lighting --ar 16:9 --v 6.0"
)

# --- MAIN DISPLAY ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🍌 Nano Banana 2")
    st.code(nano_prompt, language="text")
    st.caption("Best for natural language prompting.")

with col2:
    st.subheader("⛵ Midjourney")
    st.code(mj_prompt, language="text")
    st.caption("Optimized for token-based prompting.")

st.info("💡 **Director's Tip:** Use 'Post-Rain' with 'Blue Hour' for the most realistic reflections on car paint.")import streamlit as st

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
   
