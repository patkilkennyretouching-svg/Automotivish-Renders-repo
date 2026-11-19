import json
import random

import streamlit as st

st.set_page_config(page_title="Automotive Director Suite: Cinematic Edition", page_icon="🏎️", layout="wide")

# ---------------------------------------------------------------------------
# OPTIONS
# ---------------------------------------------------------------------------
EXTERIOR_ANGLES = ["Low-Angle Hero Shot", "High-Angle 3/4", "Bird's Eye", "Frontal Dead-On", "Rear 3/4", "Tracking Shot"]
INTERIOR_ANGLES = ["Dashboard & Steering Wheel", "Driver's Seat POV", "Center Console Close-Up", "Rear Seats Wide View"]
LENSES = ["14mm Ultra-Wide", "24mm Wide", "35mm Street", "50mm Prime", "85mm Portrait", "200mm Telephoto"]
SPEEDS = ["Cruising", "Fast", "High-Speed Chase"]

# Menu label -> description that actually goes into the prompt
VIBES = {
    "Natural / Raw": "natural, true-to-life color",
    "Technicolor (Vintage 70s, High Saturation)": "vintage 70s Technicolor look, high saturation",
    "Bleach Bypass (Gritty, High Contrast, Desaturated)": "bleach bypass look, gritty, high contrast, desaturated",
    "Nordic (Cool Blues, Clean Whites, Minimalist)": "Nordic look, cool blues, clean whites, minimalist",
    "Teal & Orange (Hollywood Blockbuster Pop)": "teal and orange blockbuster color grade",
}
LIGHTING = {
    "Standard Commercial": "standard commercial lighting",
    "Light Painting (Long exposure streaks)": "light painting, long-exposure light streaks",
    "Gobo Shadows (Palm trees/Blinds patterns)": "gobo shadows, palm tree or window blind patterns",
    "High-Key (Bright, clean, white-out background)": "high-key lighting, bright, clean, white background",
    "Chiaroscuro (Dramatic shadows and highlights)": "chiaroscuro lighting, dramatic shadows and highlights",
}
SFX_OPTIONS = ["Exhaust Flames", "Glowing Brake Rotors", "Dust Kick-up", "Water Spray"]
LEATHERS = ["Rich Brown Leather", "Tan Tuscany Leather", "Gray Nappa Leather", "Black Quilted Leather", "Alcantara & Carbon"]
INT_DETAILS = ["Hand-stitched contrast seams", "Diamond-quilted patterns", "Open-pore wood trim", "Brushed aluminum accents"]
WHEELS = ["Forged Alloys", "Center-lock Racing", "Multi-spoke Mesh"]
TIMES = ["Golden Hour", "Blue Hour", "Midnight", "Overcast Day"]
WEATHERS = ["Clear", "Heavy Rain", "Foggy", "Post-Rain Puddles"]
RENDER_STYLES = ["Photographic", "CGI render"]
NEGATIVE_OPTIONS = [
    "text", "watermark", "logos", "distorted wheels", "warped badges", "extra mirrors",
    "extra doors", "blurry", "people", "license plate",
]

# ---------------------------------------------------------------------------
# VEHICLES  (edit freely: add or remove models in any list)
# Priority brands first, then the rest alphabetically.
# "(classic)" / year tags mark heritage cars; lineups change, so tweak as needed.
# ---------------------------------------------------------------------------
CUSTOM = "Custom (type your own)"

