# Project Type: PYTHON PROJECT
# Project Name : TSS FLASK SERVICE 

Upload model to huggingface website:
   - model path: https://huggingface.co/mohelwah/tts-finetuned/resolve/main/checkpoint_2530000.pth
   - config path: https://huggingface.co/mohelwah/tts-finetuned/resolve/main/config.json

To buld the app: 
>>  docker build -t tts .

To run the app:
>>  docker run -d -p 8080:8080 tts