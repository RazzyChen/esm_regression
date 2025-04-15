import csv

def fasta_to_csv(fasta_file, output_csv):
    with open(fasta_file, 'r') as f:
        lines = f.readlines()
    
    # 打开输出 CSV 文件
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 写入 CSV 文件头部
        writer.writerow(['sequence', 'tm'])
        
        seq = ""
        for line in lines:
            line = line.strip()
            if line.startswith(">"):  # 标题行
                if seq:  # 如果之前有序列，写入 CSV
                    writer.writerow([seq, tm])
                # 提取 TM 值
                header_parts = line[1:].split('_')
                tm = header_parts[1] if len(header_parts) > 1 else "NA"  # 获取 TM 值
                seq = ""  # 重置序列
            else:
                seq += line  # 累加序列
        
        # 写入最后一个序列
        if seq:
            writer.writerow([seq, tm])

    print(f"转换完成，CSV 文件已保存为: {output_csv}")

# 示例：调用函数，转换 FASTA 文件为 CSV
fasta_file = 'result_rep_seq.fasta'  # 请替换为你的 FASTA 文件路径
output_csv = 'WB_temp_dataset_cluster.csv'  # 输出 CSV 文件路径
fasta_to_csv(fasta_file, output_csv)

