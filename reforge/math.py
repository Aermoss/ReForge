import math

def lerp(a: object, b : object, value: float) -> object:
    if isinstance(a, int) or isinstance(a, float):
        return a + (b - a) * value

    elif isinstance(a, tuple):
        if len(a) != len(b): raise TypeError("tuple sizes doesn't match")
        return (*[lerp(x, y, value) for x, y in zip(a, b)], )

    elif isinstance(a, Vector2):
        return Vector2(lerp(a.x, b.x, value), lerp(a.y, b.y, value))

    elif isinstance(a, Vector3):
        return Vector3(lerp(a.x, b.x, value), lerp(a.y, b.y, value), lerp(a.z, b.z, value))

    elif isinstance(a, Vector4):
        return Vector4(lerp(a.x, b.x, value), lerp(a.y, b.y, value), lerp(a.z, b.z, value), lerp(a.w, b.w, value))
    
    else:
        raise TypeError("expected int, float, tuple, Vector2, Vector3 or Vector4, got " + str(type(a)))
    
def clamp(a: object, min: object, max: object) -> object:
    if isinstance(a, int) or isinstance(a, float):
        return min if a < min else max if a > max else a
    
    elif isinstance(a, tuple):
        if len(a) != len(min) or len(a) != len(max): raise TypeError("tuple sizes doesn't match")
        return (*[clamp(x, y, z) for x, y, z in zip(a, min, max)], )

    elif isinstance(a, Vector2):
        return Vector2(clamp(a.x, min.x, max.x), clamp(a.y, min.y, max.y))

    elif isinstance(a, Vector3):
        return Vector3(clamp(a.x, min.x, max.x), clamp(a.y, min.y, max.y), clamp(a.z, min.z, max.z))

    elif isinstance(a, Vector4):
        return Vector4(clamp(a.x, min.x, max.x), clamp(a.y, min.y, max.y), clamp(a.z, min.z, max.z), clamp(a.w, min.w, max.w))
    
    else:
        raise TypeError("expected int, float, tuple, Vector2, Vector3 or Vector4, got " + str(type(a)))
    
def dot(a: object, b: object) -> float:
    if isinstance(a, int) or isinstance(a, float):
        return a * b
    
    elif isinstance(a, tuple):
        if len(a) != len(b): raise TypeError("tuple sizes doesn't match")
        return sum(x * y for x, y in zip(a, b))

    elif isinstance(a, Vector2):
        return a.x * b.x + a.y * b.y

    elif isinstance(a, Vector3):
        return a.x * b.x + a.y * b.y + a.z * b.z

    elif isinstance(a, Vector4):
        return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w
    
    else:
        raise TypeError("expected int, float, tuple, Vector2, Vector3 or Vector4, got " + str(type(a)))
    
def sqrt(a: object) -> object:
    if isinstance(a, int) or isinstance(a, float):
        return math.sqrt(a)

    elif isinstance(a, tuple):
        return (*[sqrt(x) for x in a], )

    elif isinstance(a, Vector2):
        return Vector2(sqrt(a.x), sqrt(a.y))

    elif isinstance(a, Vector3):
        return Vector3(sqrt(a.x), sqrt(a.y), sqrt(a.z))

    elif isinstance(a, Vector4):
        return Vector4(sqrt(a.x), sqrt(a.y), sqrt(a.z), sqrt(a.w))
    
    else:
        raise TypeError("expected int, float, tuple, Vector2, Vector3 or Vector4, got " + str(type(a)))

def length(a: object) -> float:
    if isinstance(a, int) or isinstance(a, float):
        return abs(a)

    elif isinstance(a, tuple):
        return sqrt(sum(x * x for x in a))

    elif isinstance(a, Vector2):
        return sqrt(a.x * a.x + a.y * a.y)

    elif isinstance(a, Vector3):
        return sqrt(a.x * a.x + a.y * a.y + a.z * a.z)

    elif isinstance(a, Vector4):
        return sqrt(a.x * a.x + a.y * a.y + a.z * a.z + a.w * a.w)
    
    else:
        raise TypeError("expected int, float, tuple, Vector2, Vector3 or Vector4, got " + str(type(a)))

