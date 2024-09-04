import io
import os
import tiktoken
from bs4 import BeautifulSoup
from typing import Sequence


def extract_text(filename: str) -> str:
    f = io.open(filename, mode="r", encoding="utf-8")
    html_doc = f.read()
    f.close()
    soup = BeautifulSoup(html_doc, 'html.parser')
    text = soup.get_text()
    return text

def chunking(text: str, max_token_count: int) -> Sequence[str]:
    if max_token_count < 1:
        raise ValueError("max_token_count must be a postive integer.")

    enc = tiktoken.get_encoding("cl100k_base")

    words = text.split()
    chunk = []
    encodeStr = ""
    token_count = 0
    
    for word in words:
        encodeStr = encodeStr + " " + word
        token_count += len(enc.encode(word))
        if token_count+len(enc.encode(word)) > max_token_count:
            chunk.append(encodeStr.strip())
            encodeStr = ""
            token_count = 0
    
    if encodeStr:        
        chunk.append(encodeStr.strip())
        
    return chunk

def extract_and_chunk_text(directory: str, max_tokens: int) -> dict[str, Sequence[str]]:
    results = {}
    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.html'):
                file_path = os.path.join(dirpath, filename)
                text = extract_text(file_path)
                chunks = chunking(text, max_tokens)
                results[file_path] = chunks
                
                
    return results