VEHICLES = {
    "Mercedes-Benz": [
        "Mercedes-Benz CLA 250 4MATIC",
        "Mercedes-AMG CLA 45 S",
        "Mercedes-Benz C 300 4MATIC Sedan",
        "Mercedes-Benz Electric C-Class (C 400 4MATIC Electric)",
        "Mercedes-AMG C 63 S E Performance",
        "Mercedes-Benz E 450 4MATIC Sedan",
        "Mercedes-Benz E 450 4MATIC All-Terrain",
        "Mercedes-AMG E 53 Hybrid",
        "Mercedes-Benz CLE Coupe",
        "Mercedes-Benz CLE Cabriolet",
        "Mercedes-Benz S 580 4MATIC",
        "Mercedes-Maybach S 580",
        "Mercedes-Maybach S 680",
        "Mercedes-Benz EQS Sedan",
        "Mercedes-AMG GT 63 4MATIC+ Coupe",
        "Mercedes-AMG GT 63 S E Performance 4-Door Coupe",
        "Mercedes-AMG SL 63",
        "Mercedes-Benz GLA 250",
        "Mercedes-Benz Electric GLB",
        "Mercedes-Benz GLC 300 4MATIC SUV",
        "Mercedes-Benz GLC Coupe",
        "Mercedes-Benz Electric GLC 400 4MATIC with EQ Technology",
        "Mercedes-AMG GLC 63 S E Performance",
        "Mercedes-Benz GLE 450 4MATIC",
        "Mercedes-Benz GLE Coupe",
        "Mercedes-AMG GLE 53 Hybrid",
        "Mercedes-Benz GLS 450",
        "Mercedes-Benz GLS 580",
        "Mercedes-Maybach GLS 680",
        "Mercedes-Benz G 550",
        "Mercedes-AMG G 63",
        "Mercedes-Benz G 580 with EQ Technology",
        "Mercedes-Benz EQS SUV",
        "Mercedes-Benz EQE SUV",
        "Mercedes-Benz Electric VLE",
        "Mercedes-AMG One",
        "Mercedes-Benz 300 SL Gullwing (1955, classic)",
        "Mercedes-Benz 190 SL (1955, classic)",
        "Mercedes-Benz 280 SL Pagoda (1968, classic)",
        "Mercedes-Benz 500 E (1991, classic)",
        "Mercedes-Benz CLK GTR (1998, classic)",
        "Mercedes-Benz SLR McLaren (2004, classic)",
    ],
    "Porsche": [
        "Porsche 911 Carrera",
        "Porsche 911 Carrera S",
        "Porsche 911 Carrera 4S",
        "Porsche 911 Carrera T",
        "Porsche 911 Carrera GTS",
        "Porsche 911 Targa 4 GTS",
        "Porsche 911 Cabriolet",
        "Porsche 911 Turbo S",
        "Porsche 911 GT3",
        "Porsche 911 GT3 Touring",
        "Porsche 911 GT3 RS",
        "Porsche 911 GT3 Cabriolet",
        "Porsche 911 Dakar",
        "Porsche 911 GT2 RS",
        "Porsche 718 Cayman GT4 RS",
        "Porsche 718 Spyder RS",
        "Porsche 718 Cayman GTS 4.0",
        "Porsche 718 Boxster GTS 4.0",
        "Porsche Taycan",
        "Porsche Taycan 4S",
        "Porsche Taycan 4S Cross Turismo",
        "Porsche Taycan GTS",
        "Porsche Taycan Turbo",
        "Porsche Taycan Turbo S",
        "Porsche Taycan Turbo GT",
        "Porsche Panamera",
        "Porsche Panamera 4S E-Hybrid",
        "Porsche Panamera GTS",
        "Porsche Panamera Turbo S E-Hybrid",
        "Porsche Panamera Sport Turismo",
        "Porsche Macan 4 Electric",
        "Porsche Macan 4S Electric",
        "Porsche Macan GTS Electric",
        "Porsche Macan Turbo Electric",
        "Porsche Cayenne",
        "Porsche Cayenne S",
        "Porsche Cayenne GTS",
        "Porsche Cayenne Turbo E-Hybrid",
        "Porsche Cayenne Coupe",
        "Porsche Cayenne Electric",
        "Porsche Cayenne S Electric",
        "Porsche Cayenne Turbo Electric",
        "Porsche Cayenne Coupe Electric",
        "Porsche 918 Spyder",
        "Porsche Carrera GT",
        "Porsche 959 (1986, classic)",
        "Porsche 356 Speedster (1950s, classic)",
        "Porsche 911 Carrera RS 2.7 (1973, classic)",
        "Porsche 911 Turbo 930 (1975, classic)",
        "Porsche 911 GT1 Strassenversion (1998, classic)",
        "Porsche 917 (1970, classic race car)",
        "Porsche 962 (1980s, classic race car)",
    ],
    "Ford": [
        "Ford Mustang EcoBoost Fastback",
        "Ford Mustang GT Fastback",
        "Ford Mustang GT Convertible",
        "Ford Mustang Dark Horse",
        "Ford Mustang GTD",
        "Ford Mustang Mach-E",
        "Ford Mustang Mach-E GT",
        "Ford Bronco 2-Door",
        "Ford Bronco 4-Door Badlands",
        "Ford Bronco Black Diamond",
        "Ford Bronco Everglades",
        "Ford Bronco Raptor",
        "Ford Bronco Sport Badlands",
        "Ford Maverick Lobo",
        "Ford Maverick Tremor",
        "Ford Ranger Lariat",
        "Ford Ranger Raptor",
        "Ford F-150 XLT",
        "Ford F-150 Lariat",
        "Ford F-150 King Ranch",
        "Ford F-150 Platinum",
        "Ford F-150 Limited",
        "Ford F-150 Tremor",
        "Ford F-150 Raptor",
        "Ford F-150 Raptor R",
        "Ford F-150 Hybrid",
        "Ford F-150 Lightning (final model year 2026)",
        "Ford F-250 Super Duty Lariat",
        "Ford F-350 Super Duty King Ranch",
        "Ford F-450 Super Duty Platinum",
        "Ford Expedition Platinum",
        "Ford Expedition Max King Ranch",
        "Ford Expedition Timberline",
        "Ford Explorer ST",
        "Ford Explorer ST-Line",
        "Ford Explorer Platinum",
        "Ford Explorer Timberline",
        "Ford Escape (final model year 2026)",
        "Ford GT (2017-2022)",
        "Ford GT40 Mk II (1966, classic race car)",
        "Ford Shelby Cobra 427 (1960s, classic)",
        "Ford Mustang Boss 429 (1969, classic)",
        "Ford Mustang Mach 1 (1969, classic)",
        "Ford Mustang Shelby GT500 (1967, classic)",
        "Ford Bronco (1966, classic)",
        "Ford F-100 (1956, classic)",
        "Ford Thunderbird (1957, classic)",
    ],
    "Land Rover": [
        "Land Rover Defender 90",
        "Land Rover Defender 90 V8",
        "Land Rover Defender 110",
        "Land Rover Defender 110 Octa",
        "Land Rover Defender 130",
        "Land Rover Defender 130 Outbound",
        "Land Rover Discovery",
        "Land Rover Discovery Sport (final model year 2026)",
        "Range Rover",
        "Range Rover LWB",
        "Range Rover SV",
        "Range Rover Autobiography",
        "Range Rover Electric",
        "Range Rover Sport",
        "Range Rover Sport Dynamic SE",
        "Range Rover Sport SV Edition Two",
        "Range Rover Velar",
        "Range Rover Evoque",
        "Land Rover Series I (1948, classic)",
        "Land Rover Series IIA (1960s, classic)",
        "Range Rover Classic (1970, classic)",
        "Land Rover Defender 90 (1990s, classic)",
        "Land Rover Discovery Series I (1989, classic)",
    ],
    "Aston Martin": [
        "Aston Martin DB12", "Aston Martin DB12 Volante", "Aston Martin Vantage", "Aston Martin Vantage Roadster",
        "Aston Martin Vanquish", "Aston Martin Vanquish Volante", "Aston Martin DBX707", "Aston Martin DBX S",
        "Aston Martin Valhalla", "Aston Martin Valkyrie", "Aston Martin DB5 (1964, classic)",
        "Aston Martin DB11", "Aston Martin Vanquish (2001, classic)",
    ],
    "Audi": [
        "Audi RS 6 Avant", "Audi RS 7", "Audi RS 3", "Audi RS e-tron GT", "Audi e-tron GT", "Audi RS Q8", "Audi Q8",
        "Audi Q6 e-tron", "Audi A5", "Audi A6 Avant e-tron", "Audi R8 V10 Performance (final edition)", "Audi TT RS",
        "Audi Quattro (1984, classic)", "Audi Sport Quattro S1 (1985, classic rally car)",
    ],
    "Bentley": [
        "Bentley Continental GT Speed", "Bentley Continental GTC", "Bentley Flying Spur", "Bentley Flying Spur Mulliner",
        "Bentley Bentayga", "Bentley Bentayga EWB", "Bentley Batur", "Bentley Blower (1929, classic)",
        "Bentley R-Type Continental (1952, classic)",
    ],
    "BMW": [
        "BMW M2", "BMW M3", "BMW M3 Touring", "BMW M4", "BMW M4 CSL", "BMW M5", "BMW M5 Touring", "BMW 3 Series",
        "BMW 5 Series", "BMW 7 Series", "BMW i4", "BMW i5", "BMW i7", "BMW iX", "BMW iX3 (Neue Klasse)",
        "BMW X3", "BMW X5", "BMW X5 M Competition", "BMW X7", "BMW XM", "BMW Z4 M40i",
        "BMW M1 (1978, classic)", "BMW 2002 Turbo (1973, classic)", "BMW E30 M3 (1988, classic)",
        "BMW 507 (1957, classic)", "BMW 3.0 CSL (1973, classic)",
    ],
    "Bugatti": [
        "Bugatti Tourbillon", "Bugatti Chiron Super Sport", "Bugatti Chiron Pur Sport", "Bugatti Bolide",
        "Bugatti Veyron Grand Sport Vitesse", "Bugatti Type 57SC Atlantic (1936, classic)",
    ],
    "Cadillac": [
        "Cadillac Escalade", "Cadillac Escalade IQ", "Cadillac Lyriq", "Cadillac Optiq", "Cadillac Vistiq",
        "Cadillac Celestiq", "Cadillac CT5-V Blackwing", "Cadillac CT4-V Blackwing",
        "Cadillac Eldorado Biarritz (1959, classic)", "Cadillac Series 62 (1950s, classic)",
    ],
    "Chevrolet": [
        "Chevrolet Corvette Stingray", "Chevrolet Corvette Grand Sport", "Chevrolet Corvette Z06",
        "Chevrolet Corvette E-Ray", "Chevrolet Corvette ZR1", "Chevrolet Silverado 1500 High Country",
        "Chevrolet Silverado EV", "Chevrolet Colorado ZR2", "Chevrolet Tahoe", "Chevrolet Suburban",
        "Chevrolet Blazer EV", "Chevrolet Camaro ZL1 (final edition)", "Chevrolet Bel Air (1957, classic)",
        "Chevrolet Camaro SS (1969, classic)", "Chevrolet Chevelle SS 454 (1970, classic)",
        "Chevrolet Corvette Sting Ray (1963, classic)", "Chevrolet C10 (1967, classic)",
    ],
    "Dodge / Ram / Jeep": [
        "Dodge Charger Daytona", "Dodge Charger Sixpack", "Dodge Durango Hellcat", "Ram 1500 RHO", "Ram 1500 Limited",
        "Ram 2500 Power Wagon", "Jeep Wrangler Rubicon", "Jeep Wrangler 4xe", "Jeep Gladiator Rubicon",
        "Jeep Grand Cherokee Summit", "Jeep Grand Wagoneer", "Jeep Willys (1944, classic)",
        "Dodge Challenger SRT Demon 170 (final edition)", "Dodge Charger R/T (1969, classic)",
        "Dodge Viper ACR (classic)", "Plymouth Barracuda (1970, classic)",
    ],
    "Ferrari": [
        "Ferrari 296 GTB", "Ferrari 296 GTS", "Ferrari 296 Speciale", "Ferrari SF90 XX Stradale", "Ferrari 12Cilindri",
        "Ferrari Amalfi", "Ferrari Purosangue", "Ferrari 849 Testarossa", "Ferrari Daytona SP3", "Ferrari F80",
        "Ferrari F40 (1987, classic)", "Ferrari Testarossa (1984, classic)", "Ferrari 250 GTO (1962, classic)",
        "Ferrari Enzo (2002, classic)", "Ferrari 308 GTS (1978, classic)", "Ferrari F355 (1995, classic)",
    ],
    "Genesis": [
        "Genesis G70", "Genesis G80", "Genesis G90", "Genesis GV60", "Genesis GV70", "Genesis GV80",
        "Genesis GV80 Coupe", "Genesis X Gran Berlinetta (concept)",
    ],
    "Honda / Acura": [
        "Honda Civic Type R", "Honda Prelude", "Honda Accord", "Acura Integra Type S", "Acura TLX Type S",
        "Acura NSX Type S (final edition)", "Acura NSX (1991, classic)", "Honda S2000 (classic)",
        "Honda CR-X Si (classic)",
    ],
    "Hyundai / Kia": [
        "Hyundai Ioniq 5 N", "Hyundai Ioniq 6 N", "Hyundai Ioniq 9", "Hyundai Santa Fe XRT", "Kia EV9", "Kia EV6 GT",
        "Kia Telluride", "Kia Stinger GT (final edition)",
    ],
    "Jaguar": [
        "Jaguar F-Type R (final edition)", "Jaguar Type 00 (concept)", "Jaguar E-Type Series 1 (1961, classic)",
        "Jaguar XJ220 (1992, classic)", "Jaguar D-Type (1955, classic race car)", "Jaguar XK120 (1948, classic)",
    ],
    "Lamborghini": [
        "Lamborghini Revuelto", "Lamborghini Temerario", "Lamborghini Urus SE", "Lamborghini Urus Performante",
        "Lamborghini Huracan Tecnica", "Lamborghini Huracan STO", "Lamborghini Huracan Sterrato",
        "Lamborghini Countach LPI 800-4", "Lamborghini Miura SV (1971, classic)",
        "Lamborghini Countach LP400 (1974, classic)", "Lamborghini Diablo SV (1997, classic)",
        "Lamborghini Aventador SVJ (classic)",
    ],
    "Lexus / Toyota": [
        "Lexus LC 500", "Lexus LC 500 Convertible", "Lexus RC F", "Lexus IS 500", "Lexus LX 600", "Lexus GX 550",
        "Lexus LFA (2010, classic)", "Toyota GR Supra", "Toyota GR86", "Toyota GR Corolla", "Toyota GR GT",
        "Toyota Land Cruiser", "Toyota 4Runner TRD Pro", "Toyota Tacoma TRD Pro", "Toyota Tundra TRD Pro",
        "Toyota Supra A80 (1994, classic)", "Toyota 2000GT (1967, classic)", "Toyota Land Cruiser FJ40 (1970s, classic)",
    ],
    "Lotus": [
        "Lotus Emira", "Lotus Eletre", "Lotus Emeya", "Lotus Evija", "Lotus Elise (classic)",
        "Lotus Esprit (1980s, classic)", "Lotus Seven (classic)", "Lotus 49 (1967, classic race car)",
    ],
    "Maserati": [
        "Maserati MC20", "Maserati MC20 Cielo", "Maserati GranTurismo", "Maserati GranTurismo Folgore",
        "Maserati GranCabrio", "Maserati Grecale", "Maserati Levante", "Maserati MCPura",
        "Maserati 3500 GT (1960, classic)", "Maserati Bora (1971, classic)",
    ],
    "Mazda / Subaru / Nissan": [
        "Mazda MX-5 Miata", "Mazda CX-5", "Mazda RX-7 FD (1992, classic)", "Subaru WRX", "Subaru BRZ",
        "Subaru Impreza 22B STi (1998, classic)", "Nissan GT-R Nismo", "Nissan Z Nismo", "Nissan Skyline GT-R R34 (1999, classic)",
        "Nissan Silvia S15 (classic)", "Datsun 240Z (1970, classic)",
    ],
    "McLaren": [
        "McLaren 750S", "McLaren 750S Spider", "McLaren Artura", "McLaren Artura Spider", "McLaren GTS",
        "McLaren W1", "McLaren 765LT", "McLaren Senna", "McLaren P1", "McLaren F1 (1993, classic)",
    ],
    "Rivian / Tesla": [
        "Rivian R1T", "Rivian R1S", "Tesla Model S Plaid", "Tesla Model 3 Performance", "Tesla Model X Plaid",
        "Tesla Model Y", "Tesla Cybertruck Cyberbeast",
    ],
    "Rolls-Royce": [
        "Rolls-Royce Phantom", "Rolls-Royce Phantom Extended", "Rolls-Royce Ghost", "Rolls-Royce Ghost Black Badge",
        "Rolls-Royce Cullinan", "Rolls-Royce Cullinan Black Badge", "Rolls-Royce Spectre",
        "Rolls-Royce Silver Ghost (1920s, classic)", "Rolls-Royce Silver Cloud (1955, classic)",
        "Rolls-Royce Corniche (1970s, classic)",
    ],
    CUSTOM: ["(use the custom vehicle box)"],
}

