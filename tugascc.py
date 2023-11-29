# Import modul math untuk menggunakan fungsi sqrt (akar kuadrat)
import math

# Fungsi untuk menghitung jarak Euclidean antara dua titik
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Fungsi untuk menyelesaikan masalah TSP (Traveling Salesman Problem) menggunakan pendekatan Greedy
def tsp_greedy(coordinates):
    num_cities = len(coordinates)
    visited = [False] * num_cities
    path = [0] * num_cities

    visited[0] = True
    current_city = 0

    # Loop untuk mengunjungi kota secara berurutan
    for i in range(1, num_cities):
        min_distance = float('inf')
        nearest_city = None

        # Loop untuk mencari kota terdekat yang belum dikunjungi
        for j in range(1, num_cities):
            if not visited[j]:
                distance = calculate_distance(coordinates[current_city], coordinates[j])
                # Memperbarui kota terdekat jika ditemukan jarak yang lebih kecil
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = j

        # Menandai kota terdekat sebagai dikunjungi, dan memperbarui kota saat ini
        path[i] = nearest_city
        visited[nearest_city] = True
        current_city = nearest_city

    # Kembali ke kota awal untuk menyelesaikan lintasan
    path[num_cities-1] = 0

    return path

# Contoh koordinat untuk diuji dengan algoritma Greedy TSP
coordinates = [(2, 5), (8, 3), (6, 9), (4, 7), (10, 2), (12, 6), (3, 10), (9, 8), (5, 4), (11, 1),
               (7, 12), (1, 9), (10, 5), (4, 3), (8, 11), (6, 1), (3, 7), (9, 4), (12, 10), (2, 2)]

# Menjalankan algoritma Greedy TSP dan menampilkan hasilnya
path = tsp_greedy(coordinates)
print("Greedy Algorithm:")
print("Path:", path)

# Menghitung dan menampilkan total jarak lintasan
total_distance = sum(calculate_distance(coordinates[path[i]], coordinates[path[i+1]]) for i in range(len(path)-1))
print("Total Distance:", total_distance)
