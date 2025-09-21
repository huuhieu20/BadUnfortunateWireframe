import streamlit as st

# --- Sidebar ---
st.sidebar.title("Cửa hàng mô hình Anime")
st.sidebar.info(
    """
    📍 Địa chỉ: 123 Đường ABC, Hà Nội  
    📞 SĐT: 0987 654 321  
    📧 Email: shop@anime.vn
    """
)

# --- Tiêu đề chính ---
st.title("🛒 Chương trình quản lý cửa hàng đồ chơi")

# --- Các chủ đề ---
st.subheader("Chọn chủ đề mô hình:")
option = st.radio("Chủ đề", ["Dragon Ball", "Naruto", "One Piece"])

# --- Dữ liệu mô hình ---
models = {
    "Dragon Ball": [
        {"id": "DB01", "name": "Goku", "img": "https://i.imgur.com/OUq8H0z.png"},
        {"id": "DB02", "name": "Vegeta", "img": "https://i.imgur.com/pzXy7eJ.png"},
        {"id": "DB03", "name": "Gohan", "img": "https://i.imgur.com/43QqfT7.png"}
    ],
    "Naruto": [
        {"id": "NA01", "name": "Naruto", "img": "https://i.imgur.com/oF0y8fZ.png"},
        {"id": "NA02", "name": "Sasuke", "img": "https://i.imgur.com/3P1DOrC.png"},
        {"id": "NA03", "name": "Kakashi", "img": "https://i.imgur.com/sUQNdwR.png"}
    ],
    "One Piece": [
        {"id": "OP01", "name": "Luffy", "img": "https://i.imgur.com/hncvH5o.png"},
        {"id": "OP02", "name": "Zoro", "img": "https://i.imgur.com/rV8pp3M.png"},
        {"id": "OP03", "name": "Nami", "img": "https://i.imgur.com/7gQzZqv.png"}
    ]

    ],
}

# --- Hiển thị danh sách mô hình ---
st.subheader(f"Danh sách mô hình: {option}")
cols = st.columns(3)
for i, model in enumerate(models[option]):
    with cols[i % 3]:
        st.image(model["img"], caption=f"{model['name']} (Mã: {model['id']})", use_container_width=True)

# --- Form đặt hàng ---
st.subheader("📝 Đặt hàng")
with st.form("order_form"):
    model_id = st.text_input("Nhập mã mô hình")
    quantity = st.number_input("Số lượng", min_value=1, value=1)
    name = st.text_input("Họ và tên")
    phone = st.text_input("Số điện thoại")
    address = st.text_area("Địa chỉ giao hàng")
    submit = st.form_submit_button("Xác nhận đặt hàng")

if submit:
    if model_id and name and phone and address:
        st.success("✅ Đặt hàng thành công!")
        st.write("### Hóa đơn")
        st.write(f"- Mã mô hình: {model_id}")
        st.write(f"- Số lượng: {quantity}")
        st.write(f"- Khách hàng: {name}")
        st.write(f"- SĐT: {phone}")
        st.write(f"- Địa chỉ: {address}")
        st.write("Cảm ơn bạn đã mua hàng 🛍️")
    else:
        st.error("⚠️ Vui lòng nhập đầy đủ thông tin trước khi xác nhận.")

