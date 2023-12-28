import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('ufo-model.pkl', 'rb'))

def predict(input_features):
    # Convert input features to numeric types
    numeric_features = [float(feature) for feature in input_features]
    return model.predict([np.array(numeric_features)])[0]

def main():
    st.set_page_config(page_title="UFO Prediction App", page_icon="👽")
    
    st.markdown("""
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Helvetica', sans-serif;
                background-color: #505050; 
                color: #333;
                text-align: center;
            }

            .grid {
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }

            .box {
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                padding: 20px;
                border-radius: 8px;
                max-width: 400px;
                width: 100%;
                text-align: left;
            }

            .box p {
                font-size: 1.2em;
                margin-bottom: 20px;
            }

            form {
                display: flex;
                flex-direction: column;
            }

            input {
                width: 100%;
                padding: 10px;
                margin-bottom: 16px;
                font-size: 1em;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 4px;
            }

            button {
                background: #4CAF50;
                color: #fff;
                padding: 12px 20px;
                font-size: 1.2em;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }

            button:hover {
                background: #45a049;
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("🛸 UFO Appearance Prediction!")
    st.write("According to the number of seconds, latitude, and longitude, which country is likely to have reported seeing a UFO?")

    seconds = st.number_input("Seconds", min_value=0, max_value=60, step=1)
    latitude = st.text_input("Latitude", "")
    longitude = st.text_input("Longitude", "")

    if st.button("Predict country where the UFO is seen"):
        prediction_text = f"The most likely country is : {['Australia', 'Canada', 'Germany', 'UK', 'US'][predict([seconds, latitude, longitude])]}"
        st.write(prediction_text)

if __name__ == "__main__":
    main()
