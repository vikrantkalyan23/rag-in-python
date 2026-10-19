from pathlib import Path

document_path = Path("documents/company.txt")
document = document_path.read_text(encoding="utf-8")

chunks = [
    paragraph.strip()
    for paragraph in document.split("\n\n")
    if paragraph.strip()
]

for index, chunk in enumerate(chunks, start=1):
    print(f"Chunk {index}: {chunk}")