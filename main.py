import streamlit as st

st.title("📚 Quản lý Thời khóa biểu")

# Dữ liệu thời khóa biểu
timetable = {
    "Thứ Hai": ["Toán", "Ngữ văn", "Tiếng Anh", "Vật lý"],
    "Thứ Ba": ["Hóa học", "Sinh học", "Lịch sử", "Địa lý"],
    "Thứ Tư": ["Toán", "Tin học", "Ngữ văn", "Thể dục"],
    "Thứ Năm": ["Tiếng Anh", "Vật lý", "Công nghệ", "GDCD"],
    "Thứ Sáu": ["Toán", "Ngữ văn", "Hóa học", "Lịch sử"],
    "Thứ Bảy": ["Sinh học", "Địa lý", "Tin học", "Thể dục"],
    "Chủ Nhật": ["Nghỉ học 🎉"]
}

# Selectbox chọn ngày
day = st.selectbox("Chọn ngày trong tuần:", list(timetable.keys()))

# Hiển thị môn học
st.subheader(f"📅 Thời khóa biểu {day}:")
for i, subject in enumerate(timetable[day], start=1):
    st.write(f"{i}. {subject}")
