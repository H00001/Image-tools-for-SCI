from PIL import Image, ImageDraw, ImageFont

# 假设有15个PNG文件，按文件名放入一个列表
png_files = [f"./ACCESS/input/{i}.png" for i in range(1, 16)]

# 加载所有PNG文件为PIL图像
images = [Image.open(file) for file in png_files]

# 假设每个PNG的尺寸相同
width, height = images[0].size

# 创建一个新图像，大小为3行5列
new_image = Image.new('RGBA', (width * 5, height * 3 + 200), (255, 255, 255, 255))  # 背景设置为透明

# 创建绘图对象用于添加文本
draw = ImageDraw.Draw(new_image)

# 加载一个字体（指定字体路径，确保字体支持）
try:
    font = ImageFont.truetype("arial.ttf", size=100)  # 使用 Arial 字体
except IOError:
    font = ImageFont.load_default()  # 如果没有 Arial 字体，使用默认字体

# 添加顶部边框
border_color = (0, 0, 0)  # 边框颜色
border_width = 5  # 边框宽度

li = ["COX2", "BZR", "IMDB-BINARY", "COLLAB", "Letter-low"]



draw.text((0 * width + 420, height * 3 + 10), li[0], fill=(0, 0, 0), font=font)
draw.text((1 * width + 510, height * 3 + 10), li[1], fill=(0, 0, 0), font=font)
draw.text((2 * width + 330, height * 3 + 10), li[2], fill=(0, 0, 0), font=font)
draw.text((3 * width + 450, height * 3 + 10), li[3], fill=(0, 0, 0), font=font)
draw.text((4 * width + 490, height * 3 + 10), li[4], fill=(0, 0, 0), font=font)


for i in range(3):
    for j in range(5):
        index = i * 5 + j
        x_offset = j * width
        y_offset = i * height


        if i == 2 and j == 2:
            # 将图像粘贴到新图像中
            new_image.paste(images[index], (x_offset, y_offset + 50))
        else:
            # 将图像粘贴到新图像中
            new_image.paste(images[index], (x_offset, y_offset))

# 显示最终拼接的图像

for i in range(3):
    for j in range(5):
        index = i * 5 + j
        x_offset = j * width
        y_offset = i * height

        # 在图像周围绘制边框
        draw.rectangle(
            [x_offset - border_width, y_offset - border_width, x_offset + width + border_width, y_offset + height + border_width],
            outline=border_color,
            width=border_width
        )
draw.rectangle(
    [0, 0, width * 5, 10],  # 顶部边框的坐标
    fill=border_color
)

draw.line(
    [00, 2900, 6500, 2900], width=12,  # 顶部边框的坐标
    fill=border_color
)
new_image.show()

# 保存最终图像
# new_image.save("./ACCESS/output/comb-tsen.png", dpi=(600, 600))
