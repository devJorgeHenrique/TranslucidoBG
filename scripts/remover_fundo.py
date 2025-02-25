import os
from rembg import remove
from PIL import Image
from typing import List

# Definir os formatos suportados
FORMATOS_SUPORTADOS = (".jpg", ".jpeg", ".png")

def listar_imagens(diretorio: str) -> List[str]:
    """Lista todas as imagens válidas dentro do diretório informado."""
    return [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.lower().endswith(FORMATOS_SUPORTADOS)]

def processar_varias_imagens(pasta_entrada: str, pasta_saida: str) -> List[str]:
    """
    Processa todas as imagens dentro do diretório informado, removendo o fundo.
    Retorna a lista de caminhos das imagens processadas.
    """
    os.makedirs(pasta_saida, exist_ok=True)
    imagens = listar_imagens(pasta_entrada)

    if not imagens:
        print("⚠️ Nenhuma imagem válida encontrada para processamento.")
        return []

    imagens_processadas = []
    
    for i, caminho_arquivo in enumerate(imagens, start=1):
        nome_original = os.path.basename(caminho_arquivo)
        novo_nome = f"Imagem{i:02d}.png"
        caminho_saida = os.path.join(pasta_saida, novo_nome)

        print(f"🔄 Removendo fundo: {nome_original} ➝ {novo_nome}")
        
        try:
            with Image.open(caminho_arquivo) as img:
                img = img.convert("RGBA")
                img_sem_fundo = remove(img)
                img_sem_fundo.save(caminho_saida, "PNG")
                imagens_processadas.append(caminho_saida)

            print(f"✅ Fundo removido: {nome_original} ➝ {novo_nome}")
        
        except Exception as e:
            print(f"❌ Erro ao processar {nome_original}: {e}")

    print("🚀 Remoção de fundo concluída!")
    return imagens_processadas
