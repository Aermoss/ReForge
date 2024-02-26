import reforge.api.tools as tools

tools.initInstanceHandler(__name__)
tools.importAllFilesInDirectory(__file__, __name__)