from scripts.remover_fundo import processar_varias_imagens

pasta_entrada = "./imagens"
pasta_saida = "./imagens/sem_fundo"

# Executar o processamento das imagens
imagens_processadas = processar_varias_imagens(pasta_entrada, pasta_saida)

# Exibir a lista de imagens processadas
print("\n🔍 Imagens processadas:")
for img in imagens_processadas:
    print(f"✅ {img}")
