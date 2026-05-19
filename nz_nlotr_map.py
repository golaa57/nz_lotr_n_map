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
        "name": "Mount Doom - Mount Ngauruhoe",
        "lat": -39.1568333333,
        "lon": 175.6321666667,
        "category": "lotr",
        "description": "Góra, gdzie wrzucają pierścień",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/mount_doom_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/mount_doom_2.jpg"
        ]
    },
    {
        "name": "Rivendell - Kaitoke Regional Park",
        "lat": -41.069027,
        "lon": 175.198658,
        "category": "lotr",
        "description": "Dom elfów",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/rivendell_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/rivendell_2.jpg"
        ]
    },
    {
        "name": "Ścieżka umarłych - Pūtangirua Pinnacles",
        "lat": -41.4507,
        "lon": 175.2223,
        "category": "lotr",
        "description": "Aragorn idzie do króla umarłych",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/death_path_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/death_path_2.jpg"
        ]
    },
    {
        "name": "Ogrody Isengardu - Harcourt Park",
        "lat": -41.1020,
        "lon": 175.0960,
        "category": "lotr",
        "description": "Ogrody, w których rozmawiają Gandalf z Sarumanem",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/isengard_g_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/isengard_g_2.jpg"
        ]
    },
    {
        "name": "Glenorchy",
        "lat": -44.85,
        "lon": 168.3833333333,
        "category": "both",
        "description": "Różne sceny z LOTRa i Narnii. Ciężko mi znaleźć jakieś konkretne ujęcia, ale to jest po prostu ładna okolica",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/glenorchy_1.jpg"
        ]
    },
    {
        "name": "Rzeka Dart",
        "lat": -44.8466666667,
        "lon": 168.3647222222,
        "category": "both",
        "description": "Rzeka z LOTRa i Narnii. Sceny z Kaspiana czy Drużyny Pierścienia",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/dart_1.jpg"
        ]
    },
    {
        "name": "Nen Hithoel - jeziora Mavora",
        "lat": -45.2555555556,
        "lon": 168.1680555556,
        "category": "lotr",
        "description": "Rzeka z LOTRa. Pływają po niej w drużynie pierścienia",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/mavora_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/mavora_2.jpg"
        ]
    },
    {
        "name": "Queenstown",
        "lat": -45.0311111111,
        "lon": 168.6625,
        "category": "lotr",
        "description": "Różne sceny z LOTRa. Ładnie",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/queen_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/queen_2.jpg"
        ]
    },
    {
        "name": "Edoras - Mount Sunday",
        "lat": -43.5480555556,
        "lon": 170.8930555556,
        "category": "lotr",
        "description": "Edoras, czyli państwo koników. Głównie w drugiej części",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/edoras_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/edoras_2.jpg"
        ]
    },
    {
        "name": "Pola Pelennoru - Twizel",
        "lat": -44.25,
        "lon": 170.1,
        "category": "lotr",
        "description": "Bitwa z trzeciej części",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/pelennor_1.jpg"
        ]
    },
    {
        "name": "Jezioro Pukaki",
        "lat": -44.1166666667,
        "lon": 170.1666666667,
        "category": "lotr",
        "description": "Bliżej nieokreślone ujęcia. Też ładnie",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/pukaki_1.jpg"
        ]
    },
    {
        "name": "Argonath i Fangorn - Fiordland National Park",
        "lat": -45.4283305556,
        "lon": 167.3622888889,
        "category": "lotr",
        "description": "Las entów z drugiej części. Rzeka z pierwszej części",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/fiordland_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/fiordland_2.jpg"
        ]
    },
    {
        "name": "Rzeka - Kawarau Gorge",
        "lat": -45.02,
        "lon": 169.09,
        "category": "lotr",
        "description": "Rzeka z pierwszej części",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/kawa_1.jpg"
        ]
    },
    {
        "name": "Remarkables",
        "lat": -45.0719444444,
        "lon": 168.8080555556,
        "category": "lotr",
        "description": "Bliżej nieokreślone ujęcia z LOTRa/Hobbita",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/remark_1.jpg"
        ]
    },
    {
        "name": "Mount Aspiring National Park",
        "lat": -44.3833333333,
        "lon": 168.7333333333,
        "category": "lotr",
        "description": "Różne z LOTRa. Wydaję mi się, że np. ujęcia z przekazywaniem sygnału w trzeciej części",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/aspi_1.jpg"
        ]
    },
    {
        "name": "Rohan - Canterbury Plains",
        "lat": -43.64,
        "lon": 172.09,
        "category": "lotr",
        "description": "Pono Rohan, ale to jest duży region",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/rohan_1.jpg"
        ]
    },
    {
        "name": "Wejście do Narnii w Kaspianie - Cathedral Cove",
        "lat": -36.8283,
        "lon": 175.7900,
        "category": "narnia",
        "description": "W tym miejscu pojawiają się pierwszy raz w Narnii w drugiej części.",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/cove_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/cove_2.jpg"
        ]
    },
    {
        "name": "Plaża z Kaspiana - Coromandel Peninsula",
        "lat": -37.0163888889,
        "lon": 175.6786111111,
        "category": "narnia",
        "description": "Plaża, gdzie się bawią po przybyciu w drugiej części. Ruiny cair paravel. Cathedral Cove jest elementem tego półwyspu",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/coro_1.jpg"
        ]
    },
    {
        "name": "Bitwa - Flock Hill",
        "lat": -43.1301611111,
        "lon": 171.772325,
        "category": "narnia",
        "description": "Miejsce głównej bitwy z pierwszej części",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/bitwa_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/bitwa_2.jpg"
        ]
    },
    {
        "name": "Obóz Aslana - Elephant Rocks",
        "lat": -44.8935,
        "lon": 170.6562,
        "category": "narnia",
        "description": "Obóz Aslana z pierwszej części",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/aslan_1.jpg",
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/aslan_2.jpg"
        ]
    },
    {
        "name": "Niby bitwa - Anatini Fossil Site",
        "lat": -44.89336,
        "lon": 170.65621,
        "category": "narnia",
        "description": "Niby kontynuacja bitwa z pierwszej części, ale jest to niemal ta sama lokalizacja, co obóz Aslana",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/bit_1.jpg"
        ]
    },
    {
        "name": "Zatoka Purakaunui",
        "lat": -45.75,
        "lon": 170.6333333333,
        "category": "narnia",
        "description": "Chyba plaża, po której idzie Aslan w pierwszej części",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/pura_1.jpg"
        ]
    },
    {
        "name": "Christchurch",
        "lat": -43.53,
        "lon": 172.6202777778,
        "category": "narnia",
        "description": "Różne sceny z Narnii",
        "images": [
            "https://raw.githubusercontent.com/golaa57/nz_lotr_n_map/main/images/christ_1.jpg"
        ]
    },
]

styles = {
    "lotr": {
        "color": "green",
        "icon": "tree"
    },
    "narnia": {
        "color": "red",
        "icon": "crown"
    },
    "both": {
        "color": "blue",
        "icon": "shield"
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