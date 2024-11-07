from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import io
from .preprocessing import TextPreprocessor
from .augmentation import TextAugmenter

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process")
async def process_text(
    request: Request,
    file: UploadFile = File(...),
    preprocessing_method: str = Form(None),
    augmentation_method: str = Form(None)
):
    # Read the file content
    content = await file.read()
    text = content.decode()
    
    # Initialize processors
    preprocessor = TextPreprocessor()
    augmenter = TextAugmenter()
    
    # Process according to selected method
    preprocessed_text = text
    if preprocessing_method:
        if preprocessing_method == "tokenize":
            preprocessed_text = " ".join(preprocessor.tokenize(text))
        elif preprocessing_method == "remove_punctuation":
            preprocessed_text = preprocessor.remove_punctuation(text)
        elif preprocessing_method == "pad":
            preprocessed_text = preprocessor.pad_text(text)
    
    augmented_text = preprocessed_text
    if augmentation_method:
        if augmentation_method == "synonym":
            augmented_text = augmenter.synonym_replacement(preprocessed_text)
        elif augmentation_method == "random_insertion":
            augmented_text = augmenter.random_insertion(preprocessed_text)
    
    return {
        "original_text": text,
        "preprocessed_text": preprocessed_text,
        "augmented_text": augmented_text
    }