import streamlit as st

st.title("🥤 Trang web đặt đồ uống")

# Tạo form
with st.form("order_form"):
    # 3 lựa chọn
    drink = st.selectbox("Chọn loại đồ uống:", ["Trà sữa", "Cà phê", "Nước ép"])
    sugar = st.selectbox("Chọn loại đường:", ["Ít đường", "Vừa ngọt", "Nhiều đường"])
    topping = st.selectbox("Chọn loại thạch:", ["Không thạch", "Thạch trái cây", "Trân châu"])

    # Checkbox in hóa đơn
    print_invoice = st.checkbox("In hóa đơn")

    # Nút Submit
    submitted = st.form_submit_button("Submit")

# Xử lý kết quả
if submitted:
    st.success(f"👉 Bạn đã chọn: {drink}, {sugar}, {topping}")

    # Nếu chọn in hóa đơn thì hiện nút tải xuống
    if print_invoice:
        invoice_text = f"HÓA ĐƠN\nĐồ uống: {drink}\nĐường: {sugar}\nThạch: {topping}"
        st.download_button(
            label="In hóa đơn",
            data=invoice_text,
            file_name="hoa_don.txt",
            mime="text/plain"
        )
