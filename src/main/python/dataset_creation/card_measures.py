#TODO modificare le misure in base alle esigenze
cardW = 56  #larghezza della carta
cardH = 94  #altezza della carta
cornerXmin = 1  #dal bordo a sinistra al bounding box desiderato
cornerXmax = 17  #dal bordo a sinistra alla fine del bounding box desiderato
cornerYmin = 2  #dal bordo in alto al bounding box desiderato
cornerYmax = 19  #dal bordo in alto alla fine del bounding box desiderato

# We convert the measures from mm to pixels: multiply by an arbitrary factor 'zoom'
# You shouldn't need to change this
zoom = 4
cardW *= zoom
cardH *= zoom
cornerXmin = int(cornerXmin * zoom)
cornerXmax = int(cornerXmax * zoom)
cornerYmin = int(cornerYmin * zoom)
cornerYmax = int(cornerYmax * zoom)
