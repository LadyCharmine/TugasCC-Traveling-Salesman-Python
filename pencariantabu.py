# Mengimpor modul math untuk fungsi matematika
import math

# Mengimpor modul random untuk mengacak urutan kota awal
import random

# Fungsi untuk menghitung jarak Euclidean antara dua titik
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Fungsi untuk menghitung total jarak perjalanan berdasarkan suatu lintasan
def calculate_total_distance(path, coordinates):
    total_distance = 0
    num_cities = len(path)

    # Loop untuk menghitung jarak antar kota dalam lintasan
    for i in range(num_cities-1):
        from_city = path[i]
        to_city = path[i+1]
        total_distance += calculate_distance(coordinates[from_city], coordinates[to_city])

    # Menambahkan jarak dari kota terakhir kembali ke kota awal
    total_distance += calculate_distance(coordinates[path[num_cities-1]], coordinates[path[0]])

    return total_distance

# Fungsi untuk mendapatkan tetangga dari suatu lintasan
def get_neighborhood(path):
    neighborhood = []
    num_cities = len(path)

    # Nested loop untuk menghasilkan lintasan-lintasan yang berbeda
    for i in range(1, num_cities-1):
        for j in range(i+1, num_cities):
            new_path = path.copy()
            # Swap kota pada posisi i dan j untuk mendapatkan lintasan yang berbeda
            new_path[i] = path[j]
            new_path[j] = path[i]
            neighborhood.append(new_path)

    return neighborhood

# Fungsi untuk menjalankan algoritma Tabu Search untuk TSP
def tsp_tabu_search(coordinates, num_iterations):
    num_cities = len(coordinates)
    current_path = list(range(num_cities))
    random.shuffle(current_path)
    best_path = current_path.copy()
    tabu_list = []

    # Loop untuk iterasi sebanyak num_iterations
    for _ in range(num_iterations):
        neighborhood = get_neighborhood(current_path)
        best_neighborhood_path = None
        best_neighborhood_distance = float('inf')

        # Loop untuk mencari lintasan terbaik dalam tetangga
        for path in neighborhood:
            if path not in tabu_list:
                distance = calculate_total_distance(path, coordinates)
                if distance < best_neighborhood_distance:
                    best_neighborhood_distance = distance
                    best_neighborhood_path = path

        # Memperbarui lintasan saat ini dengan lintasan terbaik dalam tetangga
        current_path = best_neighborhood_path

        # Memperbarui lintasan terbaik jika ditemukan lintasan yang lebih baik
        if best_neighborhood_distance < calculate_total_distance(best_path, coordinates):
            best_path = best_neighborhood_path

        # Menambahkan lintasan terbaik dalam tetangga ke dalam daftar tabu
        tabu_list.append(best_neighborhood_path)
        if len(tabu_list) > 10:
            tabu_list.pop(0)

    return best_path

# Koordinat contoh
coordinates = [(2, 5), (8, 3), (6, 9), (4, 7), (10, 2), (12, 6), (3, 10), (9, 8), (5, 4), (11, 1),
               (7, 12), (1, 9), (10, 5), (4, 3), (8, 11), (6, 1), (3, 7), (9, 4), (12, 10), (2, 2)]

# Jumlah iterasi untuk algoritma Tabu Search
num_iterations = 1000

# Menjalankan algoritma Tabu Search dan menampilkan hasilnya
best_path = tsp_tabu_search(coordinates, num_iterations)

print("Tabu Search Algorithm:")
print("Path:", best_path)
total_distance = calculate_total_distance(best_path, coordinates)
print("Total Distance:", total_distance)