def normalize(a: object) -> object:
    if isinstance(a, int) or isinstance(a, float):
        return a / length(a)

    elif isinstance(a, tuple):
        return (*[x / length(a) for x in a], )

    elif isinstance(a, Vector2):
        return a / length(a)

    elif isinstance(a, Vector3):
        return a / length(a)

    elif isinstance(a, Vector4):
        return a / length(a)
    
    else:
        raise TypeError("expected int, float, tuple, Vector2, Vector3 or Vector4, got " + str(type(a)))
    
def cross(a: object, b: object) -> object:
    if isinstance(a, Vector2):
        return a.x * b.y - a.y * b.x

    elif isinstance(a, Vector3):
        return Vector3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)

    elif isinstance(a, Vector4):
        return Vector4(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x, 0.0)
    
    else:
        raise TypeError("expected Vector2, Vector3 or Vector4, got " + str(type(a)))

def reflect(a: object, b: object) -> object:
    if isinstance(a, Vector2):
        return a - 2.0 * dot(a, b) * b

    elif isinstance(a, Vector3):
        return a - 2.0 * dot(a, b) * b

    elif isinstance(a, Vector4):
        return a - 2.0 * dot(a, b) * b
    
    else:
        raise TypeError("expected Vector2, Vector3 or Vector4, got " + str(type(a)))

def refract(a: object, b: object, eta: float) -> object:
    if isinstance(a, Vector2):
        k = 1.0 - eta * eta * (1.0 - dot(a, b) * dot(a, b))
        return a * eta - (eta * dot(a, b) + sqrt(k)) * b if k >= 0.0 else Vector2(0.0, 0.0)

    elif isinstance(a, Vector3):
        k = 1.0 - eta * eta * (1.0 - dot(a, b) * dot(a, b))
        return a * eta - (eta * dot(a, b) + sqrt(k)) * b if k >= 0.0 else Vector3(0.0, 0.0, 0.0)

    elif isinstance(a, Vector4):
        k = 1.0 - eta * eta * (1.0 - dot(a, b) * dot(a, b))
        return a * eta - (eta * dot(a, b) + sqrt(k)) * b if k >= 0.0 else Vector4(0.0, 0.0, 0.0, 0.0)
    
    else:
        raise TypeError("expected Vector2, Vector3 or Vector4, got " + str(type(a)))

class Vector2:
    def __init__(self, x: float, y: float = None) -> None:
        if y is None: y = x
        self.x, self.y = x, y

    def get(self) -> tuple:
        return (self.x, self.y)
    
    def getInt(self) -> tuple:
        return (int(self.x), int(self.y))

    def copy(self) -> object:
        return Vector2(self.x, self.y)
    
    def __eq__(self, value: object) -> bool:
        if value is None: return False
        if not isinstance(value, Vector2): raise TypeError("expected Vector2, got " + str(type(value)))
        return self.x == value.x and self.y == value.y
    
    def __ne__(self, value: object) -> bool:
        if value is None: return True
        if not isinstance(value, Vector2): raise TypeError("expected Vector2, got " + str(type(value)))
        return self.x != value.x or self.y != value.y

    def __add__(self, value: object) -> object:
        if not isinstance(value, Vector2): raise TypeError("expected Vector2, got " + str(type(value)))
        return Vector2(self.x + value.x, self.y + value.y)

    def __sub__(self, value: object) -> object:
        if not isinstance(value, Vector2): raise TypeError("expected Vector2, got " + str(type(value)))
        return Vector2(self.x - value.x, self.y - value.y)

    def __mul__(self, value: object) -> object:
        if isinstance(value, (int, float)): return Vector2(self.x * value, self.y * value)
        if not isinstance(value, Vector2): raise TypeError("expected Vector2, got " + str(type(value)))
        return Vector2(self.x * value.x, self.y * value.y)

    def __truediv__(self, value: object) -> object:
        if isinstance(value, (int, float)): return Vector2(self.x / value, self.y / value)
        if not isinstance(value, Vector2): raise TypeError("expected Vector2, got " + str(type(value)))
        return Vector2(self.x / value.x, self.y / value.y)
    
    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