PRIORITY_MAKES = ["Mercedes-Benz", "Porsche", "Ford", "Land Rover"]
MAKES = PRIORITY_MAKES + sorted(m for m in VEHICLES if m not in PRIORITY_MAKES and m != CUSTOM) + [CUSTOM]

# ---------------------------------------------------------------------------
# PAINT COLORS BY MAKE  (factory-style names; "(PTS)" = Paint to Sample / special order)
# Names are current-ish factory names but trims and years vary, so tweak as needed.
# Any make not listed here falls back to GENERIC_PAINTS.
# ---------------------------------------------------------------------------
CUSTOM_PAINT = "Custom color (type your own)"

PAINTS_BY_MAKE = {
    "Mercedes-Benz": [
        "Obsidian Black Metallic", "Black", "Polar White", "Cirrus Silver Metallic", "High-Tech Silver Metallic",
        "Selenite Grey Metallic", "Graphite Grey Metallic", "Indium Grey Metallic", "Twilight Blue Metallic",
        "Emerald Green Metallic", "Dark Petrol", "Sonoran Brown Metallic", "Miami Silver Metallic",
        "Moody Sky Grey Metallic", "Mojave Silver Metallic", "MANUFAKTUR Alpine Grey Magno (matte)",
        "MANUFAKTUR Patagonia Red Metallic", "MANUFAKTUR Cardinal Red Metallic", "MANUFAKTUR Silicon Grey",
        "MANUFAKTUR Verde Silver Magno (matte)", "MANUFAKTUR Black Sparkling", "MANUFAKTUR Diamond White Bright",
        "designo Hyacinth Red Metallic",
    ],
    "Porsche": [
        "Gentian Blue Metallic", "White", "Black", "Jet Black Metallic", "Carrara White Metallic",
        "GT Silver Metallic", "Ice Grey Metallic", "Agate Grey Metallic", "Arctic Grey", "Chalk",
        "Lugano Blue", "Shark Blue", "Miami Blue", "Guards Red", "Carmine Red", "Racing Yellow", "Lava Orange",
        "Python Green", "Mamba Green Metallic", "Aventurine Green Metallic", "Nardo Grey",
        "Gulf Blue (PTS)", "Voodoo Blue (PTS)", "Riviera Blue (PTS)", "Maritime Blue (PTS)",
        "Oak Green Metallic (PTS)", "F.A. Green Metallic (PTS)", "Cherry Metallic (PTS)", "Slate Grey Neo (PTS)",
        "Pyro Red (PTS)", "Ruby Star Neo (PTS)", "Mint Green (PTS)", "Viper Green (PTS)", "Signal Green (PTS)",
    ],
    "Ford": [
        "Oxford White", "Star White Metallic Tri-Coat", "Shadow Black", "Agate Black Metallic",
        "Carbonized Gray Metallic", "Iconic Silver Metallic", "Space Silver Metallic", "Marsh Gray",
        "Avalanche Gray", "Race Red", "Rapid Red Metallic", "Ruby Red Metallic", "Hot Pepper Red",
        "Grabber Blue", "Neptune Blue", "Antimatter Blue Metallic", "Wild Green", "Shelter Green Metallic",
        "Field Green Metallic", "Eruption Green", "Orange Fury Metallic", "Code Orange", "Cyber Orange",
        "Birch Sand", "Iron Sands Copper Metallic", "Yellow Splash", "Area 51",
    ],
    "Land Rover": [
        "Santorini Black", "Fuji White", "Yulong White", "Carpathian Grey", "Eiger Grey", "Borasco Grey",
        "Charente Grey", "Hakuba Silver", "Silicon Silver", "Gondwana Stone", "Tasman Blue", "Portofino Blue",
        "Varesine Blue", "Woolstone Green", "Pangea Green", "Keswick Green", "Belgravia Green",
        "Sedona Red", "Firenze Red", "Lantau Bronze", "Batumi Gold", "Ostuni Pearl White", "Sandglow Yellow",
        "Patagonia White Matte Wrap",
    ],
    "Aston Martin": [
        "Onyx Black", "Lightning Silver", "Skyfall Silver", "Magnetic Silver", "China Grey", "Xenon Grey",
        "Aston Martin Racing Green", "Arden Green", "Ultramarine Black", "Cosmos Orange", "Caledonian Blue",
    ],
    "Audi": [
        "Mythos Black Metallic", "Glacier White Metallic", "Ibis White", "Daytona Gray Pearl", "Nardo Gray",
        "Florett Silver", "Navarra Blue", "Turbo Blue", "Ascari Blue", "Tango Red", "Python Yellow", "District Green",
    ],
    "Bentley": [
        "Beluga", "Onyx", "Glacier White", "Moonbeam", "Magnetic", "Cambrian Grey", "Windsor Blue",
        "Sequin Blue", "Verdant", "British Racing Green", "St. James' Red", "Dragon Red", "Peacock",
    ],
    "BMW": [
        "Alpine White", "Black Sapphire Metallic", "Brooklyn Grey Metallic", "Dravit Grey Metallic",
        "Frozen Brands Hatch Grey (matte)", "Frozen Deep Grey (matte)", "Portimao Blue Metallic",
        "San Marino Blue", "Marina Bay Blue", "Isle of Man Green", "Toronto Red", "Fire Red",
        "Sao Paulo Yellow", "Tanzanite Blue (Individual)", "Daytona Violet (Individual)",
    ],
    "Bugatti": [
        "French Racing Blue", "Nocturne Black", "Quartz White", "Brescia Red", "Atlantic Blue",
        "Exposed Carbon Fiber", "Two-tone Blue and Black",
    ],
    "Cadillac": [
        "Black Raven", "Stellar Black Metallic", "Crystal White Tricoat", "Argent Silver Metallic",
        "Shadow Metallic", "Sapphire Blue Metallic", "Opulent Blue Metallic", "Radiant Red Tintcoat",
    ],
    "Chevrolet": [
        "Torch Red", "Arctic White", "Black", "Hypersonic Gray Metallic", "Ceramic Matrix Gray Metallic",
        "Silver Flare Metallic", "Elkhart Lake Blue Metallic", "Rapid Blue", "Riptide Blue Metallic",
        "Sebring Orange Tintcoat", "Accelerate Yellow", "Red Mist Tintcoat", "Caffeine Metallic", "Cacti Green",
    ],
    "Dodge / Ram / Jeep": [
        "Pitch Black", "Bright White", "Granite Crystal", "Destroyer Grey", "Billet Silver", "Fathom Blue",
        "Hydro Blue", "Sarge Green", "Sublime Green", "TorRed", "Firecracker Red", "Go Mango", "Hellayella",
        "Plum Crazy", "Baja Yellow",
    ],
    "Ferrari": [
        "Rosso Corsa", "Rosso Scuderia", "Giallo Modena", "Nero Daytona", "Bianco Avus", "Argento Nurburgring",
        "Grigio Titanio", "Blu Tour de France", "Blu Scozia", "Azzurro California", "Verde British", "Rosso Dino",
    ],
    "Genesis": [
        "Uyuni White", "Vik Black", "Savile Silver", "Himalayan Gray", "Adriatic Blue", "Cardiff Green",
        "Barossa Burgundy", "Mauna Red",
    ],
    "Honda / Acura": [
        "Championship White", "Platinum White Pearl", "Crystal Black Pearl", "Sonic Gray Pearl", "Boost Blue Pearl",
        "Apex Blue Pearl", "Rallye Red", "Majestic Black Pearl", "Phoenix Yellow", "Tiger Eye Pearl",
    ],
    "Hyundai / Kia": [
        "Atlas White", "Abyss Black Pearl", "Cyber Gray", "Ecotronic Gray", "Performance Blue",
        "Lucid Blue", "Digital Teal", "Gravity Gold Matte", "Snow White Pearl", "Wolf Gray",
    ],
    "Jaguar": [
        "Santorini Black", "Fuji White", "Eiger Grey", "Firenze Red", "Portofino Blue", "Ultra Blue",
        "British Racing Green", "Caldera Red", "Bluefire",
    ],
    "Lamborghini": [
        "Giallo Inti", "Arancio Borealis", "Arancio Argos", "Verde Mantis", "Nero Noctis", "Bianco Monocerus",
        "Blu Cepheus", "Grigio Telesto", "Rosso Mars", "Viola Pasifae", "Giallo Orion",
    ],
    "Lexus / Toyota": [
        "Ultra White", "Eminent White Pearl", "Wind Chill Pearl", "Caviar", "Atomic Silver", "Cement",
        "Nori Green Pearl", "Heritage Blue", "Matador Red", "Infrared", "Structural Blue", "Cadmium Orange",
    ],
    "Lotus": [
        "Hethel Yellow", "British Racing Green", "Seneca Blue", "Magma Red", "Nimbus Grey", "Starlight Black",
        "Metallic Silver",
    ],
    "Maserati": [
        "Blu Nobile", "Blu Emozione", "Grigio Incognito", "Grigio Mistero", "Bianco Alpi", "Rosso Magma",
        "Nero Ribelle", "Nero Enigma", "Giallo Genio", "Verde Royale",
    ],
    "Mazda / Subaru / Nissan": [
        "Soul Red Crystal Metallic", "Machine Gray Metallic", "Snowflake White Pearl", "Jet Black",
        "Rhodium White Metallic", "Aero Gray", "WR Blue Pearl", "Ice Silver", "Crystal Black Silica",
        "Bayside Blue", "Midnight Purple", "Ultimate Silver",
    ],
    "McLaren": [
        "Papaya Spark", "Volcano Orange", "Onyx Black", "Silica White", "Ceramic Grey", "Chicane Grey",
        "Burton Blue", "Vega Blue", "Supernova Silver", "Paris Blue",
    ],
    "Rivian / Tesla": [
        "Launch Green", "El Cap Granite", "Limestone", "Compass Yellow", "Glacier White", "Forest Green",
        "Pearl White Multi-Coat", "Solid Black", "Deep Blue Metallic", "Midnight Silver Metallic", "Stealth Grey",
        "Quicksilver", "Ultra Red",
    ],
    "Rolls-Royce": [
        "Diamond Black", "English White", "Arctic White", "Tempest Grey", "Salamanca Blue", "Midnight Sapphire",
        "Belladonna Purple", "Madeira Red", "Bespoke commissioned color",
    ],
}

