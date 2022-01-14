import functools
# TODO: concurrent builds via multiprocessing
import multiprocessing
import os
import sys

import docker

IMAGE_TAG_NAMESPACE = "kelvintawl-cci"


@functools.lru_cache()
def client() -> docker.DockerClient:
    return docker.from_env()


def fullpath(rel_path: str) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, rel_path)


def _build_image(cli, path: str, img_tag: str, dockerfile: str = "Dockerfile"):
    # NOTE: does not emit build output, which may be problematic if trying to debug for caching
    # Otherwise, we may want to use the lower-level API in order to retrieve build outputs.
    # https://docker-py.readthedocs.io/en/stable/images.html#docker.models.images.ImageCollection.build
    return cli.images.build(
        path=path,
        nocache=False,  # use cached layers whenever we can
        quiet=False,
        tag=img_tag,
        dockerfile=dockerfile,
    )
           

def build_images(*directories):
    tag = os.environ.get("TAG", "latest")

    cli = client()
    build_image = functools.partial(_build_image, cli)

    for dir in directories:
        build_image(fullpath(dir), f"{IMAGE_TAG_NAMESPACE}/{dir}:{tag}")



if __name__ == "__main__":
    """
    Assumes this script is called with args to which folders to build Docker images for.
    Example:
        # to build all Docker images housed under the main/ slim/ and nginx/ directory.
        python build_images.py main slim nginx
    """
    _script, *directories = sys.argv
    build_images(*directories)
