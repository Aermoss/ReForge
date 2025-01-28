import reforge.api.instanceHandler, pygame

class Key:
    Up, Down = pygame.K_UP, pygame.K_DOWN
    Left, Right = pygame.K_LEFT, pygame.K_RIGHT
    A, B, C = pygame.K_a, pygame.K_b, pygame.K_c
    D, E, F = pygame.K_d, pygame.K_e, pygame.K_f
    G, H, I = pygame.K_g, pygame.K_h, pygame.K_i
    J, K, L = pygame.K_j, pygame.K_k, pygame.K_l
    M, N, O = pygame.K_m, pygame.K_n, pygame.K_o
    P, Q, R = pygame.K_p, pygame.K_q, pygame.K_r
    S, T, U = pygame.K_s, pygame.K_t, pygame.K_u
    V, W, X = pygame.K_v, pygame.K_w, pygame.K_x
    Y, Z = pygame.K_y, pygame.K_z
    Zero, One = pygame.K_0, pygame.K_1
    Two, Three = pygame.K_2, pygame.K_3
    Four, Five = pygame.K_4, pygame.K_5
    Six, Seven = pygame.K_6, pygame.K_7
    Eight, Nine = pygame.K_8, pygame.K_9
    F1, F2 = pygame.K_F1, pygame.K_F2
    F3, F4 = pygame.K_F3, pygame.K_F4
    F5, F6 = pygame.K_F5, pygame.K_F6
    F7, F8 = pygame.K_F7, pygame.K_F8
    F9, F10 = pygame.K_F9, pygame.K_F10
    F11, F12 = pygame.K_F11, pygame.K_F12
    LeftCtrl, RightCtrl = pygame.K_LCTRL, pygame.K_RCTRL
    LeftShift, RightShift = pygame.K_LSHIFT, pygame.K_RSHIFT
    LeftAlt, RightAlt = pygame.K_LALT, pygame.K_RALT
    Tab, CapsLock = pygame.K_TAB, pygame.K_CAPSLOCK
    Home, End = pygame.K_HOME, pygame.K_END
    Insert, Delete = pygame.K_INSERT, pygame.K_DELETE
    Plus, Minus = pygame.K_KP_PLUS, pygame.K_KP_MINUS
    Slash, Backslash = pygame.K_SLASH, pygame.K_BACKSLASH
    Asterisk, Escape = pygame.K_KP_MULTIPLY, pygame.K_ESCAPE
    Return, Backspace, Space = pygame.K_RETURN, pygame.K_BACKSPACE, pygame.K_SPACE

class Button:
    Left, Right, Middle = pygame.BUTTON_LEFT, pygame.BUTTON_RIGHT, pygame.BUTTON_MIDDLE

class Keyboard:
    def __init__(self) -> None:
        self.update()

    def update(self) -> None:
        self.keys = pygame.key.get_pressed()

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