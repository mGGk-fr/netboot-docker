# Netboot Docker

Netboot docker is a simple docker image to serve Netboot Menu to Naomi NetDimm System

Mainly based upon [DragonMinded netboot lib](https://github.com/DragonMinded/netboot)

## Setup

### Env vars

- DIMM_IMP : Ip of your NetDimm

### Ports

- 8000 : Webserver Port

### Run it

```bash
docker run -v roms_dir:/opt/netboot/netboot/roms -p 8000:8000 mggk/netboot
```

## Todo

- Better web interface
- List available roms
