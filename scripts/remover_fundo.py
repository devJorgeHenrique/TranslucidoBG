import os
from rembg import remove
from PIL import Image

# Diretório das imagens de entrada e saída
pasta = "./imagens"
pasta_saida = os.path.join(pasta, "sem_fundo")
os.makedirs(pasta_saida, exist_ok=True)

# Formatos suportados
formatos_suportados = (".jpg", ".jpeg", ".png")

# Lista de arquivos na pasta
arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(formatos_suportados)]

# Remover fundo de cada imagem
for i, arquivo in enumerate(arquivos, start=1):
    caminho_arquivo = os.path.join(pasta, arquivo)
    novo_nome = f"Imagem{i:02d}.png"
    caminho_saida = os.path.join(pasta_saida, novo_nome)

    print(f"🔄 Removendo fundo: {arquivo} ➝ {novo_nome}")

    try:
        with Image.open(caminho_arquivo) as img:
            img = img.convert("RGBA")
            img_sem_fundo = remove(img)
            img_sem_fundo.save(caminho_saida, "PNG")

        print(f"✅ Fundo removido: {arquivo} ➝ {novo_nome}")

    except Exception as e:
        print(f"❌ Erro ao processar {arquivo}: {e}")

print("🚀 Remoção de fundo concluída!")
