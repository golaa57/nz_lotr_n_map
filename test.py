import folium

# Create map centered on New Zealand
m = folium.Map(
    location=[-41.0, 174.0],
    zoom_start=5
)

# Example POI
html = """
"""

folium.Marker(
    location=[-44.6718, 167.9250],
    popup=folium.Popup(html, max_width=300),
    tooltip="Milford Sound"
).add_to(m)

# Save map
m.save("new_zealand_map.html")