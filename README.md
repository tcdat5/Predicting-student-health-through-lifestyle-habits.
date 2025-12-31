# Predicting Student Health through Lifestyle Habits
## 📝 1. Giới thiệu đề tài
Trong xã hội hiện đại, áp lực công việc và thói quen sinh hoạt không điều độ đang ảnh hưởng nghiêm trọng đến sức khỏe thế hệ trẻ. Dự án này tập trung vào việc **phân tích dữ liệu khảo sát** và xây dựng **hệ thống phân loại tự động** để xác định lối sống của cá nhân là **Healthy (Lành mạnh)** hay **Unhealthy (Cần cải thiện)**.

**Mục tiêu chính:**
1.  **Gán nhãn thông minh:** Sử dụng học máy không giám sát để tự động phân loại sức khỏe khi dữ liệu gốc chưa có nhãn.
2.  **Dự đoán chính xác:** Xây dựng mô hình phân lớp có khả năng dự đoán lối sống dựa trên thói quen hàng ngày.
3.  **Khám phá yếu tố then chốt:** Xác định các thói quen (Features) có ảnh hưởng lớn nhất đến sức khỏe tổng thể.

---

## 📊 2. Dataset
Dữ liệu được lấy từ nguồn **Kaggle - Wellbeing and Lifestyle Survey** với hơn 15,972 bản ghi.

### Các thuộc tính (Features) trong bộ dữ liệu:

| Tên thuộc tính | Mô tả |
| :--- | :--- |
| **FRUITS_VEGGIES** | Mức độ tiêu thụ trái cây và rau quả (thang điểm). |
| **DAILY_STRESS** | Mức độ căng thẳng hàng ngày (thang điểm). |
| **PLACES_VISITED** | Số lượng địa điểm đã ghé thăm. |
| **CORE_CIRCLE** | Số lượng người trong vòng kết nối cốt lõi. |
| **SUPPORTING_OTHERS** | Mức độ hỗ trợ người khác. |
| **SOCIAL_NETWORK** | Mức độ tương tác với mạng xã hội. |
| **ACHIEVEMENT** | Mức độ thành tựu cá nhân. |
| **DONATION** | Mức độ đóng góp hoặc từ thiện. |
| **BMI_RANGE** | Phạm vi Chỉ số khối cơ thể (BMI). |
| **TODO_COMPLETED** | Số lượng nhiệm vụ đã hoàn thành. |
| **FLOW** | Mức độ trải nghiệm 'dòng chảy' (độ tập trung). |
| **DAILY_STEPS** | Số bước đi hàng ngày. |
| **LIVE_VISION** | Mức độ có tầm nhìn rõ ràng về cuộc sống. |
| **SLEEP_HOURS** | Số giờ ngủ mỗi ngày. |
| **LOST_VACATION** | Số ngày nghỉ phép đã mất. |
| **DAILY_SHOUTING** | Mức độ la hét hoặc thể hiện sự tức giận. |
| **SUFFICIENT_INCOME** | Cá nhân có thu nhập đủ hay không. |
| **PERSONAL_AWARDS** | Số giải thưởng cá nhân nhận được. |
| **TIME_FOR_PASSION** | Lượng thời gian dành cho đam mê cá nhân. |
| **WEEKLY_MEDITATION** | Số lần thiền định hàng tuần. |
| **AGE** | Nhóm tuổi của cá nhân. |
| **GENDER** | Giới tính của cá nhân. |
| **WORK_LIFE_BALANCE_SCORE** | Điểm số cân bằng giữa công việc và cuộc sống. |

---

## ⚙️ 3. Pipeline Xử lý
Quy trình thực hiện được chuẩn hóa qua 4 bước:

1.  **Tiền xử lý (Preprocessing):** * Loại bỏ cột `Timestamp`.
    * Mã hóa biến định danh (`Gender`, `Age`) sang dạng số.
    * Xử lý dữ liệu nhiễu và chuẩn hóa dữ liệu bằng `StandardScaler`.