# Fallback list (also used for Custom vehicles)
GENERIC_PAINTS = [
    "Nardo Gray", "Metallic Midnight Blue", "Matte Stealth Black", "Liquid Silver", "Pearl White",
    "Racing Green", "Candy Apple Red", "Burnt Orange", "Champagne Gold", "Satin Gunmetal", "Ivory Cream",
]
PAINTS = GENERIC_PAINTS  # kept for backward compatibility


def paint_options(make):
    return PAINTS_BY_MAKE.get(make, GENERIC_PAINTS) + [CUSTOM_PAINT]


MJ_VERSIONS = ["7", "6.1", "6.0"]  # edit this list as Midjourney versions change
ASPECTS = ["16:9", "3:2", "4:3", "1:1", "9:16", "21:9"]

# ---------------------------------------------------------------------------
# SESSION STATE: defaults, validation, presets, randomize
# ---------------------------------------------------------------------------
DEFAULTS = {
    "shot_type": "Exterior",
    "angle": EXTERIOR_ANGLES[0],
    "interior_angle": INTERIOR_ANGLES[0],
    "lens": LENSES[0],
    "motion_blur": False,
    "speed": SPEEDS[0],
    "vibe": list(VIBES)[0],
    "lighting": list(LIGHTING)[0],
    "sfx": [],
    "int_material": LEATHERS[0],
    "int_detail": INT_DETAILS[0],
    "make": "Porsche",
    "model": "Porsche 911 Carrera S",
    "custom_vehicle": "",
    "finish": "Gentian Blue Metallic",
    "custom_paint": "",
    "wheels": WHEELS[0],
    "time_of_day": TIMES[0],
    "weather": WEATHERS[0],
    "render_style": RENDER_STYLES[0],
    "negatives": ["text", "watermark", "distorted wheels", "warped badges", "extra mirrors"],
    "custom_negative": "",
    "mj_version": MJ_VERSIONS[0],
    "aspect": ASPECTS[0],
    "stylize": 100,
    "mj_raw": True,
}
SETTING_KEYS = list(DEFAULTS)

