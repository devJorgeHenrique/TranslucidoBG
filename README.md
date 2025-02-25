# 🖼️ TranslucidoBG  

**TranslucidoBG** é uma ferramenta automatizada para remover fundos de imagens de forma simples e eficiente, utilizando a biblioteca `rembg`. O projeto foi desenvolvido para facilitar a edição de imagens e permitir a conversão em massa para o formato **PNG com fundo transparente**.  

---

## 🚀 Recursos  

✅ **Remoção automática** de fundo das imagens  
✅ **Suporte a múltiplos formatos**: JPG, JPEG e PNG  
✅ **Processamento em lote** para múltiplas imagens  
✅ **Geração de arquivos PNG** com fundo transparente  
✅ **Reprocessamento de imagens pendentes** para evitar retrabalho  

---

## 🔧 Uso  

1️⃣ **Remover fundo de todas as imagens na pasta**  

```bash
python remover_fundo.py
```
Isso processa todas as imagens e salva os resultados na pasta sem_fundo/.

2️⃣ Processar imagens que falharam anteriormente

Se algumas imagens falharem, utilize o script de pendentes:
```bash
python processar_pendentes.py
```
Isso evitará retrabalho e processará apenas as imagens que ainda precisam ser convertidas.

---

🛠️ Tecnologias Utilizadas
Python 3+
rembg (para remoção de fundo)
Pillow (PIL) (para manipulação de imagens)

---

📌 Melhorias Futuras

🔹 Interface Gráfica (GUI) para facilitar o uso

🔹 Versão Web/App para upload direto de imagens

🔹 Integração com serviços de armazenamento na nuvem

---

📜 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para contribuir! 🚀