class Vector3:
    def __init__(self, x: float, y: float = None, z: float = None) -> None:
        if y is None and z is None: y, z = x, x
        self.x, self.y, self.z = x, y, z

    def get(self) -> tuple:
        return (self.x, self.y, self.z)
    
    def getInt(self) -> tuple:
        return (int(self.x), int(self.y), int(self.z))

    def copy(self) -> object:
        return Vector3(self.x, self.y, self.z)
    
    def __eq__(self, value: object) -> bool:
        if value is None: return False
        if not isinstance(value, Vector3): raise TypeError("expected Vector3, got " + str(type(value)))
        return self.x == value.x and self.y == value.y and self.z == value.z
    
    def __ne__(self, value: object) -> bool:
        if value is None: return True
        if not isinstance(value, Vector3): raise TypeError("expected Vector3, got " + str(type(value)))
        return self.x != value.x or self.y != value.y or self.z != value.z

    def __add__(self, value: object) -> object:
        if not isinstance(value, Vector3): raise TypeError("expected Vector3, got " + str(type(value)))
        return Vector3(self.x + value.x, self.y + value.y, self.z + value.z)

    def __sub__(self, value: object) -> object:
        if not isinstance(value, Vector3): raise TypeError("expected Vector3, got " + str(type(value)))
        return Vector3(self.x - value.x, self.y - value.y, self.z - value.z)

    def __mul__(self, value: object) -> object:
        if isinstance(value, (int, float)): return Vector3(self.x * value, self.y * value, self.z * value)
        if not isinstance(value, Vector3): raise TypeError("expected Vector3, got " + str(type(value)))
        return Vector3(self.x * value.x, self.y * value.y, self.z * value.z)

    def __truediv__(self, value: object) -> object:
        if isinstance(value, (int, float)): return Vector3(self.x / value, self.y / value, self.z / value)
        if not isinstance(value, Vector3): raise TypeError("expected Vector3, got " + str(type(value)))
        return Vector3(self.x / value.x, self.y / value.y, self.z / value.z)
    
    def __repr__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"

class Vector4:
    def __init__(self, x: float, y: float = None, z: float = None, w: float = None) -> None:
        if y is None and z is None and w is None: y, z, w = x, x, x
        self.x, self.y, self.z, self.w = x, y, z, w

    def get(self) -> tuple:
        return (self.x, self.y, self.z, self.w)
    
    def getInt(self) -> tuple:
        return (int(self.x), int(self.y), int(self.z), int(self.w))

    def copy(self) -> object:
        return Vector4(self.x, self.y, self.z, self.w)
    
    def __eq__(self, value: object) -> bool:
        if value is None: return False
        if not isinstance(value, Vector4): raise TypeError("expected Vector4, got " + str(type(value)))
        return self.x == value.x and self.y == value.y and self.z == value.z and self.w == value.w
    
    def __ne__(self, value: object) -> bool:
        if value is None: return True
        if not isinstance(value, Vector4): raise TypeError("expected Vector4, got " + str(type(value)))
        return self.x != value.x or self.y != value.y or self.z != value.z or self.w != value.w

    def __add__(self, value: object) -> object:
        if not isinstance(value, Vector4): raise TypeError("expected Vector4, got " + str(type(value)))
        return Vector4(self.x + value.x, self.y + value.y, self.z + value.z, self.w + value.w)

    def __sub__(self, value: object) -> object:
        if not isinstance(value, Vector4): raise TypeError("expected Vector4, got " + str(type(value)))
        return Vector4(self.x - value.x, self.y - value.y, self.z - value.z, self.w - value.w)

    def __mul__(self, value: object) -> object:
        if isinstance(value, (int, float)): return Vector4(self.x * value, self.y * value, self.z * value, self.w * value)
        if not isinstance(value, Vector4): raise TypeError("expected Vector4, got " + str(type(value)))
        return Vector4(self.x * value.x, self.y * value.y, self.z * value.z, self.w * value.w)

    def __truediv__(self, value: object) -> object:
        if isinstance(value, (int, float)): return Vector4(self.x / value, self.y / value, self.z / value, self.w / value)
        if not isinstance(value, Vector4): raise TypeError("expected Vector4, got " + str(type(value)))
        return Vector4(self.x / value.x, self.y / value.y, self.z / value.z, self.w / value.w)
    
    def __repr__(self) -> str:
        return f"Vector4({self.x}, {self.y}, {self.z}, {self.w})"