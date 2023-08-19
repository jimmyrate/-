import json
import random

# 读取txt文件，将内容转换为JSON格式
def txt_to_json(file_path):
    json_data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            src, trg = line.strip().split(' ', 1)
            json_data.append({"src": trg, "trg": src})  # 交换src和trg的值
    return json_data

# 划分数据集为train, test和valid集合
def split_data(data, train_ratio=0.8, test_ratio=0.1, valid_ratio=0.1):
    total_samples = len(data)
    train_size = int(total_samples * train_ratio)
    test_size = int(total_samples * test_ratio)

    random.shuffle(data)

    train_data = data[:train_size]
    test_data = data[train_size:train_size + test_size]
    valid_data = data[train_size + test_size:]

    return train_data, test_data, valid_data

# 写入jsonl文件
def write_jsonl_file(json_data, file_path):
    with open(file_path, 'w') as file:
        for item in json_data:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')

# 主函数
def main():
    input_file = '/home/leo/fightinglee/Diffusion-mol/datasets/molecular/drd2/train_pairs.txt'
    train_file = '/home/leo/fightinglee/Diffusion-mol/datasets/molecular/drd2/train.jsonl'
    test_file = '/home/leo/fightinglee/Diffusion-mol/datasets/molecular/drd2/test.jsonl'
    valid_file = '/home/leo/fightinglee/Diffusion-mol/datasets/molecular/drd2/valid.jsonl'

    data = txt_to_json(input_file)
    train_data, test_data, valid_data = split_data(data)

    write_jsonl_file(train_data, train_file)
    write_jsonl_file(test_data, test_file)
    write_jsonl_file(valid_data, valid_file)

if __name__ == "__main__":
    main()
