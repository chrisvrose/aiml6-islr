#!/bin/bash
rm -f combined/**/*
mkdir -p combined
rsync -a --info=progress2 Indian/ combined/
rsync -a --info=progress2 self/ combined/
rsync -a --info=progress2 asl_deriv/ combined/
