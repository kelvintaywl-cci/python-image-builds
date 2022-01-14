# python-image-builds

Exploring building Docker images concurrently with Python

## What is this about?

[Docker provides a Python SDK](https://github.com/docker/docker-py).

That plays nicely with me, as I want to easily script concurrent image builds! :whale:

In this sample project, we have 3 folders, and each folder has its own _Dockerfile_.

```console

$ tree .
.
├── README.md
├── build_images.py
├── complete
│   └── Dockerfile
├── nginx
│   ├── Dockerfile
│   └── static
│       ├── 50x.html
│       └── index.html
├── requirements.txt
└── slim
    └── Dockerfile
```

As such, we want to easily build the 3 Docker images, and do so **in parallel**, rather than sequentially.

```console

$ pip install -r requirements

# IF we only want to build from `slim/` and `nginx/` directories
$ python build_images.py slim nginx
```
