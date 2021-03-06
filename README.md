# kkafplay

A Python-based audio file player with quirky features that you may never need.

Despite its insignificance, it mainly serves as a minimal Python application template that my other Python projects could copy from.

The template includes the following

- Project file/folder layout
- PEP8 compliant source code
- Automated tests
- User documentation and doc-generation pipeline
- Dependency management setup
- Continuous integration pipeline, including cross-platform distribution

Application end-users should be able to take the binary installer and use as is. 
Developers should be able to build the app all the way to the binary installer.

## Prerequisites

Install [PortAudio](http://www.portaudio.com).

### macOS

Through [Homebrew](https://brew.sh),
```shell
brew install portaudio 
```

You may need to remove code signature first with

```shell
codesign --remove-signature /usr/local/opt/portaudio/lib/libportaudio.2.dylib
```

### Windows

Download the latest distribution from [PortAudio website](http://files.
portaudio.com/archives/pa_stable_v190600_20161030.tgz) and build from source,
or through [Chocolatey](https://chocolatey.org)

```shell
choco install portaudio
```
