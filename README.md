# majorkirby [![CI](https://github.com/azavea/majorkirby/actions/workflows/ci.yml/badge.svg)](https://github.com/azavea/majorkirby/actions/workflows/ci.yml)

Puts CloudFormation stacks into motion.

This project uses `boto3` for AWS CloudFormation.

## Testing

There are two ways to run the built-in test suite. One is intended to be run locally, while the other is setup to run within a Docker container.

### Local

The local tests require a working installation of Python 3.

Install dependencies (including test extras) and run the tests:

```bash
$ python3 -m pip install -e '.[test]'
$ python3 -m unittest
```

If you prefer `uv`:

```bash
$ uv pip install -e '.[test]'
$ uv run python -m unittest
```

The legacy setuptools test runner is still supported:

```bash
$ python3 setup.py test
```

### Docker

The Docker setup builds an image with Python 3 installed, along with all of this project's dependencies. Build the image and launch the container with Docker Compose:

```bash
$ docker-compose build majorkirby
$ docker-compose run majorkirby python -m pip install -e '.[test]'
$ docker-compose run majorkirby python -m unittest
```

If you prefer to keep using the legacy setuptools test runner:

```bash
$ docker-compose run majorkirby python setup.py test
```
