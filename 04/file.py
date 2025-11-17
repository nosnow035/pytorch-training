from pathlib import Path


if __name__ == "__main__":
 data_dir = Path("DL-BasicClass\Lecture4\exercise\data")
 data_dir_path = Path(data_dir).resolve()
 print("--absolute path ---")
 print(data_dir_path)
 
 
print("-- all files under data_dir ---")
file_list = list(data_dir.glob("*"))
print(len(file_list))
for dir in enumerate(file_list):
 print(dir[1])

file_list = list(Path(data_dir).glob("**/*.png"))
print(len(file_list))







