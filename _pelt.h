#ifndef PELT_H
#define PELT_H

/* 計算兩序列的平方歐幾里德距離 */
double squared_distance(const double *seq1, const double *seq2, int len);

/* PELT-like 固定長度分段搜尋 */
void pelt_segment(
    const double *serie, int n,
    const double *query, int q,
    double *out_best_dist,
    int *out_best_start,
    int *out_best_end
);

#endif /* PELT_H */
