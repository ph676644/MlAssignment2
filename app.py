import streamlit as st
from wine_quality_predictor import predict_white, predict_red

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

verdier = [
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    "chlorides", "free sulfur dioxide", "total sulfur dioxide",
    "density", "pH", "sulphates", "alcohol"
]

inputs = []
for navn in verdier:
    value = st.number_input(
        navn,
        value=0.0,
        step=0.1,
        format="%.2f"
    )
    inputs.append(value)

# --- 3️⃣ Beregning etter knappetrykk ---
st.divider()
st.write("### Dine valg:")
st.write(f"**Vintype:** {wine_type}")

# Legg til knapp
if st.button("Beregn"):
    # Rund av verdier til 2 desimaler
    rounded_inputs = [round(v, 2) for v in inputs]

    try:
        if wine_type == "Hvit":
            predicted_quality = predict_white(rounded_inputs)
        else:
            predicted_quality = predict_red(rounded_inputs)

        st.write(f"**Verdier (11 stk):** {rounded_inputs}")
        st.success(f"🍷 Predikert vin-kvalitet: {predicted_quality:.2f}")

    except Exception as e:
        st.error(f"Noe gikk galt under prediksjonen: {e}")

else:
    st.info("Trykk på 'Beregn' for å vise resultatet.")
