import re

def extract_hidden_messages(filename):
    results = []
    pattern = re.compile(rb'[a-z]{5,}!')

    with open(filename, 'rb') as file:
        chunk_size = 1024
        buffer = b''

        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            buffer += chunk

            matches = pattern.findall(buffer)

            for match in matches:
                results.append(match.decode('utf-8'))

            buffer = buffer[-10:]

    return results

def main():
    messages = extract_hidden_messages(r"C:\Users\molev\Downloads\Notebooks-main\Notebooks-main\content\week05\resources\logo.jpg")
    for msg in messages:
        print(msg)

main()