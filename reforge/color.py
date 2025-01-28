import reforge

def isRGB(color: reforge.Vector3 | reforge.Vector4) -> bool:
    return isinstance(color, reforge.Vector3)

def isRGBA(color: reforge.Vector3 | reforge.Vector4) -> bool:
    return isinstance(color, reforge.Vector4)

def makeRGB(color: reforge.Vector3 | reforge.Vector4) -> tuple[int, int, int]:
    if isRGBA(color): color = reforge.Vector3(*color.get()[:3])
    return reforge.clamp(color, reforge.Vector3(0.0), reforge.Vector3(255.0))

def makeRGBA(color: reforge.Vector3 | reforge.Vector4) -> tuple[int, int, int, int]:
    if isRGB(color): color = reforge.Vector4(*color.get(), 255.0)
    return reforge.clamp(color, reforge.Vector4(0.0), reforge.Vector4(255.0))

def getRGB(color: reforge.Vector3 | reforge.Vector4) -> tuple[int, int, int]:
    return tuple(makeRGB(color).get()[:3])

def getRGBA(color: reforge.Vector3 | reforge.Vector4) -> tuple[int, int, int, int]:
    return tuple(makeRGBA(color).get()[:4])