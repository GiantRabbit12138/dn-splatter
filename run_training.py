import subprocess
from pathlib import Path

# 配置参数
config = {
    "dataparser": "normal-nerfstudio",
    "data_path": "datasets/cup_cuboid_for_dn_splatter",
    "log_file": "train.log"
}

# 构建命令参数
cmd = [
    "ns-train", "dn-splatter",
    "--pipeline.model.use-depth-loss", "True",
    "--pipeline.model.depth-loss-type", "EdgeAwareLogL1",
    "--pipeline.model.depth-lambda", "0.2",
    "--pipeline.model.use-normal-loss", "False",
    "--pipeline.model.use-normal-tv-loss", "False",
    "--pipeline.model.normal-supervision", "depth",
    config["dataparser"],
    "--load_normals", "False",
    "--data", str(Path(config["data_path"]).resolve())
]

# 执行命令并记录日志
with open(config["log_file"], "w") as f:
    process = subprocess.run(
        cmd, 
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    f.write(process.stdout)
    # # 实时输出到屏幕和文件
    # for line in process.stdout:
    #     print(line, end='')  # 实时显示在终端
    #     f.write(line)        # 同时写入文件
    #     f.flush()           # 确保立即写入

print(f"训练完成！退出码: {process.returncode}")
