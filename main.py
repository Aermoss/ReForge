import os, sys

sys.dont_write_bytecode = True
os.environ["REFORGE_API"] = "sdl2"

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
    entity.getComponent(reforge.TransformComponent).position = window.size / 2.0 - entity.getComponent(reforge.TransformComponent).scale / 2.0

    target = entity.getComponent(reforge.TransformComponent).position.copy()
    positions = [reforge.Vector2(0.0, 0.0)] * 10

    while not context.isTerminated():
        context.pollEvents()

        if window.input.keyboard.keys[reforge.Key.LeftShift]:
            target.x += window.input.mouse.scrollChange * 50

        else:
            target.y += window.input.mouse.scrollChange * 50

        target = reforge.clamp(target, reforge.Vector2(0.0, 0.0), window.size - entity.getComponent(reforge.TransformComponent).scale)
        entity.getComponent(reforge.TransformComponent).position = reforge.lerp(entity.getComponent(reforge.TransformComponent).position, target, 0.01)

        renderer.clear(reforge.Vector4(0.0, 0.0, 0.0, 255.0))

        for i in range(len(positions)):
            positions[i] = reforge.lerp(positions[i], (window.input.mouse.position - window.size / 2) / ((i / 2) + 2) - entity.getComponent(reforge.TransformComponent).scale / 2 + window.size / 2, 0.005)
            entity.getComponent(reforge.TransformComponent).position = positions[i]
            renderer.renderScene(scene)

        # renderer.renderScene(scene)
        renderer.present()

    renderer.terminate()
    context.terminate()
    return reforge.exitSuccess