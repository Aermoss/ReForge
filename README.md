# ReForge [Forge IV]
A 2D game engine written in Python using both PyGame, PySDL2 and PySDL3.

# Getting Started
## How to install.
```
pip install ReForge
```

# Examples
## Creating a window.
```python
import os

os.environ["REFORGE_API"] = "sdl3"

import reforge, ctypes

def reforgeEntry(argc: int, argv: reforge.List[str]) -> int:
    context = reforge.Context()
    context.makeContextCurrent()
    window = reforge.Window(title = "ReForge", width = 1200, height = 600)
    context.registerWindow(window)
    renderer = reforge.Renderer(window)
    scene = reforge.Scene()

    while not context.isTerminated():
        context.pollEvents()
        renderer.clear(reforge.Vector4(0.0, 0.0, 0.0, 255.0))
        renderer.renderScene(scene)
        renderer.present()

    context.terminate()
    return reforge.exitSuccess
```

## Rendering a rect.
```python
import os

os.environ["REFORGE_API"] = "sdl3"

import reforge, ctypes

def reforgeEntry(argc: int, argv: reforge.List[str]) -> int:
    context = reforge.Context()
    context.makeContextCurrent()
    window = reforge.Window(title = "ReForge", width = 1200, height = 600)
    context.registerWindow(window)
    renderer = reforge.Renderer(window)
    scene = reforge.Scene()

    entity = scene.createEntity()
    entity.addComponent(reforge.RectComponent(fill = False, color = reforge.Vector4(0.0, 128.0, 128.0, 255.0)))
    entity.getComponent(reforge.TransformComponent).scale = reforge.Vector2(200.0, 200.0)
    entity.getComponent(reforge.TransformComponent).position = \
        window.size / 2.0 - entity.getComponent(reforge.TransformComponent).scale / 2.0

    while not context.isTerminated():
        context.pollEvents()
        renderer.clear(reforge.Vector4(0.0, 0.0, 0.0, 255.0))
        renderer.renderScene(scene)
        renderer.present()

    renderer.terminate()
    context.terminate()
    return reforge.exitSuccess
```

## Using the low-level API.
```python
import os

os.environ["REFORGE_API"] = "sdl3"

import reforge, ctypes

def reforgeEntry(argc: int, argv: reforge.List[str]) -> int:
    context = reforge.api.Context()
    window = reforge.api.Window(title = "ReForge", width = 1200, height = 600)
    renderer = reforge.api.Renderer(window)
    inputHandler = reforge.api.Input(window)
    eventHandler = reforge.api.EventHandler()
    event = reforge.api.Event()
    running = True

    while running:
        while eventHandler.pollEvents(event):
            if event.type == reforge.api.EventType.WindowClosed:
                running = False

            inputHandler.eventHandler(event)

        if inputHandler.keyboard.keys[reforge.api.Key.Escape]:
            running = False

        renderer.clear(reforge.Vector4(0.0, 0.0, 0.0, 255.0))
        renderer.present()

    eventHandler.terminate()
    inputHandler.terminate()
    renderer.terminate()
    window.terminate()
    context.terminate()
    return reforge.exitSuccess
```
