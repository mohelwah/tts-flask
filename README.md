# Project Type: PYTHON PROJECT
# Project Name : TSS FLASK SERVICE 

Upload model to huggingface website:
   - model path: https://huggingface.co/mohelwah/tts-finetuned/resolve/main/checkpoint_2530000.pth
   - config path: https://huggingface.co/mohelwah/tts-finetuned/resolve/main/config.json

To buld the app: 
>>  docker build -t tts .
![0](https://github.com/mohelwah/tts-flask/assets/30090343/29da7ea0-2b3e-45dc-a734-6dcd74b8840b)
![1](https://github.com/mohelwah/tts-flask/assets/30090343/2a2a53cd-31da-4231-98a8-4124c4e3ecca)

To run the app:
>>  docker run -d -p 8080:8080 tts

![3](https://github.com/mohelwah/tts-flask/assets/30090343/8f5fd250-f031-4241-b56a-01617cd7feee)
 
![2](https://github.com/mohelwah/tts-flask/assets/30090343/fa1ae342-cd1b-48cd-88e8-767dbd04617a)
