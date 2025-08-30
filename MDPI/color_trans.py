

import os

# 直接通过文本搜索替换多个颜色
def replace_multiple_colors_in_svg(file_path, color_map, output_path):
    # 读取SVG文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        svg_content = file.read()

    # 遍历颜色映射并替换
    for old_color, new_color in color_map.items():
        svg_content = svg_content.replace(old_color, new_color)

    # 将修改后的内容写入新的文件
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(svg_content)

# 扫描文件夹并处理所有SVG文件
def process_svg_files_in_folder(folder_path, color_map):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 构造完整的文件路径
        file_path = os.path.join(folder_path, filename)
        
        # 检查文件是否是SVG文件
        if filename.lower().endswith('.svg'):
            # 构造输出文件路径
            output_path = os.path.join(folder_path, f"modified_{filename}")
            
            # 处理每个SVG文件
            replace_multiple_colors_in_svg(file_path, color_map, output_path)
            print(f"Processed {filename} -> {output_path}")

# 示例使用
color_map = {
    '#edb01c': '#FF0000',  # 将黑色替换为红色
    '#4a63e1': '#00FF00',  # 将白色替换为绿色
    '#0a7783': '#0000ff'   # 将蓝色替换为黄色
}


folder_path = r'E:\donwload\sne_image(1)\origin'  # 请替换为你的文件夹路径
process_svg_files_in_folder(folder_path, color_map)
