from paddleocr import PaddleOCR

_ocr = None

def get_ocr():
    global _ocr
    if _ocr is None:
        _ocr = PaddleOCR(lang="en")
    return _ocr

def run_ocr(image_path: str) -> list[tuple[str, list[int], float]]:
    ocr = get_ocr()
    result = ocr.predict(image_path)
    return [
        (result[0]["rec_texts"][i], result[0]["rec_boxes"][i].tolist(), float(result[0]["rec_scores"][i]))
        for i in range(len(result[0]["rec_texts"]))
    ]