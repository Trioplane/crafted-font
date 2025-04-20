import mcfonts
import mcfonts.export_formats

font = mcfonts.from_java_font_file("./assets/minecraft/font/include/default.json")
exported = font.export(
    mcfonts.export_formats.opentype,
    {"name":"Crafted"}
)

with open("./build/crafted.otf", "wb") as file:
    file.write(exported)