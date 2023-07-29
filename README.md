# Development Settings Sync

[![GitHub Actions](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FIanStorm%2Fdev-settings-sync%2Fbadge%3Fref%3Dmain&style=flat&label=build&logo=none)](https://actions-badge.atrox.dev/IanStorm/dev-settings-sync/goto?ref=main)
[![Docker Pulls](https://img.shields.io/docker/pulls/ianstorm/dev-settings-sync)](https://hub.docker.com/r/ianstorm/dev-settings-sync)
[![Docker Stars](https://img.shields.io/docker/stars/ianstorm/dev-settings-sync)](https://hub.docker.com/r/ianstorm/dev-settings-sync)

Development support project for **private purposes**.
Syncs settings files across different repositories.

**🐳 Make sure you have installed *Docker*.**


## How to use in "production"? 👨‍💼 👩‍💼

Files to sync are determined by their *relative file path*.
(Relative with respect to the project root.)


### Manual execution 🔧

1. Follow ["How to get a pre-built Docker image?"](#-how-to-get-a-pre-built-docker-image-☁️)
2. Run the Docker image:
	* either run the *check*:
```
$	docker run
		-t
		-v ${PWD}/:/mnt/
		ianstorm/dev-settings-sync
		check
```
*
	* or run the *sync*:
```
$	docker run
		-t
		-v ${PWD}/:/mnt/
		ianstorm/dev-settings-sync
		sync
```


### Automatic execution 🤖

It is highly recommended to include this project in your CI.
The simplest approach is to add an empty `.github/workflows/dev-settings-sync.yml` to the consuming repository.
Then run the *sync*, see [manual execution](#-manual-execution-🔧).


## How to develop? 👨‍💻 👩‍💻

Make sure you have installed *Visual Studio Code*.

1. Clone this repository.
2. `cd` inside the cloned folder.
2. Install the recommended extensions.
2. Build the Docker image: Run the vscode task `build`.


## Appendix


### How to get a pre-built Docker image? ☁️

Get the latest Docker image from Docker Hub:
```
$	docker pull ianstorm/dev-settings-sync:latest
```
