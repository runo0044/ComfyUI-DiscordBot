# /extensions
# /embeddings
# /object_info
# /prompt
# /queue
# /history
# /system_stats
import json
import random

import requests

i = 0


def txt2img(positive_prompt, negative_prompt, steps, cfg):
    global i
    p = {"prompt": {
        "3": {
            "inputs": {
                "seed": random.randint(1, 18446744073709551614),
                "steps": steps,
                "cfg": cfg,
                "sampler_name": "euler",
                "scheduler": "karras",
                "denoise": 1,
                "model": [
                    "4",
                    0
                ],
                "positive": [
                    "6",
                    0
                ],
                "negative": [
                    "7",
                    0
                ],
                "latent_image": [
                    "5",
                    0
                ]
            },
            "class_type": "KSampler"
        },
        "4": {
            "inputs": {
                "ckpt_name": "Replicant-V3.0_fp16.safetensors"
            },
            "class_type": "CheckpointLoaderSimple"
        },
        "5": {
            "inputs": {
                "width": 1024,
                "height": 1024,
                "batch_size": 4
            },
            "class_type": "EmptyLatentImage"
        },
        "6": {
            "inputs": {
                "text": "a girl,full body,solo," + positive_prompt +
                        "(portrait:0.2),(exceptional, best aesthetic, new, newest, best quality, masterpiece, "
                        "extremely detailed:1.2)",
                "clip": [
                    "4",
                    1
                ]
            },
            "class_type": "CLIPTextEncode"
        },
        "7": {
            "inputs": {
                "text": "lowres,((bad anatomy)), ((bad hands))," + negative_prompt +
                        ",text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), "
                        "(poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), "
                        "((extra limbs)), extra face, (double head), (extra head), ((extra feet)),monster, logo, "
                        "cropped, worst quality, jpeg, humpbacked, ((long body)), long neck, ((jpeg artifacts)), "
                        "deleted, old, oldest, ((censored)), ((bad aesthetic)), (mosaic censoring, bar censor, "
                        "blur censor)",
                "clip": [
                    "4",
                    1
                ]
            },
            "class_type": "CLIPTextEncode"
        },
        "8": {
            "inputs": {
                "samples": [
                    "3",
                    0
                ],
                "vae": [
                    "4",
                    2
                ]
            },
            "class_type": "VAEDecode"
        },
        "9": {
            "inputs": {
                "filename_prefix": "API" + str(i),
                "images": [
                    "8",
                    0
                ]
            },
            "class_type": "SaveImage"
        }
    }
    }
    data = json.dumps(p).encode('utf-8')
    res = requests.post("http://127.0.0.1:8188/prompt", data=data)
    print(res.text)
    res = requests.get("http://127.0.0.1:8188/queue")
    print(res.text)
    i += 1
