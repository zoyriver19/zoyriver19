import qrcode
from PIL import Image, ImageDraw

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

# 打开图标图像
icon = Image.open("static\images\douyin.jpg")  # 确保你有一个名为 douyin.jpg 的图标文件

# 确保图标是RGBA模式（包含透明度通道）
if icon.mode != 'RGBA':
    icon = icon.convert('RGBA')

# 计算图标的位置
img_w, img_h = img.size
icon_w, icon_h = icon.size

# 调整图标大小，确保不会覆盖过多的二维码数据
icon_size = int(img_w * 0.2)
icon = icon.resize((icon_size, icon_size), Image.LANCZOS)
icon_w, icon_h = icon.size

# 计算图标的位置，确保不完全覆盖二维码中心
icon_x = (img_w - icon_w) // 2
icon_y = (img_h - icon_h) // 2

# 创建一个与二维码相同大小的RGBA图像
img_with_icon = Image.new('RGBA', (img_w, img_h), (255, 255, 255, 0))
img_with_icon.paste(img, (0, 0))

# 将图标粘贴到二维码中间，但不完全覆盖
img_with_icon.paste(icon, (icon_x, icon_y), icon)

# 将带有图标的二维码转换回RGB模式
img_with_icon = img_with_icon.convert('RGB')

# 保存图像
img_with_icon.save("my_website_qrcode.png")