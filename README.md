# WKTBulkLoader
A QGIS plugin to bulk load WKT files

## To Build
```
make deploy
```
will `build doc transcompile` and install the plugin to the plugins directory.
You might need to install `sphinx` if you don't have it already. Install it by doing
```
sudo pip install sphinx
```
Do not `brew install sphinx` as it installs some other software

## To Develop
You may need to add following directories to your paths
```
export PATH="/Applications/QGIS.app/Contents/MacOS/bin:$PATH"
export PYTHONPATH="/Applications/QGIS.app/Contents/Resources/python"
```
e.g., `pyrcc4` is in `/Applications/QGIS.app/Contents/MacOS/bin`
and the `/Applications/QGIS.app/Contents/Resources/python` will be needed to `import PyQt4`

If you already have something in `PYTHONPATH`, add it instead with:
```
export PYTHONPATH="/Applications/QGIS.app/Contents/Resources/python:$PYTHONPATH”
```