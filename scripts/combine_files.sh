#!/bin/bash

find ~/Downloads/ -type f -print0 | xargs -0 mv -t ~/Videos
find /home/acworks/Documents/projects/ac-artist/wikiart/wikiart-saved/images/vincent-van-gogh/ -type f -print0 | xargs -0 cp -t /home/acworks/Documents/projects/ac-artist/pytorch-CycleGAN-and-pix2pix/datasets/vincent-van-gogh/trainA/
