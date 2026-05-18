import folium

m = folium.Map(location=[-41, 174], zoom_start=5)

pois = [
    {
        "name": "Hobbiton - Matamata",
        "lat": -37.8575,
        "lon": 175.679722,
        "category": "lotr",
        "description": "Po prostu Shire",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/hobbiton_nz.jpg"
        ]
    },
    {
        "name": "Mordor - Tongariro National Park",
        "lat": -39.213635,
        "lon": 175.5875019444,
        "category": "lotr",
        "description": "Sceny z Mordoru",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/mordor_nz.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/mordor_2.jpg"
        ]
    },
    {
        "name": "Narnia Forest",
        "lat": -43.532,
        "lon": 172.636,
        "category": "narnia",
        "description": "Mystical forest landscapes connected to fantasy productions.",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/nz-03.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/nz-03.jpg"
        ]
    }
]

styles = {
    "lotr": {
        "color": "green",
        "icon": "tree"
    },

    "narnia": {
        "color": "red",
        "icon": "crown"
    }
}

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

    style = styles[poi["category"]]

    popup_html = f"""
    <div style="width:250px">

        <h3>{poi['name']}</h3>

        {popup_images}

        <div style="font-size:13px; color:#444;">
            {poi['description']}
        </div>

    </div>
    """

    folium.Marker(
        location=[poi["lat"], poi["lon"]],
        tooltip=poi["name"],

        popup=folium.Popup(
            popup_html,
            max_width=300
        ),

        icon=folium.Icon(
            color=style["color"],
            icon=style["icon"],
            prefix="fa"
        )

    ).add_to(m)

m.save("index.html")