SINGLE_CHOICES = {
    "shot_type": ["Exterior", "Interior"],
    "make": MAKES,
    "angle": EXTERIOR_ANGLES,
    "interior_angle": INTERIOR_ANGLES,
    "lens": LENSES,
    "speed": SPEEDS,
    "vibe": list(VIBES),
    "lighting": list(LIGHTING),
    "int_material": LEATHERS,
    "int_detail": INT_DETAILS,
    "wheels": WHEELS,
    "time_of_day": TIMES,
    "weather": WEATHERS,
    "render_style": RENDER_STYLES,
    "mj_version": MJ_VERSIONS,
    "aspect": ASPECTS,
}
MULTI_CHOICES = {"sfx": SFX_OPTIONS, "negatives": NEGATIVE_OPTIONS}
BOOL_KEYS = ["motion_blur", "mj_raw"]
TEXT_KEYS = ["model", "finish", "custom_vehicle", "custom_paint", "custom_negative"]

RANDOM_KEYS = [
    "angle", "interior_angle", "lens", "speed", "vibe", "lighting",
    "int_material", "int_detail", "wheels", "time_of_day", "weather",
]

for _k, _v in DEFAULTS.items():
    st.session_state.setdefault(_k, list(_v) if isinstance(_v, list) else _v)
