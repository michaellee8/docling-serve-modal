# Sample code for running docling-serve on modal

## Setup steps

1. Run `uv sync`
2. Setup a secret called `DOCLING_SERVER_API_KEY` with an environment variable called `DOCLING_SERVE_API_KEY` using a randomly generated key. Docs: https://modal.com/docs/guide/secrets
3. Setup proxy auth. Docs: https://modal.com/docs/guide/webhook-proxy-auth
4. Deploy it run `uv run modal deploy main.py`

## Sample curl

```bash
curl -X "POST" \
  "https://<your-api-endpoint>.modal.run/v1/convert/file" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -H "X-Api-Key: $DOCLING_SERVE_API_KEY" \
  -H "Modal-Key: $MODAL_KEY" \
  -H "Modal-Secret: $MODAL_SECRET" \
  -F "image_export_mode=placeholder" \
  -F "files=@input.pdf;type=application/pdf" \
  -F "to_formats=md" \
  -F "to_formats=html" \
  -F "to_formats=json" \
  -F "do_ocr=true" \
  -F "vlm_pipeline_model=granite_docling" \
  -vv \
  -L \
  --http1.1 \
  -o output.json
```

## Notes

- L40S are selected for speed but it seems that even T4 would have worked.
- Async api endpoints from docling-serve are not used since modal has builtin handling for request timeout, and serverless container may terminate before the job is finished, see https://modal.com/docs/guide/webhook-timeouts
