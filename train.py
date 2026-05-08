# 执行训练命令
# python train.py --task a2 --config default.yaml
# 生成权重后，调用权重推理
# python infer.py --task a2 --checkpoint <您的最佳权重文件> --split val --output /data1/yhj/AdoDAS2026/output/runs/a2_100_20260503_114057/submissions/result.csv
# 调整参数命令后，要删除加载好的缓存pt文件，然后保存修改后的代码重新加载数据
# rm -rf /data1/yhj/AdoDAS2026/data_cache/*.pt

# 更改训练得到权重的保存位置：
# 新建你想要的终极目标文件夹
# mkdir -p /data1/yhj/AdoDAS2026/output/runs/
# 把刚刚训练出来的 best.pt 复制过去，并改名为直观的名字
# cp /data1/yhj/train/output/runs/a2__grouped*/checkpoints/best.pt /data1/yhj/AdoDAS2026/output/runs/my_best_a2.pt
# 删除原有的臃肿文件夹释放空间
# rm -rf /data1/yhj/train/output/runs/a2__grouped*

#!/usr/bin/env python3

from common.runner import main


if __name__ == "__main__":
    main()