st.session_state.setdefault("presets", {})
st.session_state.setdefault("preset_error", False)


def ensure_model():
    """Keep the model valid for the selected make (e.g. after a preset load)."""
    ss = st.session_state
    if ss.make not in VEHICLES:
        ss.make = DEFAULTS["make"]
    if ss.model not in VEHICLES[ss.make]:
        ss.model = VEHICLES[ss.make][0]


def ensure_finish():
    """Keep the paint valid for the selected make."""
    ss = st.session_state
    options = paint_options(ss.make)
    if ss.finish not in options:
        ss.finish = options[0]


def on_make_change():
    ss = st.session_state
    ss.model = VEHICLES[ss.make][0]
    ss.finish = paint_options(ss.make)[0]


def random_vehicle():
    ss = st.session_state
    ss.make = random.choice([m for m in MAKES if m != CUSTOM])
    ss.model = random.choice(VEHICLES[ss.make])
    ss.finish = random.choice(paint_options(ss.make)[:-1])


def vehicle_name():
    ss = st.session_state
    if ss.make == CUSTOM:
        return ss.custom_vehicle.strip() or "sports car"
    return ss.model


ensure_model()
ensure_finish()


def is_valid(key, value):
    if key in SINGLE_CHOICES:
        return value in SINGLE_CHOICES[key]
    if key in MULTI_CHOICES:
        return isinstance(value, list) and all(v in MULTI_CHOICES[key] for v in value)
    if key in BOOL_KEYS:
        return isinstance(value, bool)
    if key in TEXT_KEYS:
        return isinstance(value, str)
    if key == "stylize":
        return isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 1000
    return False


