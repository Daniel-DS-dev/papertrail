Problem 1:
I started with a flat structure "src/main.py", and that broke pytest imports, because src was just a folder 
not an installed package, so imports only worked by accident.

So I switched to the standard src layout, and created a proper package named: papertrail, under "src/" with the "__init__.py" file, and declared it in the pyproject.toml file, then I ran "uv sync" so the pakcage is installed into the venv.
so tests now run against papertrail.main just like it should be when anyone wants to run this package.