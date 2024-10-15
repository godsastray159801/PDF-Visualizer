
Dưới đây là phiên bản sửa lại của nội dung để rõ ràng hơn:

Hướng dẫn sử dụng PDF Analyzer
1. Giới thiệu
PDF Analyzer là một ứng dụng web được xây dựng bằng Streamlit, cho phép người dùng tải lên file PDF và nhận được phân tích chi tiết về nội dung tài liệu. Ứng dụng sử dụng API của Google Gemini để phân tích văn bản và trích xuất các từ khóa quan trọng.

2. Yêu cầu hệ thống
Python 3.7 trở lên
Pip (trình quản lý gói của Python)
3. Hướng dẫn cài đặt
Clone repository hoặc tạo một thư mục mới cho dự án.

Tạo môi trường ảo (được khuyến nghị):

bash
Sao chép mã
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
Cài đặt các thư viện cần thiết:

bash
Sao chép mã
pip install streamlit PyPDF2 google-generativeai python-dotenv pandas plotly
Tạo file .env trong thư mục dự án và thêm API key của Google Gemini:

bash
Sao chép mã
GOOGLE_API_KEY=your_api_key_here
4. Cấu trúc mã nguồn
Tạo file app.py và xây dựng với các bước sau:

Import các thư viện cần thiết.
Cấu hình API của Google Gemini.
Định nghĩa các hàm tiện ích:
extract_text_from_pdf(): Trích xuất văn bản từ file PDF.
call_gemini_api(): Gửi văn bản tới API Google Gemini.
analyze_research_document(): Phân tích tài liệu nghiên cứu.
extract_keywords(): Trích xuất từ khóa quan trọng.
generate_word_cloud(): Tạo biểu đồ đám mây từ khóa.
Định nghĩa hàm main() để xây dựng giao diện Streamlit.
Chạy ứng dụng với lệnh:
python
Sao chép mã
if __name__ == "__main__":
    main()
5. Chạy ứng dụng
Để khởi chạy ứng dụng, sử dụng lệnh sau trong terminal:

bash
Sao chép mã
streamlit run app.py
6. Hướng dẫn sử dụng
Truy cập vào ứng dụng: Mở trình duyệt và nhập địa chỉ được hiển thị trong terminal (thường là http://localhost:8501).

Giao diện ứng dụng: Ứng dụng sẽ hiển thị với tiêu đề "PDF Visualizer - Phân tích Nghiên cứu". Bạn có thể tải lên tệp PDF bằng cách nhấp vào nút "Browse files" hoặc kéo và thả tệp vào khu vực được chỉ định.

Quá trình phân tích: Sau khi tải lên tệp PDF, ứng dụng sẽ tự động thực hiện các bước sau:

Trích xuất văn bản từ PDF.
Gửi văn bản đến API Gemini để phân tích nội dung.
Trích xuất các từ khóa quan trọng từ tài liệu.
Tạo biểu đồ đám mây từ khóa.
Hiển thị kết quả:

Bên trái: Phân tích chi tiết nội dung với 5 mục chính.
Bên phải: Biểu đồ đám mây từ khóa quan trọng.
Tải xuống báo cáo: Ở cuối trang, nhấp vào nút "Tải báo cáo dạng TEXT" để tải xuống báo cáo đầy đủ dưới dạng file văn bản.

7. Xử lý lỗi và tối ưu hóa
Ứng dụng có cơ chế thử lại khi gặp lỗi từ API.
Hiển thị thông báo lỗi rõ ràng cho người dùng.
Sử dụng expander của Streamlit để tổ chức thông tin một cách gọn gàng.
8. Mở rộng và tùy chỉnh
Thay đổi mô hình phân tích: Điều chỉnh prompt trong hàm analyze_research_document() để thay đổi cách phân tích văn bản.
Tùy chỉnh giao diện: Sử dụng các component khác của Streamlit như st.sidebar, st.metrics, v.v.
Thêm tính năng mới: Ví dụ như so sánh nhiều tài liệu PDF, lưu lịch sử phân tích, hoặc tích hợp thêm các công cụ phân tích khác.
9. Kết luận
PDF Analyzer là một công cụ hữu ích để phân tích nhanh chóng các tài liệu nghiên cứu phức tạp. Với giao diện thân thiện và các tính năng xử lý thông minh, nó giúp tiết kiệm thời gian đáng kể trong việc tổng hợp và hiểu rõ nội dung của các tài liệu PDF.
