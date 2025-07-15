# 💻 Laptop Price Predictor 🎯  
Predict the price of any laptop configuration using Machine Learning — all from your browser! Built using **Streamlit**, this app features dynamic UI, real-time predictions, and theme switching for a polished user experience.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white" alt="Streamlit Badge">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-Live-green" alt="Live Status">
</p>

---

## 🚀 Live Demo

🔗 **Try the App**:  
➡️➡️   [Laptop Price Prediction App](https://laptoppricepredictionapp-hdsgjt35ra9nrsbnhhnpwk.streamlit.app/)    ⬅️⬅️

📸 **Preview Screenshot**:  
<img width="100%" alt="App Screenshot" src="https://github.com/user-attachments/assets/21d672be-d21f-457d-9727-e1c2962e9e2f" />

---

## 🧠 Features

✅ Predicts laptop price based on:
- Brand, Type, RAM, Weight  
- Touchscreen, IPS Display, Screen Size & Resolution  
- CPU Brand, GPU Brand, HDD/SSD Storage  
- Operating System  

🎨 Stylish UI:
- Toggle between **Sky Blue 🌌** and **Light Green 🌿** themes  
- Responsive two-column layout for smoother input experience  
- Clean animations for enhanced user experience  

🧠 Powered by ML:
- Preprocessed & trained ML pipeline with `LinearRegression`
- Instant predictions with `scikit-learn` and `pickle`

---

## 🛠 Tech Stack

| Area       | Tech Used                  |
|------------|----------------------------|
| Frontend   | [Streamlit](https://streamlit.io) |
| Backend    | Scikit-learn, Pickle       |
| Language   | Python 3.9+                |
| ML Model   | Linear Regression + Pipeline |
| Libraries  | Pandas, NumPy, Sklearn     |

---

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/monissheikh1234/Laptop_Price_Prediction_App.git
   cd Laptop_Price_Prediction_App
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the Model**
   > Skip this step if `pipe.pkl` is already present
   ```bash
   python train_model.py
   ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

---

## 🌍 Deployment

> The app is deployed for free using **Streamlit Community Cloud**  
> You can deploy your own by:
- Forking this repo  
- Logging into [Streamlit Cloud](https://streamlit.io/cloud)  
- Connecting your GitHub and selecting this repo  
- Setting `app.py` as the entry point and deploying  

📖 Full deployment guide [here](https://docs.streamlit.io/streamlit-community-cloud)

---

## 📁 Project Structure

```
Laptop_Price_Prediction_App/
├── app.py                # Streamlit UI
├── train_model.py        # Data preprocessing & model training
├── pipe.pkl              # Trained ML model
├── df.pkl                # DataFrame for dropdowns
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork, open issues or submit pull requests.  
If you find this project useful, consider leaving a ⭐ on the repo.

---

## 🙋‍♂️ Author

Created by **[Monis Sheikh](https://github.com/monissheikh1234)**  
Connect on [LinkedIn]([https://www.linkedin.com/in/monis-sheikh](https://www.linkedin.com/in/monis-mustaque-sheikh-756096276/))

---

🧡 _Built with love, Python, and Streamlit_