def snapshot():
    return {k: (list(st.session_state[k]) if isinstance(st.session_state[k], list) else st.session_state[k])
            for k in SETTING_KEYS}


def apply_settings(data):
    if not isinstance(data, dict):
        return False
    for key, value in data.items():
        if key in SETTING_KEYS and is_valid(key, value):
            st.session_state[key] = list(value) if isinstance(value, list) else value
    ensure_model()
    ensure_finish()
    return True


def randomize():
    ss = st.session_state
    for key in RANDOM_KEYS:
        ss[key] = random.choice(SINGLE_CHOICES[key])
    ss["motion_blur"] = random.random() < 0.3
    ss["sfx"] = random.sample(SFX_OPTIONS, k=random.choice([0, 0, 1, 2]))


def save_preset():
    name = st.session_state.get("preset_name", "").strip()
    if name:
        st.session_state.presets[name] = snapshot()
        st.session_state["preset_name"] = ""


def load_preset():
    name = st.session_state.get("preset_choice")
    if name in st.session_state.presets:
        apply_settings(st.session_state.presets[name])


def delete_preset():
    name = st.session_state.get("preset_choice")
    st.session_state.presets.pop(name, None)


def load_from_file():
    f = st.session_state.get("preset_file")
    st.session_state["preset_error"] = False
    if f is None:
        return
    try:
        ok = apply_settings(json.load(f))
        st.session_state["preset_error"] = not ok
    except Exception:
        st.session_state["preset_error"] = True


# ---------------------------------------------------------------------------
# PAGE
# ---------------------------------------------------------------------------
st.title("🏎️ Automotive Director Suite: Cinematic Edition")
st.markdown("---")

# ---------------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------------
sb = st.sidebar
sb.radio("Shot Type", ["Exterior", "Interior"], key="shot_type", horizontal=True)
interior = st.session_state.shot_type == "Interior"

sb.button("🎲 Randomize look", on_click=randomize, use_container_width=True)

with sb.expander("🚘 Vehicle", expanded=True):
    st.selectbox("Make", MAKES, key="make", on_change=on_make_change)
    st.selectbox(
        "Model (type to search)", VEHICLES[st.session_state.make], key="model",
        disabled=st.session_state.make == CUSTOM,
    )
    st.text_input(
        "Custom vehicle", key="custom_vehicle", placeholder="e.g. 1967 Volvo P1800",
        disabled=st.session_state.make != CUSTOM,
    )
    st.button("🎲 Random vehicle", on_click=random_vehicle)

with sb.expander("📷 Camera & Motion", expanded=False):
    st.selectbox("Exterior Camera Angle", EXTERIOR_ANGLES, key="angle", disabled=interior)
    st.selectbox("Interior Camera Angle", INTERIOR_ANGLES, key="interior_angle", disabled=not interior)
    st.selectbox("Lens", LENSES, key="lens")
    st.toggle("Enable Motion Blur?", key="motion_blur", disabled=interior)
    st.select_slider(
        "Perceived Speed", options=SPEEDS, key="speed",
        disabled=interior or not st.session_state.motion_blur,
    )

with sb.expander("🎬 Vibe & Color Grade", expanded=False):
    st.selectbox("Color Grade", list(VIBES), key="vibe")
    st.radio("Render Style", RENDER_STYLES, key="render_style", horizontal=True)

with sb.expander("💡 Lighting Modifiers", expanded=False):
    st.selectbox("Lighting Style", list(LIGHTING), key="lighting")

with sb.expander("🔥 Physical Effects (SFX)", expanded=False):
    st.multiselect("Active Elements", SFX_OPTIONS, key="sfx", disabled=interior)

