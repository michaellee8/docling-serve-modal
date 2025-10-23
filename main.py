import modal
from docling_serve.app import create_app

app = modal.App("docling-serve-modal")

image = modal.Image.from_registry(
    "quay.io/docling-project/docling-serve-cu128:v1.7.0"
).run_commands("docling-tools models download --all")


@app.function(
    image=image,
    secrets=[modal.Secret.from_name("DOCLING_SERVE_API_KEY")],
    timeout=7200,
    gpu=["L40S", "A100-40GB", "A10", "L4", "T4"],
    scaledown_window=60,
)
@modal.concurrent(max_inputs=32)
@modal.asgi_app(requires_proxy_auth=True)
def docling_serve_fastapi_app_with_lifespan():
    web_app = create_app()
    return web_app
