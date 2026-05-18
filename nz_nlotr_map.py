import folium

m = folium.Map(location=[-41, 174], zoom_start=5)

pois = [
    {
        "name": "Hobbiton",
        "lat": -37.872,
        "lon": 175.682,
        "description": "The Shire filming location.",
        "images": [
            "https://upload.wikimedia.org/wikipedia/commons/6/6f/Hobbiton_Movie_Set.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/6/67/Hobbiton_houses.jpg"
        ]
    }
]

for poi in pois:

    popup_images = ""

    for image_url in poi["images"]:
        popup_images += f"""
        <img
            src="{image_url}"
            width="250"
            style="
                margin-bottom:10px;
                border-radius:10px;
            "
        >
        """

    popup_html = f"""
    <div style="width:260px">

        <h3>{poi['name']}</h3>

        {popup_images}

        <p>{poi['description']}</p>

    </div>
    """

    folium.Marker(
        location=[poi["lat"], poi["lon"]],
        popup=folium.Popup(popup_html, max_width=300)
    ).add_to(m)

m.save("nz_map.html")