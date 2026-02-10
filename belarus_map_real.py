import json

cities = {
    "Минск": [53.9006, 27.5590], "Брест": [52.0977, 23.7341], "Гродно": [53.6688, 23.8298],
    "Лида": [53.8918, 25.3023], "Новогрудок": [53.5939, 25.8232], "Заславль": [54.0084, 27.2882],
    "Вилейка": [54.4904, 26.9114], "Браслав": [55.6385, 27.0305], "Миоры": [55.6174, 27.6259],
    "Шарковщина": [55.3621, 27.4647], "Полоцк": [55.4856, 28.7684], "Витебск": [55.1927, 30.2064],
    "Новолукомль": [54.6548, 29.1383], "Могилёв": [53.8981, 30.3325], "Гомель": [52.4312, 30.9937],
    "Слуцк": [53.0298, 27.5583], "Несвиж": [53.2185, 26.6713], "Пинск": [52.1158, 26.1031]
}

def fix_path(start_city, end_city, mid_points=None):
    path = [cities[start_city]]
    if mid_points: path.extend(mid_points)
    path.append(cities[end_city])
    return path

# Данные радиальных линий
rad_data = [
    {"target": "Брест", "txt": "350км, 3:40", "color": "blue", "path": fix_path("Минск", "Брест", [[53.2, 26.6], [52.5, 25.1]])},
    {"target": "Гродно", "txt": "280км, 3:00", "color": "blue", "path": fix_path("Минск", "Гродно", [[54.0, 26.5], [53.9, 25.3]]), "t_pos": 0.25}, # Исключение
    {"target": "Гомель", "txt": "310км, 3:15", "color": "blue", "path": fix_path("Минск", "Гомель", [[53.1, 29.2]])},
    {"target": "Витебск", "txt": "290км, 3:00", "color": "blue", "path": fix_path("Минск", "Витебск", [[54.3, 28.4]])},
    {"target": "Могилёв", "txt": "200км, 2:10", "color": "blue", "path": fix_path("Минск", "Могилёв", [[53.8, 29.0]])},
    {"target": "Пинск", "txt": "300км, 3:30", "color": "blue", "path": fix_path("Минск", "Пинск", [[53.0, 27.5], [52.2, 26.7]])},
    {"target": "Лида", "txt": "170км, 1:50", "color": "blue", "path": fix_path("Минск", "Лида", [[54.0, 26.5]]), "t_pos": 0.75}, # Исключение
    {"target": "Несвиж", "txt": "120км, 1:30", "color": "blue", "path": fix_path("Минск", "Несвиж", [[53.3, 26.7]])},
    {"target": "Слуцк", "txt": "105км, 1:20", "color": "blue", "path": fix_path("Минск", "Слуцк")},
    {"target": "Заславль", "txt": "25км, 0:30", "color": "blue", "path": fix_path("Минск", "Заславль")},
    {"target": "Вилейка", "txt": "100км, 1:30", "color": "blue", "path": fix_path("Минск", "Вилейка", [[54.2, 27.2]])},
    {"target": "Новогрудок", "txt": "150км, 1:50", "color": "blue", "path": fix_path("Минск", "Новогрудок", [[53.5, 26.4]])},
    {"target": "Полоцк", "txt": "230км, 2:50", "color": "blue", "path": fix_path("Минск", "Полоцк", [[54.6, 27.9]])},
    {"target": "Браслав", "txt": "240км, 3:15", "color": "blue", "path": fix_path("Минск", "Браслав", [[54.5, 27.2], [55.2, 27.2]])},
    {"target": "Миоры", "txt": "240км, 3:10", "color": "blue", "path": fix_path("Минск", "Миоры", [[54.5, 27.2]])},
    {"target": "Шарковщина", "txt": "210км, 2:50", "color": "blue", "path": fix_path("Минск", "Шарковщина", [[54.8, 27.4]])},
    {"target": "Новолукомль", "txt": "180км, 2:15", "color": "blue", "path": fix_path("Минск", "Новолукомль", [[54.3, 28.4]])},
    {"target": "Брест_Розовая", "txt": "255км, 2:40", "color": "deeppink", "path": fix_path("Несвиж", "Брест", [[52.7, 25.4]])}
]

