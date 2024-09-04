# rock-paper-scissors

[![Docker Pulls](https://img.shields.io/docker/pulls/wasabina67/rock-paper-scissors)](https://hub.docker.com/r/wasabina67/rock-paper-scissors)
[![Docker Stars](https://img.shields.io/docker/stars/wasabina67/rock-paper-scissors)](https://hub.docker.com/r/wasabina67/rock-paper-scissors)

Rock paper scissors 🪨📃✂️

## QuickStart

<details><summary>rock_paper_scissors.mp4</summary>

<video controls src="https://github.com/user-attachments/assets/0a81f397-f8d8-4256-8c8c-d57537218219" muted="false"></video>

</details>

```bash
docker pull wasabina67/rock-paper-scissors:latest
```

```bash
docker run -it --rm --name rock-paper-scissors wasabina67/rock-paper-scissors:latest
```

## Example

```bash
$ docker run -it --rm --name rock-paper-scissors wasabina67/rock-paper-scissors:latest
Choose Rock(1), Paper(2), or Scissors(3): 1
Computer chose: Rock(1)
It's draw!
```

```bash
$ docker run -it --rm --name rock-paper-scissors wasabina67/rock-paper-scissors:latest
Choose Rock(1), Paper(2), or Scissors(3): 3
Computer chose: Paper(2)
You win!
```
