Problem 1:
I started with a flat structure "src/main.py", and that broke pytest imports, because src was just a folder 
not an installed package, so imports only worked by accident.

Solution:
So I switched to the standard src layout, and created a proper package named: papertrail, under "src/" with the "__init__.py" file, and declared it in the pyproject.toml file, then I ran "uv sync" so the pakcage is installed into the venv.
so tests now run against papertrail.main just like it should be when anyone wants to run this package.



OCR:
I had worked on OCR before in the past, and we worked mainly with two libraries DocTR and PaddleOCR, and we found paddle OCR to be better, i tested both here again and found Paddle to still be better. So we will be using paddle in this project.
Paddle gives more accurate characters, paddle does give you more of a  sentence, characters on the same line and their bounding boxes as one, which won't be helpful in the case where you need word/texts bounding boxes alone, but we can always extract it some other way.