with sb.expander("🛋️ Interior Luxury", expanded=False):
    st.selectbox("Leather Type", LEATHERS, key="int_material")
    st.selectbox("Stitching/Finish", INT_DETAILS, key="int_detail")

with sb.expander("🚗 Exterior & Paint", expanded=False):
    st.selectbox("Paint", paint_options(st.session_state.make), key="finish")
    st.text_input(
        "Custom color", key="custom_paint", placeholder="e.g. Gulf Blue, satin olive wrap",
        disabled=st.session_state.finish != CUSTOM_PAINT,
    )
    st.selectbox("Wheels", WHEELS, key="wheels")

with sb.expander("☁️ Environment", expanded=False):
    st.selectbox("Time", TIMES, key="time_of_day")
    st.selectbox("Weather", WEATHERS, key="weather", disabled=interior)

with sb.expander("🚫 Avoid (Negative Prompt)", expanded=False):
    st.multiselect("Common problems to avoid", NEGATIVE_OPTIONS, key="negatives")
    st.text_input("Anything else (comma-separated)", key="custom_negative")

with sb.expander("⛵ Midjourney Settings", expanded=False):
    st.selectbox("Version", MJ_VERSIONS, key="mj_version")
    st.selectbox("Aspect Ratio", ASPECTS, key="aspect")
    st.slider("Stylize", 0, 1000, key="stylize")
    st.checkbox("Raw style (less 'Midjourney look')", key="mj_raw")

with sb.expander("💾 Presets", expanded=False):
    st.text_input("Preset name", key="preset_name")
    st.button("Save current settings", on_click=save_preset)
    if st.session_state.presets:
        st.selectbox("Saved presets", list(st.session_state.presets), key="preset_choice")
        c1, c2 = st.columns(2)
        c1.button("Load", on_click=load_preset)
        c2.button("Delete", on_click=delete_preset)
    st.caption("Presets last until you close the tab. Download to keep them.")
    st.download_button(
        "⬇️ Download settings (JSON)",
        data=json.dumps(snapshot(), indent=2),
        file_name="automotive_preset.json",
        mime="application/json",
    )
    st.file_uploader("Load settings file", type="json", key="preset_file")
    st.button("Apply uploaded file", on_click=load_from_file)
    if st.session_state.preset_error:
        st.warning("That file couldn't be read as a settings file.")

# ---------------------------------------------------------------------------
# PROMPT GENERATION
# ---------------------------------------------------------------------------
ss = st.session_state
vehicle = vehicle_name()
if ss.finish == CUSTOM_PAINT:
    paint_name = ss.custom_paint.strip() or "factory"
else:
    paint_name = ss.finish.replace(" (PTS)", "")
photographic = ss.render_style == "Photographic"

if interior:
    angle_used = ss.interior_angle
    subject_core = f"detailed luxury interior of a {vehicle}, {ss.int_material} with {ss.int_detail}"
    motion_desc = "Static shot, sharp focus."
    setting = f"Natural light through the windows, {ss.time_of_day}"
else:
    angle_used = ss.angle
    subject_core = f"{vehicle} in {paint_name} paint with {ss.wheels} wheels"
    if ss.sfx:
        subject_core += f", featuring {', '.join(ss.sfx).lower()}"
    if ss.motion_blur:
        motion_desc = (
            f"Panning motion shot at {ss.speed.lower()} pace, car body sharp, "
            "streaked background and blurred spinning wheels."
        )
    else:
        motion_desc = "Static shot, sharp focus, frozen moment."
    setting = f"{ss.time_of_day}, {ss.weather}"

vibe_desc = VIBES[ss.vibe]
light_desc = LIGHTING[ss.lighting]

negatives = list(ss.negatives)
negatives += [n.strip() for n in ss.custom_negative.split(",") if n.strip()]
neg_text = ", ".join(negatives)

# Nano Banana
if photographic:
    nano_intro = "A professional automotive photograph."
    nano_close = "True-to-life reflections, fine surface detail, cinematic advertising aesthetic."
else:
    nano_intro = "A high-end CGI automotive render."
    nano_close = "Ray-traced reflections, studio-grade render, cinematic advertising aesthetic."

nano_parts = [
    nano_intro,
    f"Angle: {angle_used}.",
    f"Lens: {ss.lens}.",
    f"Subject: {subject_core}.",
    motion_desc,
    f"Setting: {setting}.",
    f"Color grade: {vibe_desc}.",
    f"Lighting: {light_desc}.",
    nano_close,
]
if neg_text:
    nano_parts.append(f"Avoid: {neg_text}.")
nano_prompt = " ".join(nano_parts)

# Midjourney
mj_style = "photorealistic automotive photography" if photographic else "high-end CGI automotive render"
mj_prompt = ", ".join([
    subject_core, angle_used, ss.lens, motion_desc.rstrip("."), setting,
    vibe_desc, light_desc, mj_style,
])
mj_flags = f" --ar {ss.aspect} --v {ss.mj_version} --stylize {ss.stylize}"
if ss.mj_raw:
    mj_flags += " --style raw"
if neg_text:
    mj_flags += f" --no {neg_text}"
mj_prompt += mj_flags

# ---------------------------------------------------------------------------
# DISPLAY
# ---------------------------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
    st.subheader("🍌 Nano Banana 2")
    st.code(nano_prompt, language="text")
    st.caption(f"{len(nano_prompt.split())} words")
with col2:
    st.subheader("⛵ Midjourney")
    st.code(mj_prompt, language="text")
    st.caption(f"{len(mj_prompt.split())} words")

if interior:
    st.info("💡 Interior mode: exterior angles, weather, motion blur, and SFX are turned off. "
            "An 85mm lens gives nice depth of field on leather stitching.")
