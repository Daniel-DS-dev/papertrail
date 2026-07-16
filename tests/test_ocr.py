from pathlib import Path

from papertrail.ocr.engine import run_ocr

SAMPLE = Path("data/sample/img/X00016469612.jpg")


def test_run_ocr_extracts_known_text():
    output = run_ocr(str(SAMPLE))
    texts = [text for text, _, _ in output]
    assert any("THANK" in t for t in texts)


def test_run_ocr_returns_valid_bbox_shape():
    output = run_ocr(str(SAMPLE))
    _, bbox, score = output[0]
    assert len(bbox) == 4
    assert 0.0 <= score <= 1.0