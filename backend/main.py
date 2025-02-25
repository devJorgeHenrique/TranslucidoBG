from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import shutil
import os
from typing import List
import zipfile
from scripts.remover_fundo import processar_varias_imagens

app = FastAPI()

# Diretórios
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
ZIP_DIR = "zips"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ZIP_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "API para remoção de fundo de imagens está funcionando!"}

@app.post("/upload/")
async def upload_images(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="Nenhum arquivo enviado.")

    file_paths = []
    
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            file_paths.append(file_path)
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": f"Erro ao salvar {file.filename}: {str(e)}"})

    # Processa as imagens e remove o fundo
    try:
        processed_images = processar_varias_imagens(file_paths, OUTPUT_DIR)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Erro ao processar imagens: {str(e)}"})

    if not processed_images:
        raise HTTPException(status_code=500, detail="Nenhuma imagem foi processada.")

    # Cria um arquivo ZIP com as imagens processadas
    zip_path = os.path.join(ZIP_DIR, "imagens_sem_fundo.zip")
    try:
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for image in processed_images:
                zipf.write(image, os.path.basename(image))
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Erro ao criar ZIP: {str(e)}"})

    return {"download_url": f"/download/{os.path.basename(zip_path)}"}

@app.get("/download/{zip_filename}")
def download_zip(zip_filename: str):
    zip_path = os.path.join(ZIP_DIR, zip_filename)
    if not os.path.exists(zip_path):
        raise HTTPException(status_code=404, detail="Arquivo ZIP não encontrado.")

    return FileResponse(zip_path, filename=zip_filename, media_type="application/zip")
