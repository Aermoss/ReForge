import reforge, time

class ThreadingPolicy:
    SingleThreaded, MultiThreaded = range(2)

class RenderAPI:
    SDL2, SDL3, PyGame = range(3)

class ApplicationSpecification:
    def __init__(self, name: str = "ReForge", width: int = 1200, height: int = 600, \
        renderAPI = RenderAPI.SDL3, threadingPolicy = ThreadingPolicy.SingleThreaded) -> None:
        self.name, self.width, self.height, self.renderAPI, self.threadingPolicy = \
            name, width, height, renderAPI, threadingPolicy

class Application:
    def __init__(self, specification) -> None:
        if reforge.applicationInstance is not None:
            reforge.api.apiLog(reforge.api.apiLogType.FatalError, "only one instance of application can be created!", terminate = True)

        if specification.threadingPolicy != reforge.ThreadingPolicy.SingleThreaded:
            reforge.api.apiLog(reforge.api.apiLogType.FatalError, "only single-threaded applications are supported!", terminate = True)

        if not reforge.api.setCurrentAPI(["sdl2", "sdl3", "pygame"][specification.renderAPI]):
            reforge.api.apiLog(reforge.api.apiLogType.FatalError, "failed to set the current API!", terminate = True)

        if len(reforge.api.initAPI()) == 0:
            reforge.api.apiLog(reforge.api.apiLogType.FatalError, "failed to initialize the current API!", terminate = True)

        reforge.applicationInstance = self
        self.specification = specification
        self.context = reforge.Context()
        self.context.makeContextCurrent()
        self.window = reforge.Window(title = specification.name, width = specification.width, height = specification.height)
        self.context.registerWindow(self.window)
        self.context._preventTerminate = True
        self.renderer = reforge.Renderer(self.window)
        self.scene = reforge.Scene()

    def onCreate(self) -> None:
        ...

    def onUpdate(self, deltaTime) -> None:
        ...

    def onDestroy(self) -> None:
        ...

    def run(self):
        lastTime, self.deltaTime = time.time(), 0.0
        self.onCreate()

        while not self.context.isTerminated():
            self.context.pollEvents()
            self.deltaTime, lastTime = time.time() - lastTime, time.time()
            self.renderer.clear(self.window.backgroundColor)
            self.onUpdate(self.deltaTime)
            self.scene.update(self.deltaTime)
            self.renderer.renderScene(self.scene)
            self.renderer.present()

        self.onDestroy()
        self.renderer.terminate()
        reforge.api.terminateAPI()
        self.context._context.terminate()
        self.context._context = None
        return reforge.exitSuccess