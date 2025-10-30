from huggingface_hub import login, create_repo, HfApi
# Step 1: Login 
login(token = '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')
print('Successfully login')
# Step 2: Create dataset repo on Huggingface 
try:
    create_repo(repo_id = "cssi87m/ICLSam2CombinedDataset", repo_type = "dataset")
    print("Successfully create dataset")
except Exception as e: 
    print(e)
# Step 3: Upload folder
api = HfApi()
api.upload_large_folder(
    folder_path = "/mnt/disk1/aiotlab/huync/AAAI-MedSam2/Combined_Dataset",
    repo_id = "cssi87m/ICLSam2CombinedDataset", 
    repo_type = "dataset"
)
print("Successfully upload dataset")