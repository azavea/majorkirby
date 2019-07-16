# majorkirby [![Build Status](https://travis-ci.org/azavea/majorkirby.svg)](https://travis-ci.org/azavea/majorkirby)

Puts CloudFormation stacks into motion.

## Testing

There are two ways to run the built-in test suite. One is intended to be run locally, while the other is setup to run within a Docker container.

### Local

The local tests require a working installation of Python 3:

```bash
$ python3 setup.py test
```

### Docker

The Docker setup builds an image with Python 3 installed, along with all of this project's dependencies. Build the image and launch the container with Docker Compose:

```bash
$ docker-compose build majorkirby
$ docker-compose run majorkirby python setup.py test
```
