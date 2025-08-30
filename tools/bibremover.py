import re
import sys

def remove_duplicate_keys(input_file, output_file):
    """通过文本处理直接解决重复键问题"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找所有条目
    entries = re.findall(r'(@\w+\{[^@]+)', content, re.DOTALL)
    
    # 跟踪已出现的键
    seen_keys = {}
    unique_entries = []
    duplicates = 0
    
    for entry in entries:
        # 提取键
        key_match = re.search(r'@\w+\{([^,]+)', entry)
        if not key_match:
            unique_entries.append(entry)
            continue
            
        key = key_match.group(1).strip()
        
        # 处理重复键
        if key in seen_keys:
            duplicates += 1
            new_key = f"{key}_dup{seen_keys[key]}"
            entry = entry.replace(f"{{{key},", f"{{{new_key},", 1)
            seen_keys[key] += 1
        else:
            seen_keys[key] = 1
        
        unique_entries.append(entry)
    
    # 保存结果
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(unique_entries))
    
    print(f"处理完成: {input_file} → {output_file}")
    print(f"原始条目数: {len(entries)}")
    print(f"发现重复键: {duplicates}")
    print(f"处理后条目数: {len(unique_entries)}")

# 使用示例
if __name__ == "__main__":
    input_bib = "./tools/input.bib"  # 替换为您的输入文件
    output_bib = "./tools/clean.bib"  # 输出文件名
    remove_duplicate_keys(input_bib, output_bib)