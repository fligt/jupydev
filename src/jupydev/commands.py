# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import subprocess


def jupydev_docs(): 

    subprocess.run(
        ["echo", "Running: echo hi..."], 
        check=True) 

    subprocess.run(
        ["echo", "hi"], 
        check=True) 

if __name__ == '__main__': 
    jupydev_docs()

# %%
