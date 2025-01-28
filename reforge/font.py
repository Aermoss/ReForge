import reforge, hashlib

class Font:
    def __init__(self, filePath: str, size: int) -> None:
        self._font = reforge.api.Font(filePath, size)
        self.__lastRender, self.__lastRenderHash = None, None
    
    @property
    def filePath(self) -> int:
        return self._font.filePath

    @property
    def size(self) -> int:
        return self._font.size

    def load(self, filePath: str, size: int) -> None:
        self._font.load(filePath, size)

    def free(self) -> None:
        self._font.free()

    def render(self, text: str, color: reforge.Vector3 | reforge.Vector4) -> reforge.Surface:
        renderHash = hashlib.sha256(str(text).encode()).hexdigest() + hashlib.sha256(str(reforge.getRGBA(color)).encode()).hexdigest()

        if renderHash != self.__lastRenderHash:
            self.__lastRender = reforge.Surface(self._font.render(text, reforge.makeRGBA(color)))
            self.__lastRenderHash = renderHash

        return self.__lastRender

    def terminate(self) -> None:
        self._font.terminate()