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

# --- Dữ liệu mô hình (dùng link imgbb) ---
models = {
    "Dragon Ball": [
        {"id": "DB01", "name": "Goku", "img": "https://i.ibb.co/J3h7X7B/goku.png"},
        {"id": "DB02", "name": "Vegeta", "img": "https://i.ibb.co/4Zb5KwT/vegeta.png"},
        {"id": "DB03", "name": "Gohan", "img": "https://i.ibb.co/FY4R6Vn/gohan.png"}
    ],
    "Naruto": [
        {"id": "NA01", "name": "Naruto", "img": "https://i.ibb.co/vmckP6H/naruto.png"},
        {"id": "NA02", "name": "Sasuke", "img": "https://i.ibb.co/2Mhb9Kb/sasuke.png"},
        {"id": "NA03", "name": "Kakashi", "img": "https://i.ibb.co/DGpNGWb/kakashi.png"}
    ],
    "One Piece": [
        {"id": "OP01", "name": "Luffy", "img": "https://i.ibb.co/5McC4Gt/luffy.png"},
        {"id": "OP02", "name": "Zoro", "img": "https://i.ibb.co/wdKCFbH/zoro.png"},
        {"id": "OP03", "name": "Nami", "img": "https://i.ibb.co/VpdWJ7M/nami.png"}
    ]
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


