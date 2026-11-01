import urllib.request
import os

urls = [
    "https://cdn.tecconcursos.com.br/figuras/81bbd8f3-cc10-4f76-ad56-e652ad185846",
    "https://cdn.tecconcursos.com.br/figuras/c16c53dc-25c8-47a9-a41b-cbdb3dfebc25"
]

out_dir = r"C:\Programação\hermes\PDF Revisão\temp_imgs"
os.makedirs(out_dir, exist_ok=True)

for i, url in enumerate(urls):
    out_path = os.path.join(out_dir, f"img{i+1}.png")
    try:
        urllib.request.urlretrieve(url, out_path)
        print(f"Baixado: {out_path} ({os.path.getsize(out_path)} bytes)")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")