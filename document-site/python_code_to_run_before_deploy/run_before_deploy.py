import os





file_list = [x for x in os.listdir("python_code_to_run_before_deploy") if x!="run_before_deploy.py"]
for file_name in file_list:
    print(f"run {file_name}")
    os.system(f"python python_code_to_run_before_deploy/{file_name}")