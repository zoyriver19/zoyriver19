import qrcode

# 你的网页链接
url = "https://zoyriver19.github.io/zoyriver19/"

# 创建QRCode对象
qr = qrcode.QRCode(
    version=1,  # 控制二维码的大小，1是最小的
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 控制二维码的错误纠正级别
    box_size=10,  # 控制二维码中每个小格子的像素数
    border=4,  # 控制二维码边框的宽度，默认为4
)

# 添加数据到QRCode对象
qr.add_data(url)
qr.make(fit=True)

# 创建图像
img = qr.make_image(fill='black', back_color='white')

# 保存图像
img.save("my_website_qrcode.png")