2.  **Gán nhãn (Labeling - Unsupervised):** * Ứng dụng **K-Means Clustering (k=2)**. 
    * Phân tích tâm cụm: Nhóm có chỉ số vận động cao và stress thấp được xác định là `1 (Healthy)`, ngược lại là `0 (Unhealthy)`.
3.  **Huấn luyện (Training):** Chia dữ liệu theo tỷ lệ 80% Train - 20% Test.
4.  **Đánh giá (Evaluation):** Kiểm chứng mô hình qua các chỉ số Accuracy, Precision, Recall và F1-Score.

---

## 4. 🤖 Mô hình sử dụng

Dự án thử nghiệm và so sánh 3 thuật toán phổ biến:

1.  **Logistic Regression:**
    * *Lý do chọn:* Là mô hình cơ sở (Baseline), đơn giản, tốc độ nhanh và dễ giải thích mức độ ảnh hưởng của các biến (Feature Importance).
2.  **K-Nearest Neighbors (KNN):**
    * *Lý do chọn:* Dựa trên nguyên lý "gần mực thì đen", so sánh người dùng với những mẫu dữ liệu giống họ nhất để đưa ra kết luận.
3.  **Decision Tree (Cây quyết định):**
    * *Lý do chọn:* Mô phỏng quy trình ra quyết định của con người (If-Else), dễ trực quan hóa và nắm bắt các luật (rules) phân loại.

---

## 5. 📈 Kết quả (Evaluation)

Kết quả đánh giá trên tập Test (20% dữ liệu):

| Metric | Logistic Regression | KNN (k=5) | Decision Tree |
| :--- | :---: | :---: | :---: |
| **Accuracy** | ~99% | ~94.8% | ~90.5% |
| **Precision** | ~100% | ~95% | ~90% |
| **Recall** | ~100% | ~95% | ~90% |
| **F1-Score** | ~100% | ~95% | ~90% |

> **Nhận xét:** Các mô hình đều đạt độ chính xác rất cao. Điều này là do nhãn mục tiêu (`HEALTHY_CLUSTER`) được sinh ra từ chính các đặc trưng đầu vào thông qua quy luật Clustering rõ ràng, giúp các mô hình Supervised Learning dễ dàng học được quy luật này.
---
## 6. 🚀 Hướng dẫn chạy dự án

### Bước 1: Cài đặt môi trường
Yêu cầu Python 3.8+. Cài đặt các thư viện cần thiết:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```
### Bước 2: Chuẩn bị dữ liệu
Đảm bảo file Wellbeing_and_lifestyle_data_Kaggle.csv nằm trong thư mục data/ của dự án.

### Bước 3: Chạy huấn luyện (Training)
Chạy file script chính để xử lý dữ liệu, huấn luyện mô hình và xem các chỉ số đánh giá:
```bash
python app/train.py
```

### Bước 4: Chạy Demo dự đoán (Inference)
Sau khi huấn luyện xong, hệ thống sẽ cho phép nhập thông tin cá nhân. 

## 📁 7. Cấu trúc thư mục dự án
```text
Lifestyle_Prediction_Project/
├── app/                  # Source code chính (xử lý & huấn luyện)
├── data/                 # Chứa file csv dữ liệu gốc
├── demo/                 # Script chạy thử dự đoán nhanh
├── models/               # Lưu trữ mô hình đã huấn luyện (.pkl)
├── reports/              # Báo cáo chi tiết (PDF/Word)
├── slides/               # Slide thuyết trình (PPT)
├── .gitignore            # File cấu hình git
├── requirements.txt      # Danh sách các thư viện cần cài đặt
└── README.md             # Hướng dẫn sử dụng dự án
```
## 8. 👤 Thông tin tác giả
Họ và tên: Trương Công Đạt

Mã sinh viên: 10123096

Lớp: 124231
