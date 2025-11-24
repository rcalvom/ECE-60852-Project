# Automatic Refinement of Unit Proofs with Large Language Models

This is an Automatic Refiner of Unit Proofs based on [CBMC](https://www.cprover.org/cbmc/).

## Requirements

* Docker 28 or higher (developed and tested with Docker 28.0.4)
* Python 3.12 (developed and tested with Python 3.12.11)
* docker-compose

## Usage

```bash
python manage.py \
  debugger \
  --harness_dir=/workdir/RIOT/cbmc/harness_gen_tests/_gcoap_forward_proxy_copy_options \
  --project_dir=/workdir/RIOT \
  --harness_file=/workdir/RIOT/cbmc/harness_gen_tests/_gcoap_forward_proxy_copy_options/_gcoap_forward_proxy_copy_options_harness.c
```

## Notes

This project was developed for the course [ECE60852 Holistic Software Security](https://purs3lab.github.io/hss/) at Purdue University.

Developed by Ricardo Andres Calvo Mendez.
