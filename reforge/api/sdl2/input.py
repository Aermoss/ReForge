import reforge.api.tools, sdl2

class Key:
    Up, Down = sdl2.SDL_SCANCODE_UP, sdl2.SDL_SCANCODE_DOWN
    Left, Right = sdl2.SDL_SCANCODE_LEFT, sdl2.SDL_SCANCODE_RIGHT
    A, B, C = sdl2.SDL_SCANCODE_A, sdl2.SDL_SCANCODE_B, sdl2.SDL_SCANCODE_C
    D, E, F = sdl2.SDL_SCANCODE_D, sdl2.SDL_SCANCODE_E, sdl2.SDL_SCANCODE_F
    G, H, I = sdl2.SDL_SCANCODE_G, sdl2.SDL_SCANCODE_H, sdl2.SDL_SCANCODE_I
    J, K, L = sdl2.SDL_SCANCODE_J, sdl2.SDL_SCANCODE_K, sdl2.SDL_SCANCODE_L
    M, N, O = sdl2.SDL_SCANCODE_M, sdl2.SDL_SCANCODE_N, sdl2.SDL_SCANCODE_O
    P, Q, R = sdl2.SDL_SCANCODE_P, sdl2.SDL_SCANCODE_Q, sdl2.SDL_SCANCODE_R
    S, T, U = sdl2.SDL_SCANCODE_S, sdl2.SDL_SCANCODE_T, sdl2.SDL_SCANCODE_U
    V, W, X = sdl2.SDL_SCANCODE_V, sdl2.SDL_SCANCODE_W, sdl2.SDL_SCANCODE_X
    Y, Z = sdl2.SDL_SCANCODE_Y, sdl2.SDL_SCANCODE_Z
    Zero, One = sdl2.SDL_SCANCODE_0, sdl2.SDL_SCANCODE_1
    Two, Three = sdl2.SDL_SCANCODE_2, sdl2.SDL_SCANCODE_3
    Four, Five = sdl2.SDL_SCANCODE_4, sdl2.SDL_SCANCODE_5
    Six, Seven = sdl2.SDL_SCANCODE_6, sdl2.SDL_SCANCODE_7
    Eight, Nine = sdl2.SDL_SCANCODE_8, sdl2.SDL_SCANCODE_9
    F1, F2 = sdl2.SDL_SCANCODE_F1, sdl2.SDL_SCANCODE_F2
    F3, F4 = sdl2.SDL_SCANCODE_F3, sdl2.SDL_SCANCODE_F4
    F5, F6 = sdl2.SDL_SCANCODE_F5, sdl2.SDL_SCANCODE_F6
    F7, F8 = sdl2.SDL_SCANCODE_F7, sdl2.SDL_SCANCODE_F8
    F9, F10 = sdl2.SDL_SCANCODE_F9, sdl2.SDL_SCANCODE_F10
    F11, F12 = sdl2.SDL_SCANCODE_F11, sdl2.SDL_SCANCODE_F12
    LeftCtrl, RightCtrl = sdl2.SDL_SCANCODE_LCTRL, sdl2.SDL_SCANCODE_RCTRL
    LeftShift, RightShift = sdl2.SDL_SCANCODE_LSHIFT, sdl2.SDL_SCANCODE_RSHIFT
    LeftAlt, RightAlt = sdl2.SDL_SCANCODE_LALT, sdl2.SDL_SCANCODE_RALT
    Tab, CapsLock = sdl2.SDL_SCANCODE_TAB, sdl2.SDL_SCANCODE_CAPSLOCK
    Home, End = sdl2.SDL_SCANCODE_HOME, sdl2.SDL_SCANCODE_END
    Insert, Delete = sdl2.SDL_SCANCODE_INSERT, sdl2.SDL_SCANCODE_DELETE
    Plus, Minus = sdl2.SDL_SCANCODE_KP_PLUS, sdl2.SDL_SCANCODE_KP_MINUS
    Slash, Backslash = sdl2.SDL_SCANCODE_SLASH, sdl2.SDL_SCANCODE_BACKSLASH
    Asterisk, Escape = sdl2.SDL_SCANCODE_KP_MULTIPLY, sdl2.SDL_SCANCODE_ESCAPE
    Return, Backspace, Space = sdl2.SDL_SCANCODE_RETURN, sdl2.SDL_SCANCODE_BACKSPACE, sdl2.SDL_SCANCODE_SPACE

class Button:
    Left, Right, Middle = sdl2.SDL_BUTTON_LEFT, sdl2.SDL_BUTTON_RIGHT, sdl2.SDL_BUTTON_MIDDLE

class Keyboard:
    def __init__(self) -> None:
        self.keys = sdl2.SDL_GetKeyboardState(None)

    def update(self) -> None:
        ...

    def terminate(self) -> None:
        ...

class Mouse:
    def __init__(self) -> None:
        self.buttons = {}
        self.position, self.scroll = reforge.Vector2(0, 0), 0
        self.positionChange, self.scrollChange = reforge.Vector2(0, 0), 0
        self._lastPosition, self._lastScroll = reforge.Vector2(0, 0), 0
        self.positionState, self.scrollState = False, False

    def update(self) -> None:
        self.positionChange = self.position - self._lastPosition
        self.scrollChange = self._lastScroll - self.scroll

        self._lastPosition = self.position
        self._lastScroll = self.scroll

        self.positionState = self.positionChange != reforge.Vector2(0, 0)
        self.scrollState = self.scrollChange != 0

    def terminate(self) -> None:
        ...

class Input:
    def __init__(self, window) -> None:
        reforge.api.tools.addInstance(__name__, self)
        self._window = window
        self.keyboard, self.mouse = reforge.api.Keyboard(), reforge.api.Mouse()

    def update(self) -> None:
        self.keyboard.update()
        self.mouse.update()

    def eventHandler(self, event: object) -> None:
        match event.type:
            case reforge.api.EventType.MouseMotion:
                if event.windowID is None or (event.windowID is not None and event.windowID == self._window._windowID):
                    self.mouse.position.x, self.mouse.position.y = event.x, event.y

            case reforge.api.EventType.MouseButtonUp:
                if event.windowID is None or (event.windowID is not None and event.windowID == self._window._windowID):
                    self.mouse.buttons[event.button] = False

            case reforge.api.EventType.MouseButtonDown:
                if event.windowID is None or (event.windowID is not None and event.windowID == self._window._windowID):
                    self.mouse.buttons[event.button] = True

            case reforge.api.EventType.MouseWheel:
                self.mouse.scroll += event.y

    def terminate(self):
        self.keyboard.terminate()
        self.mouse.terminate()