#!/bin/bash

# Ubuntu
find ~/Downloads/ -type f -print0 | xargs -0 cp -t ~/Videos
find /home/acworks/Documents/projects/ac-artist/wikiart/wikiart-saved/images/vincent-van-gogh/ -type f -print0 | xargs -0 cp -t /home/acworks/Documents/projects/ac-artist/pytorch-CycleGAN-and-pix2pix/datasets/vincent-van-gogh/trainA/


find . -type f -print0 | sort -zR | tail -zn +2001 | xargs -0 rm


# Mac OS
find images/vincent-van-gogh/ -type f -print0 | xargs -0 -I{} cp {} dataset/vincent-van-gogh/
