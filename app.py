import streamlit as st

st.title("Vin-input app 🍷")

# --- 1️⃣ Velg type vin ---
wine_type = st.radio(
    "Velg vintype:",
    ["Hvit", "Rød"],
    index=0,
    horizontal=True
)

# --- 2️⃣ Skriv inn 11 numeriske verdier ---
st.subheader("Skriv inn 11 måleverdier:")

# Opprett 11 felter for double/float input
verdier =  [
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    "chlorides", "free sulfur dioxide", "total sulfur dioxide",
    "density", "pH", "sulphates", "alcohol"
]

inputs = []
for i in range(1, 12):
    value = st.number_input(
        verdier[i-1],
        value=0.0,
        step=0.1,
        format="%.2f"
    )
    inputs.append(value)

# --- 3️⃣ Vis resultatet ---
st.divider()
st.write("### Dine valg:")
st.write(f"**Vintype:** {wine_type}")
st.write(f"**Verdier (11 stk):** {inputs}")

output = 0
for i in inputs:
    output += i

st.write(f"Output = {output:.2f}")
