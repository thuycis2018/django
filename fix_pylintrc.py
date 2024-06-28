import chardet


def convert_to_utf8(file_path):
    # Detect encoding
    with open(file_path, 'rb') as f:
        rawdata = f.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']
        print(f"Detected encoding: {encoding}")

    # Read content with detected encoding
    with open(file_path, 'r', encoding=encoding) as f:
        content = f.read()

    # Write content to file with UTF-8 encoding
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Converted {file_path} to UTF-8 encoding")


def remove_bom(file_path):
    # Read content with utf-8-sig to remove BOM if present
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Write content back with utf-8 encoding
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Removed BOM from {file_path} if present")


file_path = '.pylintrc'
convert_to_utf8(file_path)
remove_bom(file_path)
