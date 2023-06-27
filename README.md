# Phân loại văn bản dựa trên tập mẫu có sẵn

Đây là hệ thông phân loại văn bản dựa trên một tập văn bản được cho sẵn

## Tính năng

- Phân loại một văn bản mới vào một chủ đề đã có tập văn bản mẫu có sẵn
- Không giới hạn số lượng chủ đề

## Công nghệ

- [Python] 
- [PhoBERT] - Sử dụng mô hình ngôn ngữ PhoBERT để embedding các câu
- [Cosine-Similarity] - Sử dụng độ đo cosine
## Yêu cầu
* Python 3.6+

## Cài đặt
Bước 1 : Download source code
```sh
git clone https://gitlab.aiacademy.edu.vn/research-develop/nlp/vosint_v3_document_clustering.git
cd ../vosint_v3_document_clustering
```

Bước 2 : Cài đặt các thư viện cần thiết 
```sh
pip install -r requirements.txt
```

Bước 3 : Khởi chạy dịch vụ
```sh
cd ../
python main.py
```

Lưu ý : cần sửa đường dẫn trong file sau 
```sh
../main.py (sys.path.append - đổi thành đường dẫn tuyệt đối)
```