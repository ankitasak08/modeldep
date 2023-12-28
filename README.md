# 🛸 UFO Country Prediction with Logistic Regression and Flask

Welcome to the UFO Country Prediction project! In this beginner-level project, I explored the deployment of a machine learning model that predicts the country where UFO sightings have been reported over the past century. The model is built using the logistic regression algorithm, and the entire application is deployed using Flask and Streamlit.

## Project Overview

This project encompasses the following key aspects:

1. **Logistic Regression Implementation:**
   - The machine learning model is constructed using the logistic regression algorithm.
   - Practical implementation on the dataset is carried out to predict the country of UFO sightings.

2. **Flask as a Framework:**
   - Flask, a lightweight web framework for Python, is employed to build the web application.
   - Flask is chosen for its simplicity and ease of integration with machine learning models.

3. **Frontend Development with HTML and CSS:**
   - To enhance user interaction, basic HTML and CSS are utilized for frontend development.
   - The use of these technologies adds a visual appeal to the web application.

4. **Interactive Model Presentation:**
   - The goal is to make the model more interactive for users.
   - Through the integration of HTML, CSS, and Flask, the frontend provides an engaging interface.

5. **Deployment with Streamlit:**
   - Streamlit is selected as the deployment environment to showcase the machine learning model on the web.
   - Streamlit's simplicity and effectiveness make it an ideal choice for beginners.

6. **Learning Experience:**
   - This project serves as a major learning experience for beginners in machine learning and web development.
   - The deployment process exposes users to various technologies, enriching their understanding of end-to-end project implementation.

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your-username/ufo-country-prediction.git
   cd ufo-country-prediction
   ```

2. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application.
   ```bash
   python app.py
   ```
   Visit `http://localhost:5000` in your web browser to interact with the UFO Country Prediction web application.

## Project Structure

- `logregmodel.ipynb` : Jupyter Notebook file containing the implementation and analysis of the logistic regression model.

- `mod.py` : Python script containing the implementation of the logistic regression model in a modularized form.

- `requirements.txt`: File specifying the required Python packages and dependencies. Install them using the command pip install -r requirements.txt.

- `ufo-model.pkl` : Pickle file containing the trained logistic regression model. This file is used in the deployment phase to make predictions.

- `ufodata.csv` : CSV file containing the dataset of UFO sightings, which is used for training and testing the machine learning model.

## Acknowledgments

This project is inspired by the desire to integrate machine learning with web development.

Feel free to explore, contribute, and enhance this project further. Happy coding! 🚀
