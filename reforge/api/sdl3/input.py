import reforge.api.instanceHandler, sdl3

class Key:
    Up, Down = sdl3.SDL_SCANCODE_UP, sdl3.SDL_SCANCODE_DOWN
    Left, Right = sdl3.SDL_SCANCODE_LEFT, sdl3.SDL_SCANCODE_RIGHT
    A, B, C = sdl3.SDL_SCANCODE_A, sdl3.SDL_SCANCODE_B, sdl3.SDL_SCANCODE_C
    D, E, F = sdl3.SDL_SCANCODE_D, sdl3.SDL_SCANCODE_E, sdl3.SDL_SCANCODE_F
    G, H, I = sdl3.SDL_SCANCODE_G, sdl3.SDL_SCANCODE_H, sdl3.SDL_SCANCODE_I
    J, K, L = sdl3.SDL_SCANCODE_J, sdl3.SDL_SCANCODE_K, sdl3.SDL_SCANCODE_L
    M, N, O = sdl3.SDL_SCANCODE_M, sdl3.SDL_SCANCODE_N, sdl3.SDL_SCANCODE_O
    P, Q, R = sdl3.SDL_SCANCODE_P, sdl3.SDL_SCANCODE_Q, sdl3.SDL_SCANCODE_R
    S, T, U = sdl3.SDL_SCANCODE_S, sdl3.SDL_SCANCODE_T, sdl3.SDL_SCANCODE_U
    V, W, X = sdl3.SDL_SCANCODE_V, sdl3.SDL_SCANCODE_W, sdl3.SDL_SCANCODE_X
    Y, Z = sdl3.SDL_SCANCODE_Y, sdl3.SDL_SCANCODE_Z
    Zero, One = sdl3.SDL_SCANCODE_0, sdl3.SDL_SCANCODE_1
    Two, Three = sdl3.SDL_SCANCODE_2, sdl3.SDL_SCANCODE_3
    Four, Five = sdl3.SDL_SCANCODE_4, sdl3.SDL_SCANCODE_5
    Six, Seven = sdl3.SDL_SCANCODE_6, sdl3.SDL_SCANCODE_7
    Eight, Nine = sdl3.SDL_SCANCODE_8, sdl3.SDL_SCANCODE_9
    F1, F2 = sdl3.SDL_SCANCODE_F1, sdl3.SDL_SCANCODE_F2
    F3, F4 = sdl3.SDL_SCANCODE_F3, sdl3.SDL_SCANCODE_F4
    F5, F6 = sdl3.SDL_SCANCODE_F5, sdl3.SDL_SCANCODE_F6
    F7, F8 = sdl3.SDL_SCANCODE_F7, sdl3.SDL_SCANCODE_F8
    F9, F10 = sdl3.SDL_SCANCODE_F9, sdl3.SDL_SCANCODE_F10
    F11, F12 = sdl3.SDL_SCANCODE_F11, sdl3.SDL_SCANCODE_F12
    LeftCtrl, RightCtrl = sdl3.SDL_SCANCODE_LCTRL, sdl3.SDL_SCANCODE_RCTRL
    LeftShift, RightShift = sdl3.SDL_SCANCODE_LSHIFT, sdl3.SDL_SCANCODE_RSHIFT
    LeftAlt, RightAlt = sdl3.SDL_SCANCODE_LALT, sdl3.SDL_SCANCODE_RALT
    Tab, CapsLock = sdl3.SDL_SCANCODE_TAB, sdl3.SDL_SCANCODE_CAPSLOCK
    Home, End = sdl3.SDL_SCANCODE_HOME, sdl3.SDL_SCANCODE_END
    Insert, Delete = sdl3.SDL_SCANCODE_INSERT, sdl3.SDL_SCANCODE_DELETE
    Plus, Minus = sdl3.SDL_SCANCODE_KP_PLUS, sdl3.SDL_SCANCODE_KP_MINUS
    Slash, Backslash = sdl3.SDL_SCANCODE_SLASH, sdl3.SDL_SCANCODE_BACKSLASH
    Asterisk, Escape = sdl3.SDL_SCANCODE_KP_MULTIPLY, sdl3.SDL_SCANCODE_ESCAPE
    Return, Backspace, Space = sdl3.SDL_SCANCODE_RETURN, sdl3.SDL_SCANCODE_BACKSPACE, sdl3.SDL_SCANCODE_SPACE

class Button:
    Left, Right, Middle = sdl3.SDL_BUTTON_LEFT, sdl3.SDL_BUTTON_RIGHT, sdl3.SDL_BUTTON_MIDDLE

class Keyboard:
    def __init__(self) -> None:
        self.keys = sdl3.SDL_GetKeyboardState(None)

    def update(self) -> None:
        ...

    def terminate(self) -> None:
        ...

class Mouse:
    def __init__(self) -> None:
        self.buttons = {Button.Left: False, Button.Right: False, Button.Middle: False}
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
        reforge.api.instanceHandler.addInstance(__name__, self)
        self._window = window
        self.keyboard, self.mouse = reforge.api.Keyboard(), reforge.api.Mouse()

    def update(self) -> None:
        self.keyboard.update()
        self.mouse.update()

    def eventHandler(self, event: object) -> None:
        match event.type:
            case reforge.api.EventType.MouseMotion:
                if event.windowId is None or (event.windowId is not None and event.windowId == self._window._windowID):
                    self.mouse.position = event.motion.copy()

            case reforge.api.EventType.MouseButtonUp:
                if event.windowId is None or (event.windowId is not None and event.windowId == self._window._windowID):
                    self.mouse.buttons[event.button] = False

            case reforge.api.EventType.MouseButtonDown:
                if event.windowId is None or (event.windowId is not None and event.windowId == self._window._windowID):
                    self.mouse.buttons[event.button] = True

            case reforge.api.EventType.MouseWheel:
                if event.windowId is None or (event.windowId is not None and event.windowId == self._window._windowID):
                    self.mouse.scroll += event.wheel.y

            case _:
                ...

    def terminate(self):
        self.keyboard.terminate()
        self.mouse.terminate()