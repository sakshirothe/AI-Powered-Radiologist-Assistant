import os

print("Top level inside dataset_full/Training:")
training_path = "dataset_full/Training"
print(os.listdir(training_path))

print("\nChecking inside each item of Training:\n")
for item in os.listdir(training_path):
    full_path = os.path.join(training_path, item)
    if os.path.isdir(full_path):
        files = os.listdir(full_path)
        print(f"Folder: {item}")
        print(f"Number of items: {len(files)}")
        print(f"First 5 items: {files[:5]}")
        print("-" * 40)
    else:
        print(f"File: {item}")