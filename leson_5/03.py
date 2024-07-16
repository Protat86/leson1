from pathlib import Path

def analyze_file(filename):
    path = Path(filename)
    text = path.read_text()
    
    num_lines = text.count(" ")
    num_words = len(text.split())
    num_chars = len(text)
    
    print(f"Кількість рядків: {num_lines}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість символів: {num_chars}")

