# Predicting-student-health-through-lifestyle-habits.
## 1. Giới thiệu đề tài
* **Bài toán:** Trong xã hội hiện đại, áp lực công việc và thói quen sinh hoạt ảnh hưởng lớn đến sức khỏe. Dự án này nhằm mục đích phân tích dữ liệu khảo sát và xây dựng mô hình Machine Learning để tự động phân loại lối sống là **Healthy (Lành mạnh)** hay **Unhealthy (Cần cải thiện)**.
* **Mục tiêu:**
    1. Phân cụm dữ liệu để gán nhãn sức khỏe (do dữ liệu gốc chưa có nhãn).
    2. Huấn luyện các mô hình phân lớp (Classification) để dự đoán.
    3. Xác định các yếu tố ảnh hưởng nhất (Feature Importance).

## 2. Dataset
* **Nguồn dữ liệu:** Kaggle - Wellbeing and Lifestyle Survey.
* **Mô tả:** Bộ dữ liệu chứa ~16,000 bản ghi khảo sát về thói quen hàng ngày.
* **Mô tả các thuộc tính (Features):**
Timestamp: Ngày và giờ dữ liệu được ghi lại.
FRUITS_VEGGIES: Mức độ tiêu thụ trái cây và rau quả (có thể là thang điểm).
DAILY_STRESS: Mức độ căng thẳng hàng ngày (có thể là thang điểm).
PLACES_VISITED: Số lượng địa điểm đã ghé thăm.
CORE_CIRCLE: Số lượng người trong vòng kết nối cốt lõi của một người.
SUPPORTING_OTHERS: Mức độ hỗ trợ người khác (có thể là thang điểm).
SOCIAL_NETWORK: Mức độ tương tác với mạng xã hội (có thể là thang điểm).
ACHIEVEMENT: Mức độ thành tựu cá nhân (có thể là thang điểm).
DONATION: Mức độ đóng góp hoặc từ thiện (có thể là thang điểm).
BMI_RANGE: Phạm vi Chỉ số khối cơ thể (BMI) (có thể được phân loại).
TODO_COMPLETED: Số lượng nhiệm vụ đã hoàn thành.
FLOW: Mức độ trải nghiệm 'dòng chảy' (trạng thái hoàn toàn tập trung vào một hoạt động, có thể là thang điểm).
DAILY_STEPS: Số bước đi hàng ngày.
LIVE_VISION: Mức độ có tầm nhìn rõ ràng về cuộc sống (có thể là thang điểm).
SLEEP_HOURS: Số giờ ngủ mỗi ngày.
LOST_VACATION: Số ngày nghỉ phép đã mất.
DAILY_SHOUTING: Mức độ la hét hoặc thể hiện sự tức giận hàng ngày (có thể là thang điểm).
SUFFICIENT_INCOME: Cá nhân có thu nhập đủ hay không (có thể là thang nhị phân hoặc thang điểm).
PERSONAL_AWARDS: Số giải thưởng cá nhân nhận được.
TIME_FOR_PASSION: Lượng thời gian dành cho đam mê cá nhân (có thể là thang điểm).
WEEKLY_MEDITATION: Số lần thiền định hàng tuần.
AGE: Nhóm tuổi của cá nhân.
GENDER: Giới tính của cá nhân.
WORK_LIFE_BALANCE_SCORE: Điểm số được tính toán đại diện cho sự cân bằng giữa công việc và cuộc sống.

  

## 3. Pipeline Xử lý
Quy trình thực hiện dự án (Workflow):

1. **Tiền xử lý (Preprocessing):**
   * Loại bỏ cột `Timestamp`.
   * Mã hóa dữ liệu định danh (`Gender`, `Age`) sang dạng số.
   * Xử lý dữ liệu nhiễu và chuẩn hóa dữ liệu (`StandardScaler`).
   
2. **Gán nhãn (Labeling - Unsupervised):**
   * Sử dụng thuật toán **K-Means Clustering** (với k=2) để chia dữ liệu thành 2 nhóm.
   * Phân tích tâm cụm: Nhóm có vận động cao, stress thấp được gán nhãn `1 (Healthy)`, ngược lại là `0 (Unhealthy)`.

3. **Huấn luyện (Training):**
   * Chia dữ liệu: 80% Train - 20% Test.
   * Huấn luyện trên 3 mô hình: Logistic Regression, Decision Tree, Random Forest.

4. **Đánh giá (Evaluation):**
   * Sử dụng các chỉ số: Accuracy, Precision, Recall, F1-Score.

## 4. Mô hình sử dụng & Kết quả
Dự án đã thử nghiệm 3 thuật toán và kết quả trên tập Test như sau:

| Mô hình | Accuracy | Lý do chọn |
|:---|:---:|:---|
| **Logistic Regression** | ~98% | Mô hình cơ sở, dễ giải thích trọng số, nhanh. |
| **Decision Tree** | ~97% | Mô phỏng quy luật if-else, dễ trực quan hóa. |
| **Random Forest** | **~99%** | **(Chọn)** Kết hợp nhiều cây quyết định, chống overfitting tốt nhất. |

*(Lưu ý: Accuracy cao do nhãn được sinh ra từ quy luật Clustering rõ ràng)*

## 5. Cấu trúc thư mục dự án
Lifestyle_Prediction_Project/ ├── app/ # Source code chính ├── data/ # Chứa file csv dữ liệu ├── demo/ # Script chạy thử dự đoán ├── models/ # Chứa model đã train (.pkl) ├── reports/ # Báo cáo chi tiết (PDF/Word) ├── slides/ # Slide thuyết trình (PPT) ├── requirements.txt # Thư viện cần thiết └── README.md # Hướng dẫn sử dụng

## 6. Hướng dẫn chạy dự án

Hướng dẫn chạy dự án

Hướng dẫn chạy dự án
Để chạy được dự án này trên máy tính cá nhân, bạn vui lòng thực hiện theo các bước sau:

1. Chuẩn bị môi trường
Yêu cầu: Máy tính đã cài đặt Python phiên bản 3.8 trở lên.
Tải mã nguồn: Bạn có thể tải file .zip hoặc sử dụng lệnh git để clone project:
Bash
git clone https://github.com/vinh-le/Lifestyle_Prediction_Project.git
cd Lifestyle_Prediction_Project

2. Cài đặt các thư viện cần thiết
Sử dụng công cụ pip để cài đặt các thư viện được liệt kê trong file requirements.txt (bao gồm pandas, scikit-learn, joblib...):
Bash
pip install -r requirements.txt

3. Chuẩn bị dữ liệu
Đảm bảo file dữ liệu Wellbeing_and_lifestyle_data_Kaggle.csv đã nằm trong thư mục data/.
Nếu chưa có, bạn có thể tải từ nguồn Kaggle và copy vào thư mục này.

4. Huấn luyện mô hình (Train)
Trước khi dự đoán, bạn cần chạy script huấn luyện để mô hình học dữ liệu và lưu lại các file trọng số vào thư mục models/:
python -m app.train
Kết quả: Sau khi chạy, bạn sẽ thấy các file best_model.pkl, scaler.pkl và features.pkl xuất hiện trong thư mục models/.

5. Chạy Demo dự đoán (Inference)
Sau khi đã huấn luyện xong, bạn có thể chạy script demo để nhập thông tin cá nhân và nhận kết quả dự đoán trực tiếp từ mô hình:
python demo/demo_inference.py

## 7. Thông tin tác giả
Họ và tên: Trương Công Đạt
Mã sinh viên: 10123096
Lớp: 124231

