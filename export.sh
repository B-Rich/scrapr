#!/bin/bash

declare -a VERTS=("restaurants")
#"restaurants"
#"document destruction"
#"copy machines"
#"print shops"
#"office furniture"
#"office equipment"
#"document imaging"
#"janitorial services"
#"painters"
#"pest control"
#"remodeling"
#"plumbers"
#"alarm systems")

declare -a CITIES=("El Paso")
#"Austin"
#"Dallas"
#"Houston"
#"San Antonio")

for city_index in "${!CITIES[@]}"
do

    for vert in "${VERTS[@]}"
    do
        BACKUP_DIR="/home/seth/Virtual Sales/MarkVerts/${CITIES[$city_index]}/output/"
        YB_FILES="/home/seth/Virtual Sales/MarkVerts/${CITIES[$city_index]}/raw/${vert// /_}_yb.csv"
        YP_FILES="/home/seth/Virtual Sales/MarkVerts/${CITIES[$city_index]}/raw/${vert// /_}_yp.csv"
        OUTPUT="/home/seth/Virtual Sales/MarkVerts/${CITIES[$city_index]}/output/${vert// /_}.csv"

        mkdir -p "$BACKUP_DIR"

        cat "$YB_FILES" "$YP_FILES" | python "/home/seth/Virtual Sales/MarkVerts/cleanup.py" > "$OUTPUT"
    done

done