circle_data = [
    {"from": "Брест", "to": "Гродно", "txt": "240км, 3:00", "path": fix_path("Брест", "Гродно", [[52.4, 23.9], [53.1, 24.4]])},
    {"from": "Гродно", "to": "Лида", "txt": "110км, 1:20", "path": fix_path("Гродно", "Лида", [[53.6, 24.6]])},
    {"from": "Лида", "to": "Новогрудок", "txt": "55км, 0:50", "path": fix_path("Лида", "Новогрудок", [[53.7, 25.6]])},
    {"from": "Новогрудок", "to": "Заславль", "txt": "130км, 1:30", "path": fix_path("Новогрудок", "Заславль", [[53.5, 26.4], [53.9, 27.1]])},
    {"from": "Заславль", "to": "Вилейка", "txt": "85км, 1:10", "path": fix_path("Заславль", "Вилейка", [[54.2, 27.2]])},
    {"from": "Вилейка", "to": "Браслав", "txt": "180км, 2:30", "path": fix_path("Вилейка", "Браслав", [[55.1, 26.8]])},
    {"from": "Браслав", "to": "Миоры", "txt": "45км, 0:45", "path": fix_path("Браслав", "Миоры")},
    {"from": "Миоры", "to": "Шарковщина", "txt": "30км, 0:30", "path": fix_path("Миоры", "Шарковщина")},
    {"from": "Шарковщина", "to": "Полоцк", "txt": "95км, 1:20", "path": fix_path("Шарковщина", "Полоцк", [[55.5, 28.1]])},
    {"from": "Полоцк", "to": "Витебск", "txt": "105км, 1:30", "path": fix_path("Полоцк", "Витебск", [[55.2, 29.5]])},
    {"from": "Витебск", "to": "Новолукомль", "txt": "115км, 1:40", "path": fix_path("Витебск", "Новолукомль", [[54.9, 29.8]])},
    {"from": "Новолукомль", "to": "Могилёв", "txt": "120км, 1:45", "path": fix_path("Новолукомль", "Могилёв", [[54.2, 29.7]])},
    {"from": "Могилёв", "to": "Гомель", "txt": "180км, 2:10", "path": fix_path("Могилёв", "Гомель", [[53.1, 30.2]])},
    {"from": "Гомель", "to": "Слуцк", "txt": "270км, 3:20", "path": fix_path("Гомель", "Слуцк", [[52.1, 30.0], [52.4, 28.5]])},
    {"from": "Слуцк", "to": "Несвиж", "txt": "70км, 1:00", "path": fix_path("Слуцк", "Несвиж")},
    {"from": "Несвиж", "to": "Пинск", "txt": "160км, 2:00", "path": fix_path("Несвиж", "Пинск", [[52.6, 26.4]])},
    {"from": "Пинск", "to": "Брест", "txt": "180км, 2:10", "path": fix_path("Пинск", "Брест", [[52.2, 25.2]])},
]

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Карта Беларуси v9</title>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        #map { height: 100vh; width: 100%; background: #ffffff; }
        .city-label { font-size: 10pt; font-weight: bold; color: #111; white-space: nowrap; pointer-events: none; }
        .line-label { font-size: 8pt; font-weight: bold; white-space: nowrap; cursor: pointer; }
        path { transition: opacity 0.3s; outline: none !important; }
        .custom-control { background: white; padding: 10px; border-radius: 6px; box-shadow: 0 1px 5px rgba(0,0,0,0.2); }
    </style>
</head>
<body>
    <div id="map"></div>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://unpkg.com/leaflet-polylineoffset/leaflet.polylineoffset.js"></script>
    <script>
        var map = L.map('map').setView([53.7, 27.5], 7);
        L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png').addTo(map);

        var allLines = { radial: [], circle: [] };

        function toggleLine(line, labelId, forceState) {
            var txt = document.getElementById(labelId);
            var isHidden = forceState !== undefined ? !forceState : line.options.opacity > 0.2;
            line.setStyle({opacity: isHidden ? 0.1 : 0.7, weight: isHidden ? 2 : 3});
            if(txt) txt.style.opacity = isHidden ? 0.2 : 1;
        }

        function addRoad(type, path, text, color, offsetValue, tPos) {
            var line = L.polyline(path, { color: color, weight: 3, opacity: 0.7, offset: offsetValue, cursor: 'pointer' }).addTo(map);
            var idx = Math.floor(path.length * (tPos || 0.5));
            if (idx >= path.length) idx = path.length - 1;
            var pos = path[idx];
            var labelId = 'txt_' + L.stamp(line);

            L.marker(pos, {
                icon: L.divIcon({
                    className: 'line-label',
                    html: '<div id="' + labelId + '" style="color:' + color + '; text-shadow: 2px 2px 0 #fff, -2px -2px 0 #fff;">' + text + '</div>',
                    iconAnchor: [20, type === 'radial' ? 14 : -6]
                })
            }).addTo(map);

            var action = function() { toggleLine(line, labelId); };
            line.on('click', action);
            setTimeout(() => { if(document.getElementById(labelId)) document.getElementById(labelId).onclick = action; }, 500);
            allLines[type].push({line: line, labelId: labelId});
        }
"""

html_content += f"var radData = {json.dumps(rad_data)};\n"
html_content += f"var circleData = {json.dumps(circle_data)};\n"
html_content += f"var cityCoords = {json.dumps(cities)};\n"

html_content += """
        radData.forEach(r => addRoad('radial', r.path, r.txt, r.color, -2, r.t_pos));
        circleData.forEach(c => addRoad('circle', c.path, c.txt, 'red', 2));

        for (var name in cityCoords) {
            L.circleMarker(cityCoords[name], {radius: 4, color: '#000', fillColor: '#fff', fillOpacity: 1, weight: 2}).addTo(map);
            
            var ox = 12, oy = -12;
            // Ювелирная настройка позиций для Гродно, Бреста и Лиды
            if (name === "Гродно") { ox = -45; oy = 0; } 
            if (name === "Брест") { ox = -35; oy = 10; } 
            if (name === "Лида") { ox = 10; oy = 10; } 

            L.marker(cityCoords[name], {
                icon: L.divIcon({ 
                    className: 'city-label', 
                    html: '<div style="margin-left: '+ox+'px; margin-top: '+oy+'px;">' + name + '</div>' 
                })
            }).addTo(map);
        }

        var ctrl = L.control({position: 'topright'});
        ctrl.onAdd = function() {
            var div = L.DomUtil.create('div', 'custom-control');
            div.innerHTML = '<strong>Фильтр</strong><br>' +
                '<label><input type="checkbox" id="chk_rad" checked> Радиальные</label><br>' +
                '<label><input type="checkbox" id="chk_circ" checked> Кольцевые</label>';
            return div;
        };
        ctrl.addTo(map);

        setTimeout(() => {
            document.getElementById('chk_rad').onchange = function() {
                allLines.radial.forEach(obj => toggleLine(obj.line, obj.labelId, this.checked));
            };
            document.getElementById('chk_circ').onchange = function() {
                allLines.circle.forEach(obj => toggleLine(obj.line, obj.labelId, this.checked));
            };
        }, 300);
    </script>
</body>
</html>
"""

with open("belarus_map_v9.html", "w", encoding="utf-8") as f:
    f.write(html_content)