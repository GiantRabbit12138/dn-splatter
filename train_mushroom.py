import subprocess
from pathlib import Path

# 配置参数
config = {
    "dataparser": "mushroom",
    "data_path": "./datasets/room_datasets/activity",
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
    "--data", str(Path(config["data_path"]).resolve()),
    "--mode", "kinect"
]

process = subprocess.run(cmd)

print(f"训练完成！退出码: {process.returncode}")
