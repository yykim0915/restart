#!/bin/bash

mongoimport -d test -c citytour --headerline --type csv --drop citytour.csv
