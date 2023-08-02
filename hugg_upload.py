from huggingface_hub import HfApi
api = HfApi()
api.upload_file(
    path_or_fileobj="models/checkpoint_2530000.pth",
    path_in_repo="checkpoint_2530000.pth",
    repo_id="mohelwah/tts-finetuned",
    repo_type="model",
)