# 🚀 Advanced-Data-Science-Internship-Projects


### **Nascent IT Ventures | Month 2 Portfolio**

Welcome to my repository! This collection showcases end-to-end Data Science solutions developed during my internship at **Nascent IT Ventures**. The projects span across Computer Vision, Predictive Modeling, and Natural Language Processing (NLP).

---

## 🛠️ Tech Stack

* **Languages:** Python (Pandas, NumPy, Scikit-Learn)
* **Computer Vision:** OpenCV
* **NLP:** NLTK, XGBoost, TF-IDF
* **Visualization:** Matplotlib, Seaborn
* **Tools:** Jupyter Notebook, Git, Joblib

---

## 📁 Projects Overview (Sequential)

### 1. 🎥 Real-Time Object Counter (OpenCV)

**Objective:** Real-time detection and counting of moving objects in a video stream.

* **Process:** Implemented Background Subtraction (MOG2), Contour Detection, and Centroid Tracking.
* **Output:** Generates an `annotated_output.avi` video featuring a Live Object Counter HUD.

### 2. 🎨 Image Cartoonifier (OpenCV)

**Objective:** Transform standard photographs into stylized cartoon or watercolor-style art using image processing.

* **Techniques:** Bilateral filtering (to smooth colors while preserving edges) and Adaptive Thresholding (to create the "sketch" effect).
* **Key Features:** Modular Python script with command-line arguments for different styles.

### 3. 🎭 Sentiment Analysis System (NLP)

**Objective:** Classify user feedback/reviews into Positive or Negative sentiments.

* **Approach:** Used TF-IDF Vectorization for text-to-numeric conversion followed by Logistic Regression.
* **Evaluation:** Includes a Confusion Matrix heatmap to visualize model performance.

### 4. 🛡️ Spam Detection System (NLP)

**Objective:** An intelligent classification system to distinguish between 'Ham' and 'Spam' messages.

* **Algorithms:** Comparative study between Random Forest and XGBoost.
* **Achievement:** Achieved high Precision to ensure legitimate emails never land in the spam folder.

### 5. 📉 Customer Churn Analytics & Prediction

**Objective:** Analyze customer behavior to predict potential churn for a subscription-based service.

* **Model:** Random Forest & XGBoost.
* **Highlights:** Extensive Feature Engineering (Tenure, Contract Type) and handling class imbalance using weight balancing.
* **Metric focus:** Optimized for Recall to identify every possible at-risk customer.
