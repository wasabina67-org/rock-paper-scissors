IMAGE_NAME = wasabina67/rock-paper-scissors
IMAGE_TAG = latest
CONTAINER_NAME = rock-paper-scissors

BUILD = docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
RUN = docker run -it --rm --name $(CONTAINER_NAME) $(IMAGE_NAME):$(IMAGE_TAG)
PUSH = docker push $(IMAGE_NAME):$(IMAGE_TAG)
PULL = docker pull $(IMAGE_NAME):$(IMAGE_TAG)

build:
	$(BUILD)
run:
	$(RUN)
push:
	$(PUSH)
pull:
	$(PULL)

.PHONY: build run push pull
