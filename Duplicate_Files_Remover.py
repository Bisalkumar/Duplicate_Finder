import os
import hashlib
from concurrent.futures import ProcessPoolExecutor

def hash_file(filename, algorithm='sha256'):
    BLOCKSIZE = 65536
    hasher = hashlib.new(algorithm)
    
    with open(filename, 'rb') as file:
        buf = file.read(BLOCKSIZE)
        while buf:
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()

def scan_directory(path="."):
    # Using os.walk to go through all directories and subdirectories
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            full_path = os.path.join(dirpath, f)
            yield full_path

def main():
    hashMap = {}
    sizeMap = {}
    duplicates = set()

    # Collecting all files from directory and subdirectories
    files = list(scan_directory())

    # Filtering by file size
    for f in files:
        fsize = os.path.getsize(f)
        if fsize not in sizeMap:
            sizeMap[fsize] = [f]
        else:
            sizeMap[fsize].append(f)

    # Using processes to parallelize the hashing, especially beneficial for CPU-bound operations
    with ProcessPoolExecutor() as executor:
        for size, files_with_same_size in sizeMap.items():
            if len(files_with_same_size) > 1:
                # Map each file to the hash_file function
                results = list(executor.map(hash_file, files_with_same_size))
                
                for i, file_hash in enumerate(results):
                    if file_hash in hashMap:
                        duplicates.add(files_with_same_size[i])
                    else:
                        hashMap[file_hash] = files_with_same_size[i]

    if duplicates:
        print('Duplicates Found:')
        for duplicate in duplicates:
            print(duplicate)
            # This just prints the duplicates. You can choose to delete or move them as required.
    else:
        print('No duplicate files found')

if __name__ == "__main__":
    main()
