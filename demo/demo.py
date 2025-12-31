import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

# ===============================
# CẤU HÌNH GIAO DIỆN
# ===============================
st.set_page_config(
    page_title="Dự đoán sức khỏe sinh viên",
    page_icon="💙",
    layout="centered"
)

st.title("💙 Dự đoán sức khỏe sinh viên")

# ===============================
# LOAD & XỬ LÝ DỮ LIỆU
# ===============================
@st.cache_data
def load_data():
    df = pd.read_csv("Wellbeing_and_lifestyle_data_Kaggle.csv")

    # Lọc độ tuổi sinh viên
    df = df[df['AGE'].isin(['Less than 20', '21 to 35'])].copy()

    df['AGE'] = df['AGE'].map({'Less than 20': 0, '21 to 35': 1})
    df['GENDER'] = df['GENDER'].map({'Female': 0, 'Male': 1})

    # Stress
    df['DAILY_STRESS'] = pd.to_numeric(df['DAILY_STRESS'], errors='coerce')
    df['DAILY_STRESS'].fillna(df['DAILY_STRESS'].mean(), inplace=True)

    # ===============================
    # DAILY STEPS → 1–10 (nghìn bước)
    # ===============================
    df['DAILY_STEPS'] = pd.to_numeric(df['DAILY_STEPS'], errors='coerce')
    df['DAILY_STEPS'] = df['DAILY_STEPS'].clip(1, 10)
    df['DAILY_STEPS'].fillna(df['DAILY_STEPS'].median(), inplace=True)

    return df

df = load_data()

# ===============================
# FEATURE
# ===============================
features = [
    'BMI_RANGE',
    'DAILY_STRESS',
    'DAILY_STEPS',     # 1–10 nghìn bước
    'SLEEP_HOURS',
    'FRUITS_VEGGIES',
    'TIME_FOR_PASSION',
    'ACHIEVEMENT',
    'FLOW',
    'LIVE_VISION',
    'PERSONAL_AWARDS'
]

X = df[features]

# ===============================
# KMEANS – TẠO NHÃN SỨC KHỎE
# ===============================
scaler_cluster = StandardScaler()
X_cluster = scaler_cluster.fit_transform(X)

kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
df["CLUSTER"] = kmeans.fit_predict(X_cluster)

cluster_summary = df.groupby("CLUSTER")[[
    "DAILY_STEPS",
    "SLEEP_HOURS",
    "FRUITS_VEGGIES",
    "DAILY_STRESS"
]].mean()

healthy_cluster = (
    cluster_summary["DAILY_STEPS"]
    + cluster_summary["SLEEP_HOURS"]
    + cluster_summary["FRUITS_VEGGIES"]
    - cluster_summary["DAILY_STRESS"]
).idxmax()

y = (df["CLUSTER"] == healthy_cluster).astype(int)

# ===============================
# TRAIN LOGISTIC REGRESSION
# ===============================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression(C=0.5, max_iter=1000)
model.fit(X_scaled, y)

# ===============================
# GIAO DIỆN NHẬP LIỆU
# ===============================
st.subheader("📌 Nhập thông tin cá nhân")

col1, col2 = st.columns(2)

with col1:
    bmi = st.selectbox("BMI (1: bình thường, 2: thừa cân)", [1, 2])
    stress = st.slider("Mức độ stress (0–5)", 0, 5, 2)
    steps = st.selectbox("Số bước mỗi ngày (nghìn bước)", list(range(1, 11)))
    sleep = st.slider("Số giờ ngủ", 0.0, 12.0, 7.0)

with col2:
    fruits = st.slider("Rau củ / trái cây (0–5)", 0, 5, 3)
    passion = st.slider("Thời gian cho đam mê (giờ/ngày)", 0.0, 10.0, 2.0)
    achievement = st.slider("Cảm giác thành tựu (0–10)", 0, 10, 5)
    flow = st.slider("Trạng thái Flow (0–10)", 0, 10, 5)
    vision = st.slider("Tầm nhìn cuộc sống (0–10)", 0, 10, 6)
    awards = st.number_input("Số giải thưởng", 0, 20, 0)

# ===============================
# DỰ ĐOÁN
# ===============================
if st.button("🔍 Dự đoán sức khỏe"):

    user_data = pd.DataFrame([[ 
        bmi, stress, steps, sleep, fruits,
        passion, achievement, flow, vision, awards
    ]], columns=features)

    user_scaled = scaler.transform(user_data)
    prediction = model.predict(user_scaled)
    prob = model.predict_proba(user_scaled)

    st.subheader("📊 Kết quả dự đoán")

    if prediction[0] == 1:
        st.success("✅ Bạn thuộc nhóm **LỐI SỐNG LÀNH MẠNH**")
        st.write(f"Độ tin cậy ước lượng: **{min(prob[0][1], 0.95)*100:.2f}%**")
    else:
        st.error("⚠️ Bạn thuộc nhóm **CẦN CẢI THIỆN SỨC KHỎE**")
        st.write(f"Độ tin cậy ước lượng: **{min(prob[0][0], 0.95)*100:.2f}%**")

    # ===============================
    # GỢI Ý CẢI THIỆN
    # ===============================
    st.subheader("💡 Gợi ý cải thiện lối sống")

    suggestions = []
    
    if bmi == 2:
        suggestions.append(
        "Bạn đang ở nhóm thừa cân, nên kết hợp ăn uống lành mạnh "
        "và vận động thường xuyên để giảm nguy cơ tim mạch và mệt mỏi."
    )
    if stress >= 3:
        suggestions.append("🧠 Giảm stress: thiền, tập thở sâu, quản lý thời gian học tập.")

    if steps <= 3:
        suggestions.append("🚶 Tăng vận động: nên đi ít nhất 6.000–8.000 bước/ngày.")

    if fruits <= 2:
        suggestions.append("🥦 Bổ sung rau củ & trái cây mỗi ngày.")

    if sleep < 6:
        suggestions.append("😴 Ngủ đủ 7–8 giờ để phục hồi thể chất & tinh thần.")

    if suggestions:
        for s in suggestions:
            st.write("- " + s)
    else:
        st.success("🎉 Lối sống của bạn đang rất tốt, hãy tiếp tục duy trì!")
