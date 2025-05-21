# 引入之前定義的函數
import numpy as np
from pelt_segmentation import find_best_fixed_length_segment as find_best_fixed_length_segment_pelt_like

# --- 測試案例 1: 簡單的精確匹配 ---
query1 = [1, 2, 3]
serie1 = [0, 1, 1, 2, 3, 4, 5, 1, 2, 3, 6]
query1 = np.array(query1, dtype=np.float64)
serie1 = np.array(serie1, dtype=np.float64)
# 預期：在索引 2-4 (1,2,3) 和 7-9 (1,2,3) 都會找到，距離為0。
# 由於程式碼會取第一個找到的最小距離，所以結果可能取決於遍歷順序。
# 在這個實現中，預計會找到較早的那個。
# 實際輸出： (0.0, 2, 4) 或 (0.0, 7, 9)

print("--- 測試案例 1: 簡單的精確匹配 ---")
min_dist1, start_idx1, end_idx1 = find_best_fixed_length_segment_pelt_like(query1, serie1)
print(f"Query: {query1}, Serie: {serie1}")
print(f"最小距離: {min_dist1}, 起始索引: {start_idx1}, 結束索引: {end_idx1}")
print(f"找到的子片段: {serie1[start_idx1 : end_idx1 + 1] if start_idx1 != -1 else 'N/A'}\n")


# --- 測試案例 2: 沒有精確匹配，但有近似匹配 ---
query2 = [10, 20, 30]
serie2 = [1, 5, 12, 21, 28, 4, 9, 18, 27, 35]
query2 = np.array(query2, dtype=np.float64)
serie2 = np.array(serie2, dtype=np.float64)
# 預期：在索引 2-4 ([12, 21, 28]) 和 7-9 ([18, 27, 35]) 會有近似匹配。
# 計算距離：
# [12, 21, 28] vs [10, 20, 30] -> (12-10)^2 + (21-20)^2 + (28-30)^2 = 2^2 + 1^2 + (-2)^2 = 4 + 1 + 4 = 9
# [18, 27, 35] vs [10, 20, 30] -> (18-10)^2 + (27-20)^2 + (35-30)^2 = 8^2 + 7^2 + 5^2 = 64 + 49 + 25 = 138
# 預期輸出：(9.0, 2, 4)

print("--- 測試案例 2: 沒有精確匹配，但有近似匹配 ---")
min_dist2, start_idx2, end_idx2 = find_best_fixed_length_segment_pelt_like(query2, serie2)
print(f"Query: {query2}, Serie: {serie2}")
print(f"最小距離: {min_dist2}, 起始索引: {start_idx2}, 結束索引: {end_idx2}")
print(f"找到的子片段: {serie2[start_idx2 : end_idx2 + 1] if start_idx2 != -1 else 'N/A'}\n")


# --- 測試案例 3: serie 中有多個可能匹配，查詢長度為1 ---
query3 = [5]
serie3 = [1, 2, 5, 3, 6, 5, 4, 5, 7]
query3 = np.array(query3, dtype=np.float64)
serie3 = np.array(serie3, dtype=np.float64)
# 預期：會找到所有 5 的位置 (索引 2, 5, 7)。
# 由於距離都為 0，預計會返回第一個找到的。
# 預期輸出：(0.0, 2, 2)

print("--- 測試案例 3: serie 中有多個可能匹配，查詢長度為1 ---")
min_dist3, start_idx3, end_idx3 = find_best_fixed_length_segment_pelt_like(query3, serie3)
print(f"Query: {query3}, Serie: {serie3}")
print(f"最小距離: {min_dist3}, 起始索引: {start_idx3}, 結束索引: {end_idx3}")
print(f"找到的子片段: {serie3[start_idx3 : end_idx3 + 1] if start_idx3 != -1 else 'N/A'}\n")


# --- 測試案例 4: serie 比 query 短 ---
query4 = [1, 2, 3, 4, 5]
serie4 = [1, 2, 3]
query4 = np.array(query4, dtype=np.float64)
serie4 = np.array(serie4, dtype=np.float64)
# 預期：無法找到匹配，返回 float('inf'), -1, -1

