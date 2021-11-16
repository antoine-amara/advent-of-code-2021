# Advent Of Code 2021

The dev environment and the solutions for Advent Of Code 2021.

Each solution has a python script with the name pattern: day-{N}.py.

## How to use

First, you need vscode and remote container extension installed:
- vscode: https://code.visualstudio.com/Download
- tuto on how to install and use remote container extension: https://code.visualstudio.com/docs/remote/containers

If you have vscode and remote container, open this workspace into the container, run a vscode terminal, and launch this command to install dependencies:
```shell
make dependencies
```

It will install all dependencies inside the remote container with poetry.

You are done, the environment is ready.

To launch a solution for one day:

```shell
make run day={{N}}
```

To see other available commands:

```shell
make help
```
