#!/bin/bash -x

declare -a VERTS=("copy machines"
"print shops"
"office furniture"
"office equipment")

declare -a CITIES=("Las Cruces")

declare -a CITY_SEARCH=("Las Cruces, NM")

#declare -a VERTS=("bars"
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
#"alarm systems"
#"doctors"
#"attorneys")

#declare -a CITIES=("Las Cruces"
#"Santa Fe"
#"Albuquerque")

#declare -a CITY_SEARCH=("Las Cruces, NM"
#"Santa Fe, NM"
#"Albuquerque, NM")

for city_index in "${!CITIES[@]}"
do

    mkdir -p "/home/seth/Virtual Sales/MarkVerts/${CITIES[$city_index]}/raw/"

    for vert in "${VERTS[@]}"
    do
        python scrape.py --what "$vert" --where "${CITY_SEARCH[$city_index]}" > "/home/seth/Virtual Sales/MarkVerts/${CITIES[$city_index]}/raw/${vert// /_}_yp.csv"
    done

done