print("--- 測試案例 4: serie 比 query 短 ---")
min_dist4, start_idx4, end_idx4 = find_best_fixed_length_segment_pelt_like(query4, serie4)
print(f"Query: {query4}, Serie: {serie4}")
print(f"最小距離: {min_dist4}, 起始索引: {start_idx4}, 結束索引: {end_idx4}")
print(f"找到的子片段: {serie4[start_idx4 : end_idx4 + 1] if start_idx4 != -1 else 'N/A'}\n")


# --- 測試案例 5: 空的 query ---
query5 = []
serie5 = [1, 2, 3]
query5 = np.array(query5, dtype=np.float64)
serie5 = np.array(serie5, dtype=np.float64)
# 預期：無法找到匹配，返回 float('inf'), -1, -1

print("--- 測試案例 5: 空的 query ---")
min_dist5, start_idx5, end_idx5 = find_best_fixed_length_segment_pelt_like(query5, serie5)
print(f"Query: {query5}, Serie: {serie5}")
print(f"最小距離: {min_dist5}, 起始索引: {start_idx5}, 結束索引: {end_idx5}")
print(f"找到的子片段: {serie5[start_idx5 : end_idx5 + 1] if start_idx5 != -1 else 'N/A'}\n")


# --- 測試案例 6: 空的 serie ---
query6 = [1, 2, 3]
serie6 = []
query6 = np.array(query6, dtype=np.float64)
serie6 = np.array(serie6, dtype=np.float64)
# 預期：無法找到匹配，返回 float('inf'), -1, -1

print("--- 測試案例 6: 空的 serie ---")
min_dist6, start_idx6, end_idx6 = find_best_fixed_length_segment_pelt_like(query6, serie6)
print(f"Query: {query6}, Serie: {serie6}")
print(f"最小距離: {min_dist6}, 起始索引: {start_idx6}, 結束索引: {end_idx6}")
print(f"找到的子片段: {serie6[start_idx6 : end_idx6 + 1] if start_idx6 != -1 else 'N/A'}\n")


# --- 測試案例 7: 長度較長，且存在跨 i_offset 的最佳解 ---
query7 = [10, 11]
serie7 = [1, 2, 3, 10, 11, 4, 5, 9, 12, 10, 11, 6, 7]
query7 = np.array(query7, dtype=np.float64)
serie7 = np.array(serie7, dtype=np.float64)
# query 長度為 2，i_offset 會有 0 和 1 兩種。
# 索引 3-4 (10,11) 距離 0，起始索引 3 % 2 == 1 -> i_offset = 1
# 索引 9-10 (10,11) 距離 0，起始索引 9 % 2 == 1 -> i_offset = 1
# 預期：找到 (0.0, 3, 4)

print("--- 測試案例 7: 長度較長，且存在跨 i_offset 的最佳解 ---")
min_dist7, start_idx7, end_idx7 = find_best_fixed_length_segment_pelt_like(query7, serie7)
print(f"Query: {query7}, Serie: {serie7}")
print(f"最小距離: {min_dist7}, 起始索引: {start_idx7}, 結束索引: {end_idx7}")
print(f"找到的子片段: {serie7[start_idx7 : end_idx7 + 1] if start_idx7 != -1 else 'N/A'}\n")

# --- 測試案例 8: 只有一個可能的子片段 ---
query8 = [50, 60]
serie8 = [10, 20, 51, 59]
query8 = np.array(query8, dtype=np.float64)
serie8 = np.array(serie8, dtype=np.float64)
# 預期：找到 (51, 59) 距離 (51-50)^2 + (59-60)^2 = 1^2 + (-1)^2 = 1 + 1 = 2
# 預期輸出：(2.0, 2, 3)

print("--- 測試案例 8: 只有一個可能的子片段 ---")
min_dist8, start_idx8, end_idx8 = find_best_fixed_length_segment_pelt_like(query8, serie8)
print(f"Query: {query8}, Serie: {serie8}")
print(f"最小距離: {min_dist8}, 起始索引: {start_idx8}, 結束索引: {end_idx8}")
print(f"找到的子片段: {serie8[start_idx8 : end_idx8 + 1] if start_idx8 != -1 else 'N/A'}\n")