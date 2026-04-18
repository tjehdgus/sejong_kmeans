import numpy as np
from scipy.spatial.distance import cdist

# 클러스터 중심과 종속변수(따릉이 위치) 간의 거리 계산
distances_to_black = cdist(centroids, dependent_data[['lat', 'lng']])

# 각 클러스터 중심에서 가장 가까운 따릉이 위치까지의 거리 계산
min_distances_to_black = np.min(distances_to_black, axis=1)

# 클러스터 중심점 중에서 특정 거리 이내에 따릉이 위치가 있는 비율 계산 (약 200미터)
threshold_distance = 0.002
accuracy_centroid_within_threshold = np.mean(min_distances_to_black < threshold_distance)
print(f"200미터 이내에 따릉이 위치가 있는 클러스터 중심점 비율: {accuracy_centroid_within_threshold * 100:.2f}%")
